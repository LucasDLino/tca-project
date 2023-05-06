import os
from datetime import datetime
from ..data_generator.random_floats_type import get_random_float_type_name
from collections import Counter


def create_file(n, data_type):
    # Date
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create file name
    file_name = "numbers=" + str(n) + "_data_type=" + str(data_type) + "_date=" + date + ".txt"

    # Create backup folder if it doesn't exist
    if not os.path.exists("backup"):
        os.makedirs("backup")

    # Create file in backup folder, and if it doesn't exist, create it
    file = open(os.path.join("backup", file_name), "w+")

    return file


def write_title(file, test_name, n, data_type, date):
    if file is not None:
        file.write(
            "### --- " + test_name + " --- " + str(n) + " numbers - Data Type: " + get_random_float_type_name(data_type)
            + " - Generated at: " + date + " --- ###\n\n")


def write_numbers(file, numbers, write_numbers_list=False, write_repeated=False):
    if file is not None:

        # List of repeated numbers
        repeated = []
        if write_repeated:
            # Count the occurrences of each number
            counts = Counter(numbers)

            # Write repeated numbers to file
            repeated = [num for num, count in counts.items() if count > 1]

        if write_numbers_list:
            # Write numbers to file
            file.write("Numbers: " + str(numbers) + "\n\n")

            if write_repeated:
                file.write("Repeated numbers: " + str(repeated) + "\n\n")
        else:
            # Write just the quantity of numbers
            file.write("Numbers: List of numbers has been omitted. It contains " + str(len(numbers)) + " numbers.\n\n")

            if write_repeated:
                file.write("Repeated numbers: List of repeated numbers has been omitted. It contains " + str(len(repeated)) + " numbers.\n\n")


def write_is_sorted(file, is_sorted):
    if file is not None:
        file.write("Algorithm successfully sorted the list of numbers.\n\n" if is_sorted else "Algorithm failed to sort the list of numbers.\n\n")


def write_results(file, elapsed_time, ordered_numbers, write_numbers_list=False):
    if file is not None:
        if write_numbers_list:
            file.write("Ordered numbers: " + str(ordered_numbers) + "\n\n\n")

        file.write("Execution time: " + str(elapsed_time) + " seconds\n\n\n")
