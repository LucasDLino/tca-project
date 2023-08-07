import time
import math


def mergesort(numbers):
    # Insert timer to check time of sort algorithm
    start_time = time.time()

    # TODO: Remove - Print start time
    print("start_time: ", start_time)

    mergesort_implementation(numbers)

    # End timer
    end_time = time.time()

    # TODO: Remove - Print end time
    print("end_time: ", end_time)

    # Compute elapsed time
    elapsed_time = end_time - start_time

    # TODO: Remove - Print elapsed time
    print("elapsed_time: ", elapsed_time, "\n")

    return numbers, elapsed_time


def mergesort_implementation(numbers):

    data_size = len(numbers)

    if data_size < 2:
        return numbers

    branch_base_size = math.floor(data_size/2)
    left_branch = numbers[:branch_base_size]
    right_branch = numbers[branch_base_size:]

    mergesort_implementation(left_branch)
    mergesort_implementation(right_branch)

    left_marker = 0
    right_marker = 0

    sentinel = float("inf")

    left_branch.append(sentinel)
    right_branch.append(sentinel)

    for index in range(0, data_size):
        if (left_branch[left_marker] < right_branch[right_marker]):
            numbers[index] = left_branch[left_marker]
            left_marker += 1
        else:
            numbers[index] = right_branch[right_marker]
            right_marker += 1

    return numbers
