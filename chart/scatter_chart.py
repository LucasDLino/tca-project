import matplotlib.pyplot as plt
from utility.data_generator.random_floats_type import get_random_float_type_name
import random


def create_scatter_chart():
    # Create empty figure
    fig, ax = plt.subplots()

    return fig, ax


def add_data_to_scatter_chart(n, elapsed_time, data_type, sort_name):
    # Get current figure and axis
    fig, ax = plt.gcf(), plt.gca()

    markers = ["o", "v", "^", "<", ">", "s", "p", "*", "h", "H", "D"]

    # Add data to figure
    ax.plot(n, elapsed_time, marker=random.choice(markers), markersize=7, label=get_random_float_type_name(data_type))

    # Show text for this point
    ax.annotate(f"t = {elapsed_time:.3f}s", (n, elapsed_time), xytext=(n, elapsed_time), textcoords='data', ha='left', va='bottom', fontsize=8)

    # Scale x axis to log
    ax.set_xscale('log')

    # Add title and axis names
    ax.set_title(sort_name + ' Algorithm - n = ' + str(n) + ' numbers')

    ax.set_xlabel('Quantity of Numbers')
    ax.set_ylabel('Time (seconds)')

    ax.legend()

    return fig


def add_line_to_scatter_chart():
    # Get current figure and axis
    fig, ax = plt.gcf(), plt.gca()

    # Get all plotted lines in the current axis
    lines = ax.get_lines()

    # Get all x and y data points for the plotted lines
    x_data, y_data = [], []
    for line in lines:
        x_data.extend(line.get_xdata())
        y_data.extend(line.get_ydata())

    # Add a line connecting all data points
    ax.plot(x_data, y_data, linestyle='--', color='gray')

    # Show the plot
    plt.show()


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


def generate_scatter_chart(n, data_type, elapsed_time, sort_name):
    # Create empty figure
    create_scatter_chart()

    # Add data to figure
    add_data_to_scatter_chart(n, elapsed_time, data_type, sort_name)

    # Show figure
    show_scatter_chart()

    return
