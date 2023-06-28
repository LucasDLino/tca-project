from vectorial_product import compute_vectorial_product, get_vector
from pseudo_angle import compute_pseudo_angle


def check_is_vertex(points_list):
    pivot = points_list[0]

    for starting_position in range(1, len(points_list) - 1):

        point_a = points_list[starting_position]
        point_b = points_list[starting_position + 1]

        vector_a_b = get_vector(point_a, point_b)
        vector_b_pivot = get_vector(point_b, pivot)

        vectorial_product = compute_vectorial_product(vector_a_b, vector_b_pivot)

        if vectorial_product == 0 or vectorial_product < 0:
            return False
    return True


# get the 2d point with the minimum y coordinate within a 2d points list
def get_min_y(points_list):
    # returns None if there is no list
    if not points_list:
        return None

    # iterates over the list to find the desired point based on two rules hierarchical rules: lesser y and, if there is a tie, higher x
    return min(points_list, key=lambda point: (point[1], -point[0]))


# get the length of a 2d vector
def get_vector_length(vector):
    return (vector[0] ** 2 + vector[1] ** 2) ** (1 / 2)


# get the point that forms the lesser angle with the current edge, along with the accumulated angle.
def get_min_angle_point(actual_point, points_list, last_angle):
    # set a big value for comparison reasons
    min_pseudo_angle = 10 ** 6

    # declare the min_angle_point
    min_angle_point = None

    # declare the max_distance (used when the desired direction has collinear points)
    max_distance = None

    # iterate over all the points of the list
    for point in points_list:
        # if the current point is not the pivot, do:
        if point != actual_point:
            # get the vector going from the pivot to the current point
            vector = get_vector(actual_point, point)

            # get the pseudo angle between the current edge and the found vector
            pseudo_angle = compute_pseudo_angle(vector[0], vector[1]) - last_angle

            # adjust the pseudo angle value, if it its negative
            if pseudo_angle < 0:
                pseudo_angle += 8

            # if a lesser angle is found, set the current angle and point as the minimum values
            if pseudo_angle < min_pseudo_angle:
                min_pseudo_angle = pseudo_angle
                min_angle_point = point

            # if an equal angle as the lesser one is found
            elif pseudo_angle == min_pseudo_angle:
                # calculate the distance between the pivot and the current point
                distance = get_vector_length(get_vector(actual_point, point))
                if max_distance == None:
                    max_distance = get_vector_length(get_vector(actual_point, min_angle_point))

                # if the distance is greater than the max registered, set the current angle and point as the minimum values
                if distance > max_distance:
                    max_distance = distance
                    min_angle_point = point

    # return the min_angle_point and the accumulated pseudo angle.
    return min_angle_point, min_pseudo_angle + last_angle


def jarvis_2d_hull(points_list):
    # find the point with smallest y
    bottomest = get_min_y(points_list)

    # set the pivot point to the bottomest
    actual_point = bottomest

    # create the hull list with the first point of the hull (we are sure that the bottomest is one of them)
    hull = [actual_point]

    # declare next point variable
    next_point = None

    # set the angle accumulator to 0
    last_angle = 0

    # set a iteration counter and limit to it
    iteration_counter = 0
    iteration_limit = 10 ** 6

    # while the hull is not closed (and the iteration limit is not reached)
    while bottomest != next_point and iteration_counter != iteration_limit:
        # get the next point of the hull and the accumulated pseudo angle
        next_point, last_angle = get_min_angle_point(actual_point, points_list, last_angle)

        # append the next point to the hull
        hull.append(next_point)

        # set the pivot point as the next_point
        actual_point = next_point

        # add to the iteration counter
        iteration_counter += 1

    # return the hull
    return hull


print(jarvis_2d_hull([(1, 1), (2, 3), (4, 2), (3, 1), (5, 4), (6, 3), (7, 2), (6, 1), (4, 4), (2, 5)]))
