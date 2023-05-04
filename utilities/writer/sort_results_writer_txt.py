import os
from datetime import datetime
from ..data_generator.random_floats_type import get_type_name


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
            "### --- " + test_name + " --- " + str(n) + " numbers - Data Type: " + get_type_name(data_type)
            + " - Generated at: " + date + " --- ###\n\n")


def write_numbers(file, numbers, write_repeated=False):
    if file is not None:
        file.write("Numbers: " + str(numbers) + "\n\n")

        if write_repeated:
            file.write("Repeated numbers: " + str([item for item in numbers if numbers.count(item) > 1]) + "\n\n")


def write_results(file, elapsed_time):
    if file is not None:
        file.write("Execution time: " + str(elapsed_time) + " seconds\n\n\n")
