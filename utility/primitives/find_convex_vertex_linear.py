from vectorial_product import get_vector, compute_vectorial_product
from pseudo_angle import compute_pseudo_angle


def compute_baricentric_point(points):
    # Compute baricentric point of a list of points

    # Resulting baricentric point
    baricentric_point = [0, 0]

    # Iterate through vertices
    for vertex in points:
        # Add coordinates of vertex to baricentric point
        baricentric_point[0] += vertex[0]
        baricentric_point[1] += vertex[1]

    # Divide coordinates of baricentric point by number of vertices
    baricentric_point[0] /= len(points)
    baricentric_point[1] /= len(points)

    return baricentric_point


def find_convex_vertex(points, i):
    # Points is a list representing the set of points and i is the index of the point to be checked

    # Get number of points
    number_of_points = len(points)

    # Get baricentric point of points
    baricentric_point = compute_baricentric_point(points)

    # Get vector from baricentric point to point i
    vector = get_vector(points[i], baricentric_point)

    # Get pseudo angle of vector
    bar_pseudo_angle = compute_pseudo_angle(vector[0], vector[1])

    # Left most point by pseudo angle
    left_most_point = None
    left_most_point_pseudo_angle = float('inf')

    # Iterate through points to find left most point by pseudo angle
    for j in range(number_of_points):
        # Continue if point j is the same as point i
        if j == i:
            continue

        # Get vector from baricentric point to point j
        p_vector = get_vector(points[j], points[i])

        # Get pseudo angle of vector
        p_pseudo_angle = compute_pseudo_angle(p_vector[0], p_vector[1]) - bar_pseudo_angle

        if p_pseudo_angle < 0:
            p_pseudo_angle += 8

        # I want to ensure that the left most point has the pseudo angle closest to the baricentric point but is less than the pseudo angle of point i
        # If so, we have a new left most point, point j equals left most point
        # Check if the pseudo angle of point j is less than the pseudo angle of point i and closer to the baricentric point
        if p_pseudo_angle <= left_most_point_pseudo_angle:
            # Update left most point
            left_most_point = points[j]

            # Update left most point pseudo angle
            left_most_point_pseudo_angle = p_pseudo_angle

    # Check if we found a left most point
    if left_most_point is None:
        # Return None
        return False

    # With the left most point, we can get the vector from point i to the left most point
    left_vector = get_vector(points[i], left_most_point)

    # If needed, we check max coordinates of point of interest because some vectorial products are null
    list_zero_vectorial_product = []

    # Now loop through the points again to find if all points are on the same side (left) of the vector from point i to the left most point
    for j in range(number_of_points):
        # Continue if point j is the same as point i or the left most point
        if j == i:
            continue

        # Get vector from point i to point j
        i_j_vector = get_vector(points[i], points[j])

        # Get vectorial product of left_vector and i_j_vector
        vectorial_product = compute_vectorial_product(left_vector, i_j_vector)

        # If vectorial product is zero, then the points are collinear
        if vectorial_product == 0:
            # Add point to list of points with zero vectorial product
            list_zero_vectorial_product.append(points[j])

        # Check if vectorial product is negative
        if vectorial_product < 0:
            # Return false because we found a point on the right side of the vector from point i to the left most point
            return False

    # Finally, if there are collinear points, we need to check if this point of interest is a maximum or minimum local
    if len(list_zero_vectorial_product) > 0:
        x_max = max(list_zero_vectorial_product, key=lambda x: x[0])[0]
        x_min = min(list_zero_vectorial_product, key=lambda x: x[0])[0]

        y_max = max(list_zero_vectorial_product, key=lambda x: x[1])[1]
        y_min = min(list_zero_vectorial_product, key=lambda x: x[1])[1]

        # Check if point of interest is a maximum or minimum local
        if x_min < points[i][0] < x_max or y_min < points[i][1] < y_max:
            # Return false because we found a point on the right side of the vector from point i to the left most point
            return False

    # Return true because all points are on the left side of the vector from point i to the left most point
    return True


if __name__ == "__main__":
    # Other complex polygon
    other_polygon = [(1, 1), (2, 3), (4, 2), (3, 1), (5, 4), (6, 3), (7, 2), (6, 1), (4, 4), (2, 5)]

    # Loop through indexes to check
    for index in range(len(other_polygon)):
        # Find convex vertex
        convex_vertex = find_convex_vertex(other_polygon, index)

        # If True, we found a convex vertex
        if convex_vertex:
            print("Point: " + str(other_polygon[index]) + " is a convex vertex")
        # If False, we did not find a convex vertex
        else:
            print("Point: " + str(other_polygon[index]) + " is not a convex vertex")
