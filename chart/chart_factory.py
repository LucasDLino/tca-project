import os
from datetime import datetime
from chart.chart_type import *
from chart.scatter_chart import *
from chart.bar_chart import *


def create_chart():
    # Create empty figure
    fig, ax = plt.subplots()

    return fig, ax


def add_data_to_chart(chart_type, n, elapsed_time, data_type, sort_name):
    if chart_type == ChartType.SCATTER:
        return add_data_to_scatter_chart(n, elapsed_time, data_type, sort_name)
    elif chart_type == ChartType.BAR:
        return add_data_to_bar_chart(n, elapsed_time, data_type, sort_name)
    else:
        return add_data_to_scatter_chart(n, elapsed_time, data_type, sort_name)


def save_chart(chart_type_name, n, data_type_name, sort_name):
    # Date
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Folder to save the plot
    figs_folder = sort_name + "-figs"

    # Create folder to sort if not exists
    if not os.path.exists(figs_folder):
        os.makedirs(figs_folder)

    # save the plot as SVG
    plt.savefig(f'{figs_folder}/chart={chart_type_name}_n={n}_data_type={data_type_name}_sort={sort_name}_date={date}.svg', format='svg', dpi=1200)


def show_chart():
    plt.show()
