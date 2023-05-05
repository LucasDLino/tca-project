import matplotlib.pyplot as plt
from utility.data_generator.random_floats_type import get_type_name


def create_scatter_chart():
    # Create empty figure
    fig, ax = plt.subplots()

    return fig, ax


def add_data_to_scatter_chart(n, elapsed_time, data_type):
    # Get current figure and axis
    fig, ax = plt.gcf(), plt.gca()

    # Add data to figure
    ax.plot(n, elapsed_time, 'o', markersize=4, label=get_type_name(data_type))

    # Add title and axis names
    ax.set_title('Quicksort Algorithm - n = ' + str(n) + ' numbers')

    ax.set_xlabel('Quantity of Numbers')
    ax.set_ylabel('Time (seconds)')

    ax.legend()

    return fig


def set_title_to_scatter_chart(title):
    # Get current axis
    ax = plt.gca()

    # Set title
    ax.set_title(title)
    return


def not_show_legend_to_scatter_chart():
    # Get current axis
    ax = plt.gca()

    # Remove legend
    ax.legend().remove()
    return


def set_ticks_scientific_limits_to_scatter_chart(limit):
    # Get current axis
    ax = plt.gca()

    # Set ticks scientific limits
    ax.ticklabel_format(style='sci', axis='x', scilimits=(limit, limit))
    return


def show_scatter_chart():
    # Show figure
    plt.show()

    return


def generate_scatter_chart(n, data_type, elapsed_time):
    # Create empty figure
    create_scatter_chart()

    # Add data to figure
    add_data_to_scatter_chart(n, elapsed_time, data_type)

    # Show figure
    show_scatter_chart()

    return
