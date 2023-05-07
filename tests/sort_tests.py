from engine import sort_engine
from utility.data_generator.random_floats_type import RandomFloatsType as dataType


def all_data_type_tests(sort_type):
    # TESTS - Run sort for 100 numbers - All data types
    sort_engine.run_all_data_types(sort_type, 100, generate_chart=True, generate_file=True,
                                   write_numbers_list=True, check_is_sorted=True)

    # TESTS - Run sort for 1000 numbers - All data types
    sort_engine.run_all_data_types(sort_type, 1000, generate_chart=True, generate_file=True,
                                   write_numbers_list=True, check_is_sorted=True)

    # TESTS - Run sort for 10000 numbers - All data types
    sort_engine.run_all_data_types(sort_type, 10000, generate_chart=True, generate_file=True,
                                   write_numbers_list=False, check_is_sorted=True)

    # TESTS - Run sort for 100000 numbers - All data types
    sort_engine.run_all_data_types(sort_type, 100000, generate_chart=True, generate_file=True,
                                   write_numbers_list=False, check_is_sorted=True)

    # TESTS - Run sort for 1000000 numbers - All data types
    sort_engine.run_all_data_types(sort_type, 1000000, generate_chart=True, generate_file=True,
                                   write_numbers_list=False, check_is_sorted=True)


def all_sizes_tests(sort_type):
    # TESTS - Run sort for all sizes of numbers list - Random numbers
    sort_engine.run_all_sizes(sort_type, data_type=dataType.RANDOM, generate_chart=True, generate_file=True,
                              write_numbers_list=False, check_is_sorted=True)

    # TESTS - Run sort for all sizes of numbers list - Random with repeated numbers
    sort_engine.run_all_sizes(sort_type, data_type=dataType.RANDOM_WITH_REPEATED, generate_chart=True, generate_file=True,
                              write_numbers_list=False, check_is_sorted=True)

    # TESTS - Run sort for all sizes of numbers list - Random ordered
    sort_engine.run_all_sizes(sort_type, data_type=dataType.RANDOM_ORDERED, generate_chart=True, generate_file=True,
                              write_numbers_list=False, check_is_sorted=True)

    # TESTS - Run sort for all sizes of numbers list - Random reversed ordered
    sort_engine.run_all_sizes(sort_type, data_type=dataType.RANDOM_REVERSED_ORDERED, generate_chart=True, generate_file=True,
                              write_numbers_list=False, check_is_sorted=True)


def single_test(sort_type, size, data_type, generate_chart=True, generate_file=False,
                write_numbers_list=False, check_is_sorted=False):
    # SINGLE TEST - for specific size and data type
    sort_engine.run_sort_algorithm(sort_type, size, data_type, generate_chart, generate_file, "TEST - n = " + str(size) +
                                   " - " + sort_engine.get_sort_type_name(sort_type), sort_engine.ChartType.BAR,
                                   None, False, write_numbers_list, check_is_sorted)
