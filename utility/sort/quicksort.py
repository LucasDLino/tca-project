import time


def quicksort(numbers):
    # Insert timer to check time of sort algorithm
    start_time = time.time()

    # TODO: Remove - Print start time
    print("start_time: ", start_time)

    try:
        quicksort_implementation(numbers, 0, len(numbers) - 1)
    except RecursionError:
        # Raise alert
        print("RecursionError: maximum recursion depth exceeded while calling a Python object", "\n")

        # TODO: Possible solutions: 1 - Allow deeper recursion; 2 - Choose middle or even random pivot point;

        return [], 0

        # End timer
    end_time = time.time()

    # TODO: Remove - Print end time
    print("end_time: ", end_time)

    # Compute elapsed time
    elapsed_time = end_time - start_time

    # TODO: Remove - Print elapsed time
    print("elapsed_time: ", elapsed_time, "\n")

    return numbers, elapsed_time


def quicksort_implementation(numbers, low, high, middle_pivot=False):
    if high <= low:
        return

    if middle_pivot:
        # Middle pivot
        numbers[low], numbers[(low + high) // 2] = numbers[(low + high) // 2], numbers[low]

    v = numbers[low]  # pivot value

    i = low  # left pointer
    j = high + 1  # right pointer

    while True:
        # Find item on left to swap
        i += 1
        # To treat repeated numbers, we check if the number is equal to the pivot and if the index is less than the right pointer
        while i < high and (numbers[i] < v or (numbers[i] == v and i < j)):
            i += 1

        # Find item on right to swap
        j -= 1
        # To treat repeated numbers, we check if the number is equal to the pivot and if the index is greater than the left pointer
        while j > low and (numbers[j] > v or (numbers[j] == v and j > i)):
            j -= 1

        # Check if pointers cross
        if i >= j:
            break

        # Swap items
        numbers[i], numbers[j] = numbers[j], numbers[i]

    # Swap with partitioning item
    numbers[low], numbers[j] = numbers[j], numbers[low]

    # Sort left partition
    quicksort_implementation(numbers, low, j - 1)

    # Sort right partition
    quicksort_implementation(numbers, j + 1, high)
