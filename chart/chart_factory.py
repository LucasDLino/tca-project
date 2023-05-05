from chart.chart_type import ChartType
from chart.scatter_chart import *
from chart.bar_chart import *


def create_chart():
    # Create empty figure
    fig, ax = plt.subplots()

    return fig, ax


def add_data_to_chart(chart_type, n, elapsed_time, data_type):
    if chart_type == ChartType.SCATTER:
        return add_data_to_scatter_chart(n, elapsed_time, data_type)
    elif chart_type == ChartType.BAR:
        return add_data_to_bar_chart(n, elapsed_time, data_type)
    else:
        return add_data_to_scatter_chart(n, elapsed_time, data_type)


def show_chart():
    plt.show()
