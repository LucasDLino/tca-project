from utilities.data_generator.random_floats import generate_numbers
from utilities.sort.quicksort import quicksort
from charts.scatter_chart import *
from utilities.writer.sort_results_writer_txt import *


def run_selection(n, data_type=0, generate_chart=False, generate_file=False, test_name=""):
    return


def run_mergesort(n, data_type=0, generate_chart=False, generate_file=False, test_name=""):
    return


def run_quicksort(n, data_type=0, generate_chart=False, generate_file=False, test_name="", file=None, figure=None, axis=None, running_all=False):
    # Date of generation
    generate_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create file to write results if not running all tests
    if generate_file and running_all is False:
        file = create_file(n, data_type)

    # Write title
    write_title(file, test_name, n, data_type, generate_at)

    # Generate list of 10 random float between (-1000000, 1000000)
    numbers = generate_numbers(n, data_type)

    # Write repeated numbers
    write_repeated = True if data_type == 1 else False

    # Write numbers to file
    write_numbers(file, numbers, write_repeated)

    # Use quicksort algorithm to sort list of numbers
    ordered_numbers, elapsed_time = quicksort(numbers)

    # Write results to file
    write_results(file, elapsed_time)

    # Generate scatter chart if not running all tests
    if generate_chart and running_all is False:
        figure, axis = create_scatter_chart()

    # Add data to scatter chart
    if generate_chart:
        add_data_to_scatter_chart(n, elapsed_time, data_type, figure, axis)

    # Show scatter chart if not running all tests
    if generate_chart and running_all is False:
        show_scatter_chart()

    # Close file if not running all tests
    if generate_file and running_all is False:
        file.close()

    return ordered_numbers, elapsed_time


def run_all_quicksort_data_types(n, generate_chart=False, generate_file=False):
    # List of pair (ordered_numbers, elapsed_time)
    results = []

    # Create file to write results
    file = None
    if generate_file:
        file = create_file(n, "all")

    # Create figure to generate chart
    figure = None
    axis = None
    if generate_chart:
        figure, axis = create_scatter_chart()

    # Loop through data types (0 = Random, 1 = Random with repeated, 2 = Ascending, 3 = Descending)
    for data_type in range(0, 4):
        # Run quicksort algorithm for each data type
        ordered_number, elapsed_time = run_quicksort(n, data_type, generate_chart, generate_file,
                                                     "TEST " + str(data_type) + " - Quicksort", file, figure, axis, True)

        # Add pair (ordered_numbers, elapsed_time) to results
        results.append((ordered_number, elapsed_time))

    if generate_chart:
        show_scatter_chart()

    # Close file
    if generate_file:
        file.close()

    return results


def run_all_quicksort_quantity(data_type, generate_chart=False, generate_file=False):
    # List of pair (ordered_numbers, elapsed_time)
    results = []

    # Create file to write results
    file = None
    if generate_file:
        file = create_file("all", data_type)

    # Create figure to generate chart
    figure = None
    axis = None
    if generate_chart:
        figure, axis = create_scatter_chart()

    # List of quantity of numbers
    n = [100, 1000, 10000, 100000, 1000000]

    # Loop through quantity of numbers
    for quantity in n:
        # Run quicksort algorithm for each quantity of numbers
        ordered_number, elapsed_time = run_quicksort(quantity, data_type, generate_chart, generate_file,
                                                     "TEST " + str(quantity) + " - Quicksort", file, figure, axis, True)

        # Add pair (ordered_numbers, elapsed_time) to results
        results.append((ordered_number, elapsed_time))

    if generate_chart:
        # Corrections chart
        title = "Quicksort - " + get_type_name(data_type) + " - All quantity of numbers"
        set_title_to_scatter_chart(axis, title)

        not_show_legend_to_scatter_chart(axis)

        set_ticks_scientific_limits_to_scatter_chart(axis, 3)

        # Show scatter chart
        show_scatter_chart()

    # Close file
    if generate_file:
        file.close()

    return results


def run_insertion(n, data_type=0, generate_chart=False, generate_file=False, test_name=""):
    return


def run_all(n, data_type=0, generate_chart=False, generate_file=False, test_name=""):
    return
