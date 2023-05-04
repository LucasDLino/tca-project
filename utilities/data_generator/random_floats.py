import random
from ..data_generator.random_floats_type import RandomFloatsType


def generate_random_floats(n):
    numbers = [random.uniform(-1000000, 1000000) for _ in range(n)]

    return numbers


def generate_random_with_repeated_floats(n):
    random_numbers = [random.uniform(-1000000, 1000000) for _ in range(n)]

    numbers = []

    for i in range(n):
        numbers.append(random.choice(random_numbers))

    return numbers


def generate_random_ordered_floats(n):
    numbers = [random.uniform(-1000000, 1000000) for _ in range(n)]

    numbers.sort()

    return numbers


def generate_random_reversed_ordered_floats(n):
    numbers = [random.uniform(-1000000, 1000000) for _ in range(n)]

    numbers.sort(reverse=True)

    return numbers


def generate_numbers(n, data_type):
    if data_type == RandomFloatsType.RANDOM:
        return generate_random_floats(n)
    elif data_type == RandomFloatsType.RANDOM_WITH_REPEATED:
        return generate_random_with_repeated_floats(n)
    elif data_type == RandomFloatsType.RANDOM_ORDERED:
        return generate_random_ordered_floats(n)
    elif data_type == RandomFloatsType.RANDOM_REVERSED_ORDERED:
        return generate_random_reversed_ordered_floats(n)
    else:
        return generate_random_floats(n)
