# Enum to select the type of random floats to generate
class RandomFloatsType:
    RANDOM = 0
    RANDOM_WITH_REPEATED = 1
    RANDOM_ORDERED = 2
    RANDOM_REVERSED_ORDERED = 3


def get_type_name(data_type):
    if data_type == RandomFloatsType.RANDOM:
        return "Random"
    elif data_type == RandomFloatsType.RANDOM_WITH_REPEATED:
        return "Random with repeated"
    elif data_type == RandomFloatsType.RANDOM_ORDERED:
        return "Random ordered"
    elif data_type == RandomFloatsType.RANDOM_REVERSED_ORDERED:
        return "Random reversed ordered"
    else:
        return "Random"
