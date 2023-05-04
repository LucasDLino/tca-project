from engine import sort_engine


def main():
    # TESTS - Run quick sort for 1000 numbers - All data types
    sort_engine.run_all_quicksort_data_types(1000, generate_chart=True, generate_file=False)

    # TESTS - Run quick sort for all quantity of numbers - Random data type
    sort_engine.run_all_quicksort_quantity(1, generate_chart=True, generate_file=False)

    # TEST 1 - Run quick sort for 1000 numbers - Random data type
    # sort_engine.run_quicksort(1000, 0, True, False, "TEST 1 - Quicksort")


if __name__ == '__main__':
    main()
