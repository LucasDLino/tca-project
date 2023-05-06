from engine import sort_engine
from utility.sort.sort_type import SortType
from utility.data_generator.random_floats_type import RandomFloatsType as dataType


def main():
    # TESTS - Run quicksort for 100000 numbers - All data types
    sort_engine.run_all_data_types(SortType.QUICKSORT, 100000, generate_chart=True, generate_file=True, write_numbers_list=False)

    # TESTS - Run quicksort for all quantity of numbers - Random data type
    sort_engine.run_all_sizes(SortType.QUICKSORT, data_type=dataType.RANDOM, generate_chart=True, generate_file=False, write_numbers_list=False)

    # TEST 1 - Run quicksort for 1000 numbers - Random data type
    sort_engine.run_sort_algorithm(SortType.QUICKSORT, 1000, data_type=dataType.RANDOM, generate_chart=True, generate_file=False,
                                   test_name="TEST 1 - Quicksort")

    # TESTS - Run selection for all quantity of numbers - Random data type
    sort_engine.run_all_sizes(SortType.SELECTION, data_type=dataType.RANDOM, generate_chart=True, generate_file=True, write_numbers_list=False)


if __name__ == '__main__':
    main()
