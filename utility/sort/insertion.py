import time


def insertion(numbers):
    # Insert timer to check time of sort algorithm
    start_time = time.time()

    # TODO: Remove - Print start time
    print("start_time: ", start_time)

    insertion_implementation(numbers)

    # End timer
    end_time = time.time()

    # TODO: Remove - Print end time
    print("end_time: ", end_time)

    # Compute elapsed time
    elapsed_time = end_time - start_time

    # TODO: Remove - Print elapsed time
    print("elapsed_time: ", elapsed_time, "\n")

    return numbers, elapsed_time


def insertion_implementation(numbers):
    # Length of numbers list
    length = len(numbers)

    # Put -inf in the first position of numbers list
    numbers.insert(0, float("-inf"))

    # Iterate through numbers list
    for i in range(1, length + 1):
        v = numbers[i]
        j = i

        while j > 0 and numbers[j - 1] > v:
            numbers[j] = numbers[j - 1]
            j = j - 1

        numbers[j] = v

    # Remove -inf from numbers list
    numbers.pop(0)
