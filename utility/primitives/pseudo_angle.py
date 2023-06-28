import sys


def get_pseudo_angle(x, y):
    # Compute pseudo angle with the least operations possible

    # Compute pseudo angle
    pseudo_angle = compute_pseudo_angle(x, y)

    # Print pseudo angle
    print("Pseudo angle: ", pseudo_angle)


def compute_pseudo_angle(x, y):
    # Compute pseudo angle with the least operations possible between two vectors

    """Idea: Define pseudo-angle as a measure along the square of vertices (+1, +1), (-1, 1),
    (-1, -1), and (+1, -1), which characterizes a function defined for any non-zero vector x ∈ R2
    and takes values in the interval (-4, +4]."""

    if x > 0:  # First comparison
        if y > 0:  # Second comparison
            if x > y:  # Third comparison
                pseudo_angle = y / x  # 0 < ps_an < 1
            else:
                pseudo_angle = 2 - x / y  # 1 < ps_an < 2
        else:
            if x > -y:  # Third comparison
                pseudo_angle = 8 + y / x  # 7 < ps_an < 8
            else:
                pseudo_angle = 6 - x / y  # 6 < ps_an < 7
    else:
        if y > 0:  # Second comparison
            if -x > y:  # Third comparison
                pseudo_angle = 4 + y / x  # 3 < ps_an < 4
            else:
                pseudo_angle = 2 - x / y  # 2 < ps_an < 3
        else:  # Second comparison
            if -x > -y:  # Third comparison
                pseudo_angle = 4 + y / x  # 4 < ps_an < 5
            else:
                pseudo_angle = 6 - x / y  # 5 < ps_an < 6

    return pseudo_angle

def compute_pseudo_angle_with_vector(vector):
    print(vector)
    return compute_pseudo_angle(vector[0], vector[1])

# if __name__ == '__main__':
#     # Get x and y values from command line arguments
#     x_coord = float(sys.argv[1])
#     y_coord = float(sys.argv[2])

#     get_pseudo_angle(x_coord, y_coord)
