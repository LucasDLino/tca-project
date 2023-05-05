# Enum with the type of charts to generate
class ChartType:
    SCATTER = 0
    BAR = 1


def get_chart_type_name(chart_type):
    if chart_type == ChartType.SCATTER:
        return "Scatter"
    elif chart_type == ChartType.BAR:
        return "Bar"
    else:
        return "Scatter"
