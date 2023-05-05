from utility.data_generator.random_floats import generate_numbers
from utility.sort.quicksort import quicksort
from utility.writer.sort_results_writer_txt import *
from chart.chart_factory import *


def run_selection(n, data_type=0, generate_chart=False, generate_file=False, test_name="", chart_type=0,
                  file=None, running_all=False, write_numbers_list=False):
    return


def run_mergesort(n, data_type=0, generate_chart=False, generate_file=False, test_name="", chart_type=0,
                  file=None, running_all=False, write_numbers_list=False):
    return


def run_quicksort(n, data_type=0, generate_chart=False, generate_file=False, test_name="", chart_type=0,
                  file=None, running_all=False, write_numbers_list=False):
    # TODO: Remove - Print test
    print("Running quicksort for data type: " + get_type_name(data_type) + " - n = " + str(n) + " numbers")

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
    if write_numbers_list:
        write_numbers(file, numbers, write_repeated)

    # Use quicksort algorithm to sort list of numbers
    ordered_numbers, elapsed_time = quicksort(numbers)

    # Write results to file
    write_results(file, elapsed_time, ordered_numbers, write_numbers_list)

    # Generate chart if not running all tests
    if generate_chart and running_all is False:
        create_chart()

    # Add data to chart
    if generate_chart:
        add_data_to_chart(chart_type, n, elapsed_time, data_type)

    # Show chart if not running all tests
    if generate_chart and running_all is False:
        show_chart()

    # Close file if not running all tests
    if generate_file and running_all is False:
        file.close()

    return ordered_numbers, elapsed_time


def run_quicksort_all_data_types(n, generate_chart=False, generate_file=False, write_numbers_list=False):
    # List of pair (ordered_numbers, elapsed_time)
    results = []

    # Create file to write results
    file = None
    if generate_file:
        file = create_file(n, "all")

    # Create figure to generate chart
    if generate_chart:
        create_bar_chart()

    # Loop through data types (0 = Random, 1 = Random with repeated, 2 = Ascending, 3 = Descending)
    for data_type in range(0, 4):
        # Run quicksort algorithm for each data type
        ordered_number, elapsed_time = run_quicksort(n, data_type, generate_chart, generate_file, "TEST " + str(data_type) + " - Quicksort",
                                                     ChartType.BAR, file, True, write_numbers_list)

        # Add pair (ordered_numbers, elapsed_time) to results
        results.append((ordered_number, elapsed_time))

    if generate_chart:
        show_bar_chart()

    # Close file
    if generate_file:
        file.close()

    return results


def run_quicksort_all_quantity(data_type, generate_chart=False, generate_file=False, write_numbers_list=False):
    # List of pair (ordered_numbers, elapsed_time)
    results = []

    # Create file to write results
    file = None
    if generate_file:
        file = create_file("all", data_type)

    # Create figure to generate chart
    if generate_chart:
        create_scatter_chart()

    # List of quantity of numbers
    n = [100, 1000, 10000, 100000, 1000000]

    # Loop through quantity of numbers
    for i, quantity in enumerate(n):
        # Run quicksort algorithm for each quantity of numbers
        ordered_number, elapsed_time = run_quicksort(quantity, data_type, generate_chart, generate_file, "TEST " + str(i) + " - Quicksort",
                                                     ChartType.SCATTER, file, True, write_numbers_list)

        # Add pair (ordered_numbers, elapsed_time) to results
        results.append((ordered_number, elapsed_time))

    if generate_chart:
        # Corrections chart
        title = "Quicksort - " + get_type_name(data_type) + " - All quantity of numbers"
        set_title_to_scatter_chart(title)

        not_show_legend_to_scatter_chart()

        # set_ticks_scientific_limits_to_scatter_chart(3)

        add_line_to_scatter_chart()

        # Show scatter chart
        show_scatter_chart()

    # Close file
    if generate_file:
        file.close()

    return results


def run_insertion(n, data_type=0, generate_chart=False, generate_file=False, test_name="", chart_type=0,
                  file=None, running_all=False, write_numbers_list=False):
    return


def run_all_sort(n, data_type=0, generate_chart=False, generate_file=False, test_name="", chart_type=0,
                 file=None, running_all=False, write_numbers_list=False):
    return
