import time


def selection(numbers):
    # Insert timer to check time of sort algorithm
    start_time = time.time()

    # TODO: Remove - Print start time
    print("start_time: ", start_time)

    selection_implementation(numbers)

    # End timer
    end_time = time.time()

    # TODO: Remove - Print end time
    print("end_time: ", end_time)

    # Compute elapsed time
    elapsed_time = end_time - start_time

    # TODO: Remove - Print elapsed time
    print("elapsed_time: ", elapsed_time, "\n")

    return numbers, elapsed_time


def selection_implementation(numbers):

    list_length = len(numbers)
    for i in range(0, list_length-1):
        m = i
        for j in range(i+1, list_length):
            if numbers[j] < numbers[m]:
                m = j
        numbers[i], numbers[m] = numbers[m], numbers[i]

    return numbers
