import sys
import vectorial_product


def compute_barycentric_coords(vertices, point):
    # Compute barycentric coordinates of a point in a triangle

    # Get coordinates of the points
    p1 = vertices[0]  # P1
    p2 = vertices[1]  # P2
    p3 = vertices[2]  # P3
    p = point  # P

    # Area of triangle P-P2-P3
    s_1 = (vectorial_product.compute_vectorial_product(p, p2) +
           vectorial_product.compute_vectorial_product(p2, p3) +
           vectorial_product.compute_vectorial_product(p3, p))

    # Area of triangle P1-P-P3
    s_2 = (vectorial_product.compute_vectorial_product(p1, p) +
           vectorial_product.compute_vectorial_product(p, p3) +
           vectorial_product.compute_vectorial_product(p3, p1))

    # Area of triangle P-P1-P2
    s_3 = (vectorial_product.compute_vectorial_product(p, p1) +
           vectorial_product.compute_vectorial_product(p1, p2) +
           vectorial_product.compute_vectorial_product(p2, p))

    # Total area of triangle P1-P2-P3
    s = (vectorial_product.compute_vectorial_product(p1, p2) +
         vectorial_product.compute_vectorial_product(p2, p3) +
         vectorial_product.compute_vectorial_product(p3, p1))

    # Compute barycentric coordinates
    barycentric_coord_a = s_1 / s
    barycentric_coord_b = s_2 / s
    barycentric_coord_c = s_3 / s

    print("barycentric_coord_a: %.2f" % barycentric_coord_a)
    print("barycentric_coord_b: %.2f" % barycentric_coord_b)
    print("barycentric_coord_c: %.2f" % barycentric_coord_c, "\n")

    # Check sum of barycentric coordinates
    sum_barycentric_coords = barycentric_coord_a + barycentric_coord_b + barycentric_coord_c

    print("sum_barycentric_coords: %.2f" % sum_barycentric_coords, "\n")

    # Respect tolerance of 1e-6
    if abs(sum_barycentric_coords - 1) > 1e-6:
        print("Sum of barycentric coordinates is not 1, for this reason, we are exiting the program")
        sys.exit(1)

    return barycentric_coord_a, barycentric_coord_b, barycentric_coord_c


def get_location_of_point_in_triangle(vertices, point):
    # Get location of a point in a triangle

    # Get barycentric coordinates of the point
    a, b, c = compute_barycentric_coords(vertices, point)

    # Check all possible cases based on the barycentric coordinates
    if a > 0 and b > 0 and c > 0:
        return "The point p = (%.2f, %.2f) is inside the triangle" % (point[0], point[1])
    elif a == 1 and b == 0 and c == 0:
        return "The point p = (%.2f, %.2f) is at vertex p1" % (point[0], point[1])
    elif a == 0 and b == 1 and c == 0:
        return "The point p = (%.2f, %.2f) is at vertex p2" % (point[0], point[1])
    elif a == 0 and b == 0 and c == 1:
        return "The point p = (%.2f, %.2f) is at vertex p3" % (point[0], point[1])
    elif a > 0 and b == 0 and c > 0:
        return "The point p = (%.2f, %.2f) is on the edge between vertex p2 and p3" % (point[0], point[1])
    elif a > 0 and b > 0 and c == 0:
        return "The point p = (%.2f, %.2f) is on the edge between vertex p1 and p3" % (point[0], point[1])
    elif a == 0 and b > 0 and c > 0:
        return "The point p = (%.2f, %.2f) is on the edge between vertex p1 and p2" % (point[0], point[1])
    else:
        return "The point p = (%.2f, %.2f) is outside the triangle" % (point[0], point[1])


def check_disjoint_triangles(triangle1_vertices, triangle2_vertices):
    # check if two triangles are disjoint.

    for i in range(0, 3):
        barycentric_coords = compute_barycentric_coords(triangle1_vertices, triangle2_vertices[i])
        # if any point vertice of triangle 2 is inside or on the edge of triangle 1, return false
        if barycentric_coords[0] >= 0 and barycentric_coords[1] >= 0 and barycentric_coords[2] >= 0:
            return False;
    # if none of the triangle2_vertices are inside or on the edge of triangle 1, return true
    return True;


if __name__ == "__main__":
    # Default values
    v1 = [3, 2]
    v2 = [5, 3]
    v3 = [2, 4]
    v = [4, 3]

    # Get coordinates of the points from command line arguments, if any
    if len(sys.argv) == 9:
        v1 = [float(sys.argv[1]), float(sys.argv[2])]
        v2 = [float(sys.argv[3]), float(sys.argv[4])]
        v3 = [float(sys.argv[5]), float(sys.argv[6])]
        v = [float(sys.argv[7]), float(sys.argv[8])]

    # Print coordinates of the points
    print("p1: ", v1, )
    print("p2: ", v2)
    print("p3: ", v3)
    print("p: ", v, "\n")

    # Compute barycentric coordinates
    # a, b, c = compute_barycentric_coords([v1, v2, v3], v)

    # Get location of the point in the triangle
    print(get_location_of_point_in_triangle([v1, v2, v3], v))
