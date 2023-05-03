import time


def quicksort(numbers):
    # Insert timer to check time of sort algorithm
    start_time = time.time()

    # TODO: Implement quicksort algorithm

    # End timer
    end_time = time.time()

    # Compute elapsed time
    elapsed_time = end_time - start_time

    print(f"Execution time: {elapsed_time} seconds")
    return elapsed_time
