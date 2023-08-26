import sys
# root_path = 'C:\\Users\\chris\\OneDrive\\Área de Trabalho\\Mestrado\\Período 1\\Técnicas Computacionais Avançadas\\Tca\\tca-project'
# sys.path.insert(0, root_path)

from mpi4py import MPI
import heapq
import time


def merge_local_results(sorted_parts):
    # create a priority queue for the merging
    priority_queue = []

    # initialize the result list
    sorted_result = []

    for i, part in enumerate(sorted_parts):
        if part:
            # Add the first element of each sorted part to the priority queue
            heapq.heappush(priority_queue, (part[0], i, 0))

    # merges the elements while the priority queue isn't empty
    while priority_queue:
        # remove the element with minimum value within the priority queue
        value, part_idx, element_idx = heapq.heappop(priority_queue)

        # add the removed value to the result list
        sorted_result.append(value)

        # add +1 to the element refference within a local list
        element_idx += 1
        if element_idx < len(sorted_parts[part_idx]):
            # add the new element to the priority queue
            heapq.heappush(priority_queue, (sorted_parts[part_idx][element_idx], part_idx, element_idx))

    return sorted_result


def hpc_sort(sort_algorithm, numbers=[]):
    # set the timer to get total elapsed time
    start_total = time.time()

    # set global parameters
    global_data_size = len(numbers)
    global_data = numbers

    # start MPI environment
    comm = MPI.COMM_WORLD

    # get rank and size
    rank = comm.Get_rank()
    size = comm.Get_size()

    # divide the data in local lists using scatter
    local_data = []
    if rank == 0:
        # calculate local_data_size and remainder
        local_data_size = global_data_size // size
        remainder = global_data_size % size

        local_data = []

        # divide the global array into balanced local parts
        start_index = 0
        for i in range(size):
            end_index = start_index + local_data_size
            if i < remainder:
                end_index += 1
            local_part = global_data[start_index:end_index]
            local_data.append(local_part)
            start_index = end_index

    # scatter the local data to all processes
    local_data = comm.scatter(local_data, root=0)

    # start local sort clock
    start_local_sort = time.time()

    # do local sorting
    local_sorted = sort_algorithm(local_data)[0]

    # gather all locally sorted lists in the main branch
    sorted_parts = comm.gather(local_sorted, root=0)

    # finish local sort clock
    end_local_sort = time.time()

    ellapsed_local_sort_time = end_local_sort - start_local_sort

    print('Tempo decorrido na thread ' + str(rank) + ':', ellapsed_local_sort_time)

    # in the main branch, merge the results within each local_sorted array
    if rank == 0:
        # start the clock for the merging results part
        start_merge_results = time.time()

        # call the function that does the merging 
        result = merge_local_results(sorted_parts=sorted_parts)

        # stop the total and merge results clocks
        end_merge_results = time.time()
        end_total = time.time()

        ellapsed_time = end_total - start_total
        print("\nTempo total decorrido com threads:", ellapsed_time)
        print("\nTempo de mesclagem paralela:", end_merge_results - start_merge_results)

        return result, ellapsed_time

    # for each branch, return the locally sorted data and the ellapsed time within it.
    return local_sorted, ellapsed_local_sort_time
