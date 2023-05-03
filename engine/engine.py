from utilities.data_generator.random_floats import generate_random_floats
from utilities.sort.quicksort import quicksort
from graph.scatter_chart import create_scatter_chart, add_data_to_scatter_chart, show_scatter_chart


def run_quicksort(n):
    # Generate list of 10 random float between (-inf, inf)
    numbers = generate_random_floats(n)

    # Use quicksort algorithm to sort list of numbers
    elapsed_time = quicksort(numbers)

    # Create empty figure
    fig, ax = create_scatter_chart()

    # Add data to figure
    add_data_to_scatter_chart(n, elapsed_time, fig, ax)

    # Show figure
    show_scatter_chart()


def run_bubblesort(n):
    return


def run_mergesort(n):
    return


# TODO: Add more algorithms


def run_all(n):
    return
