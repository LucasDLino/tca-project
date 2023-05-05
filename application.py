from engine import sort_engine


def main():
    # TESTS - Run quick sort for 1000 numbers - All data types
    sort_engine.run_quicksort_all_data_types(1000, generate_chart=True, generate_file=False, write_gen_numbers=True)

    # TESTS - Run quick sort for all quantity of numbers - Random data type
    sort_engine.run_quicksort_all_quantity(1, generate_chart=True, generate_file=False, write_gen_numbers=False)

    # TEST 1 - Run quick sort for 1000 numbers - Random data type
    # sort_engine.run_quicksort(1000, data_type=0, generate_chart=True, generate_file=False, test_name="TEST 1 - Quicksort")


if __name__ == '__main__':
    main()
