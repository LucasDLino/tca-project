import sys
venv_path = 'C:\\Users\\chris\\OneDrive\\Área de Trabalho\\Mestrado\\Período 1\\Técnicas Computacionais Avançadas\\Tca\\tca-project\\venv'
sys.path.insert(0, venv_path)

from mpi4py import MPI
from utility.data_generator.random_floats_type import *
from utility.data_generator.random_floats import generate_numbers
from utility.sort.mergesort import mergesort
import time

def custom_sort(arrays, key_func):
    if len(arrays) <= 1:
        return arrays
    
    mid = len(arrays) // 2
    left = custom_sort(arrays[:mid], key_func)
    right = custom_sort(arrays[mid:], key_func)
    
    return merge_arrays(left, right, key_func)

def merge_arrays(left, right, key_func):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        left_first = left[i][0] if len(left[i]) > 0 else float('inf')
        right_first = right[j][0] if len(right[j]) > 0 else float('inf')
        
        if key_func(left_first) < key_func(right_first):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":

    # get the list of numbers to be ordered
    global_data_size = 10000000
    global_data = generate_numbers(n=global_data_size, data_type=RandomFloatsType.RANDOM)

    start_regular = time.time()
    mergesort(global_data)
    end_regular = time.time()
    print("Tempo total normal:", end_regular - start_regular)

    # start MPI environment
    comm = MPI.COMM_WORLD

    # get rank and size
    rank = comm.Get_rank()
    size = comm.Get_size()

    # divide the data in local lists
    local_data_size = global_data_size // size
    local_data = global_data[rank * local_data_size: (rank + 1) * local_data_size]


    # set the timer to get total elapsed time
    start_total = time.time()

    # do local sorting
    start_branch = time.time()
    local_sorted = mergesort(local_data)
    end_branch = time.time()

    # merge the locally sorted branches
    start_merge = time.time()
    sorted_parts = comm.gather(local_sorted, root=0)
    end_merge = time.time()

    # Reunião eficiente dos dados ordenados
    if rank == 0:
        # Ordena os sorted_parts com base no primeiro valor de cada parte
        sorted_parts = custom_sort(sorted_parts, key_func=lambda part: part[0])

        # Flatten and extend the sorted parts to get the final result
        sorted_result = [item for part in sorted_parts for item in part]

        end_total = time.time()
        print("Resultado final:", sorted_result)
        print('-----')

        print("\nResultados das Branchs (Threads):")
        for i, part in enumerate(sorted_parts):
            print(f"Branch {i}: {part}")
            print('-----')

        print("\nTempo total decorrido:", end_total - start_total)
        # print("Tempo total normal:", end_regular - start_regular)
        print("Tempo total no branch (divisão):", end_branch - start_branch)
        print("Tempo de mesclagem dos dados locais:", end_merge - start_merge)
    else:
        comm.gather(local_sorted, root=0)

    end_total = time.time()


