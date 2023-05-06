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
    return
