import random


def generate_random_floats(n):
    numbers = [random.uniform(-1000000, 1000000) for _ in range(n)]

    print("numbers", numbers)

    return numbers
