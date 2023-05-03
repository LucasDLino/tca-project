import matplotlib.pyplot as plt


def create_scatter_chart():
    # Create empty figure
    fig, ax = plt.subplots()

    return fig, ax


def add_data_to_scatter_chart(n, elapsed_time, fig, ax):
    # Add data to figure
    ax.scatter(n, elapsed_time)

    # Add title and axis names
    ax.set_title('Quicksort Algorithm - n = ' + str(n) + ' numbers')

    ax.set_xlabel('Quantity of Numbers')
    ax.set_ylabel('Time (seconds)')
    return fig


def show_scatter_chart():
    # Show figure
    plt.show()

    return
