import matplotlib.pyplot as plt
from utility.data_generator.random_floats_type import get_random_float_type_name


def create_bar_chart():
    # Create empty figure
    fig, ax = plt.subplots()

    return fig, ax


def add_data_to_bar_chart(n, elapsed_time, data_type):
    # Get current figure and axis
    fig, ax = plt.gcf(), plt.gca()

    # Add data to figure
    ax.bar(data_type, elapsed_time, width=0.8, label=get_random_float_type_name(data_type))

    # Annotate above the bar
    ax.annotate(f"t = {elapsed_time:.3f}s", (data_type, elapsed_time), xytext=(data_type, elapsed_time), textcoords='data',
                ha='center', va='bottom', fontsize=8)

    # Add title and axis names
    ax.set_title('Quicksort Algorithm - n = ' + str(n) + ' numbers')

    ax.set_xlabel('Type of Numbers')
    ax.set_ylabel('Time (seconds)')

    # Set x-axis ticks invisible
    ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

    # Add legend
    ax.legend(fontsize=8)

    return


def set_title_to_bar_chart(title):
    # Get current axis
    ax = plt.gca()

    # Set title
    ax.set_title(title)
    return


def not_show_legend_to_bar_chart():
    # Get current axis
    ax = plt.gca()

    # Remove legend
    ax.legend().remove()
    return


def show_bar_chart():
    # Show figure
    plt.show()

    return


def generate_bar_chart(n, data_type, elapsed_time):
    # Create figure
    create_bar_chart()

    # Add data to figure
    add_data_to_bar_chart(n, elapsed_time, data_type)

    # Show figure
    show_bar_chart()

    return
