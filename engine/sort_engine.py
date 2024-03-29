from utility.data_generator.random_floats import generate_numbers
from utility.sort.quicksort import quicksort
from utility.sort.selection import selection
from utility.sort.insertion import insertion
from utility.sort.mergesort import mergesort
from utility.writer.sort_results_writer_txt import *
from chart.chart_factory import *
from utility.sort.sort_type import *
from utility.hpc_sort.hpc_sort import hpc_sort


def is_sorted(numbers):
    if len(numbers) == 0:
        return False

    for i in range(0, len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False

    return True


def get_sort_algorithm(sort_type):
    if sort_type == SortType.SELECTION:
        return selection
    elif sort_type == SortType.MERGESORT:
        return mergesort
    elif sort_type == SortType.QUICKSORT:
        return quicksort
    elif sort_type == SortType.INSERTION:
        return insertion


def run_sort_algorithm(sort_type, n, data_type=0, generate_chart=False, generate_file=False, test_name="", chart_type=0,
                       file_data=None, running_all=False, write_numbers_list=False, check_is_sorted=False, is_multithreading=False):
    # Getting sort algorithm
    sort_algorithm = get_sort_algorithm(sort_type)

    # Sort algorithm name
    sort_name = get_sort_type_name(sort_type)

    # Data type name
    data_type_name = get_random_float_type_name(data_type)

    # TODO: Remove - Print test
    print("Running " + sort_name + " algorithm for data type: " +
          data_type_name + " - n = " + str(n) + " numbers")

    # Date of generation
    generate_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create file to write results if not running all tests
    if generate_file and running_all is False:
        file_data = create_file(n, data_type_name, sort_name)

    # Write title
    write_title(file_data, test_name, n, data_type, generate_at)

    # Generate list of 10 random float between (-1000000, 1000000)
    numbers = generate_numbers(n, data_type)

    # Write repeated numbers
    write_repeated = True if data_type == 1 else False

    # Write numbers to file
    write_numbers(file_data, numbers, write_numbers_list, write_repeated)

    # Use selected sort algorithm to sort list of numbers
    if (is_multithreading == False): 
        ordered_numbers, elapsed_time = sort_algorithm(numbers)
    else:
        ordered_numbers, elapsed_time = hpc_sort(sort_algorithm, numbers)

    # Check if list is sorted
    if check_is_sorted:
        check_sorted = is_sorted(ordered_numbers)
        # TODO: Remove - Print success or fail
        print(
            "Algorithm was successful!" if check_sorted else "Algorithm failed :(", "\n\n")

        write_is_sorted(file_data, check_sorted)

    # Write results to file
    write_results(file_data, elapsed_time, ordered_numbers, write_numbers_list)

    # Generate chart if not running all tests
    if generate_chart and running_all is False:
        create_chart()

    # Add data to chart
    if generate_chart:
        add_data_to_chart(chart_type, n, elapsed_time, data_type, sort_name)

    # Show chart if not running all tests
    if generate_chart and running_all is False:
        save_chart(get_chart_type_name(chart_type),
                   n, data_type_name, sort_name)
        show_chart()

    # Close file if not running all tests
    if generate_file and running_all is False:
        file_data.close()

    return ordered_numbers, elapsed_time


def run_all_data_types(sort_type, n, generate_chart=False, generate_file=False, write_numbers_list=False, check_is_sorted=False):
    # List of pair (ordered_numbers, elapsed_time)
    results = []

    # Name of sort algorithm
    sort_name = get_sort_type_name(sort_type)

    # Create file to write results
    file_data = None
    if generate_file:
        file_data = create_file(n, "all", sort_name)

    # Create figure to generate chart
    if generate_chart:
        create_bar_chart()

    # Loop through data types (0 = Random, 1 = Random with repeated, 2 = Ascending, 3 = Descending)
    for data_type in range(0, 4):
        # Run sort algorithm for each data type
        ordered_number, elapsed_time = run_sort_algorithm(sort_type, n, data_type, generate_chart, generate_file,
                                                          "TEST " +
                                                          str(data_type) +
                                                          " - " + sort_name,
                                                          ChartType.BAR, file_data, True, write_numbers_list, check_is_sorted)

        # Add pair (ordered_numbers, elapsed_time) to results
        results.append((ordered_number, elapsed_time))

    if generate_chart:
        save_chart(get_chart_type_name(ChartType.BAR), n, "all", sort_name)
        show_bar_chart()

    # Close file
    if generate_file:
        file_data.close()

    return results


def run_all_sizes(sort_type, data_type, generate_chart=False, generate_file=False, write_numbers_list=False, check_is_sorted=False):
    # List of pair (ordered_numbers, elapsed_time)
    results = []

    # Name of sort algorithm
    sort_name = get_sort_type_name(sort_type)

    # Data type name
    data_type_name = get_random_float_type_name(data_type)

    # Create file to write results
    file_data = None
    if generate_file:
        file_data = create_file("all", data_type_name, sort_name)

    # Create figure to generate chart
    if generate_chart:
        create_scatter_chart()

    # List of quantity of numbers
    n = [100, 1000, 10000, 100000, 1000000]

    # Loop through quantity of numbers
    for i, quantity in enumerate(n):
        # Run sort algorithm for each quantity of numbers
        ordered_number, elapsed_time = run_sort_algorithm(sort_type, quantity, data_type, generate_chart, generate_file,
                                                          "TEST " +
                                                          str(i) + " - " +
                                                          sort_name,
                                                          ChartType.SCATTER, file_data, True, write_numbers_list, check_is_sorted)

        # Add pair (ordered_numbers, elapsed_time) to results
        results.append((ordered_number, elapsed_time))

    if generate_chart:
        # Corrections chart
        title = sort_name + " - " + data_type_name + " - All quantity of numbers"
        set_title_to_scatter_chart(title)

        not_show_legend_to_scatter_chart()

        # set_ticks_scientific_limits_to_scatter_chart(3)

        add_line_to_scatter_chart()

        save_chart(get_chart_type_name(ChartType.SCATTER),
                   "all", data_type_name, sort_name)

        # Show scatter chart
        show_scatter_chart()

    # Close file
    if generate_file:
        file_data.close()

    return results


def run_all_algorithms(data_type, generate_chart=False, generate_file=False, write_numbers_list=False, check_is_sorted=False):
    return
