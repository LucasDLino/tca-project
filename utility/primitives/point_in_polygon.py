def compute_line_intersection(x0, y0, x1, y1):
    # Compute intersection of two lines

    # Handle the case when the lines are parallel to the y-axis
    if x1 - x0 == 0:
        return x0, y0

        # Compute intersection
    x_intersection = (x0 * y1 - y0 * x1) / (x1 - x0)
    y_intersection = y0  # Set y_intersection as y0 to ensure horizontal intersection

    return x_intersection, y_intersection


def get_point_in_polygon(vertices, point):
    # Get location of a point in a polygon

    x0, y0 = point
    n = len(vertices)

    intersect = 0  # Number of intersections

    for i in range(n):
        xi, yi = vertices[i]
        xi_next, yi_next = vertices[(i + 1) % n]

        if yi != yi_next:  # Side is not horizontal
            # Calculate the intersection of the line with the polygon side
            x_intersection, y_intersection = compute_line_intersection(x0 - xi, y0 - yi, xi_next - xi, yi_next - yi)

            # add tolerance
            if (min(xi, xi_next) <= x_intersection <= max(xi, xi_next)) and \
                    (min(yi, yi_next) <= y_intersection <= max(yi, yi_next)):
                # The point is on the boundary
                return "p is on the boundary: STOP."

            if x_intersection > x0 and y_intersection < max(yi, yi_next):  # Fix condition for checking below the point
                intersect += 1

        else:  # Side is horizontal
            if y0 == yi and min(xi, xi_next) <= x0 <= max(xi, xi_next):
                # The point is on the horizontal side
                return "p is on the boundary: STOP."

    if intersect % 2 == 1:
        return "p is inside P."
    else:
        return "p is outside P."


if __name__ == '__main__':
    polygon = [(0, 0), (0, 4), (4, 4), (4, 0)]  # Square polygon
    point_test = (3, 3)  # Point inside the square

    result = get_point_in_polygon(polygon, point_test)
    print("Square polygon: ", result)  # Prints "p is inside P."

    polygon = [(0, 0), (2, 3), (5, 2), (4, 6), (1, 4)]  # Complex polygon
    point_test = (3, 3)  # Point inside the polygon

    result = get_point_in_polygon(polygon, point_test)
    print("Complex polygon: ", result)  # Prints "p is inside P."
