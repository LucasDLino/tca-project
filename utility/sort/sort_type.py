# Enum to select the type of sort algorithms
class SortType:
    SELECTION = 0
    MERGESORT = 1
    QUICKSORT = 2
    INSERTION = 3


def get_sort_type_name(sort_type):
    if sort_type == SortType.SELECTION:
        return "Selection"
    elif sort_type == SortType.MERGESORT:
        return "Mergesort"
    elif sort_type == SortType.QUICKSORT:
        return "Quicksort"
    elif sort_type == SortType.INSERTION:
        return "Insertion"
    else:
        return "Selection"
