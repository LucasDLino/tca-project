import sys
root_path = 'C:\\Users\\chris\\OneDrive\\Área de Trabalho\\Mestrado\\Período 1\\Técnicas Computacionais Avançadas\\Tca\\tca-project'
sys.path.insert(0, root_path)

from tests import sort_tests
from utility.sort.sort_type import SortType


def main():
    # ----------- UNCOMMENT THE TESTS YOU WANT TO RUN -----------

    # Tests for Quicksort
    # sort_tests.all_data_type_tests(SortType.QUICKSORT)
    # sort_tests.all_sizes_tests(SortType.QUICKSORT)
    # sort_tests.single_test(SortType.QUICKSORT, 100000, sort_tests.dataType.RANDOM_REVERSED_ORDERED, generate_chart=True, generate_file=True,
    #                        write_numbers_list=False, check_is_sorted=True)

    # Tests for Insertion Sort
    # sort_tests.all_data_type_tests(SortType.INSERTION)
    # sort_tests.all_sizes_tests(SortType.INSERTION)

    # Tests for Selection Sort
    # sort_tests.all_data_type_tests(SortType.SELECTION)
    # sort_tests.all_sizes_tests(SortType.SELECTION)

    # Tests for MergeSort
    # sort_tests.all_data_type_tests(SortType.MERGESORT)
    #  sort_tests.all_sizes_tests(SortType.MERGESORT)


    for value in [10000]:

        sort_tests.single_test(SortType.MERGESORT, value, sort_tests.dataType.RANDOM, generate_chart=False, generate_file=True,
                            write_numbers_list=False, check_is_sorted=True, is_multithreading=True)
        
        # sort_tests.single_test(SortType.MERGESORT, value, sort_tests.dataType.RANDOM, generate_chart=False, generate_file=True,
        #                     write_numbers_list=False, check_is_sorted=True, is_multithreading=True)
        
        print('=======================================')    


if __name__ == '__main__':
    main()
