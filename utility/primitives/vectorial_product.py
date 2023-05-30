import sys
import pseudo_angle


def compute_vectorial_product(u, v):
    # Compute vectorial product between u and v

    # Compute vectorial product
    vectorial_product = u[0] * v[1] - u[1] * v[0]

    return vectorial_product


def get_convex_angle(u, v):
    # Compute pseudo angles - show with 4 decimal places
    pseudo_angle_u = pseudo_angle.compute_pseudo_angle(u[0], u[1])
    print("pseudo_angle_u: %.4f" % pseudo_angle_u)
    pseudo_angle_v = pseudo_angle.compute_pseudo_angle(v[0], v[1])
    print("pseudo_angle_v: %.4f" % pseudo_angle_v, "\n")

    # Compute convex angle
    convex_angle = abs(pseudo_angle_u - pseudo_angle_v)

    # If one of the vectors is on the 4-th quadrant (7 < pseudo_angle < 8), and the other is on the
    # 1-st or 2-nd quadrant (0 < pseudo_angle < 4), subtract 8 from the pseudo angle
    if (pseudo_angle_u > 7 and pseudo_angle_v < pseudo_angle_u - 4) or (pseudo_angle_v > 7 and pseudo_angle_u < pseudo_angle_v - 4):
        convex_angle = 8 - convex_angle

    print("convex_angle: %.4f" % convex_angle, "\n")

    return convex_angle


def check_vectorial_product(u, v, w):
    # Compute vector product
    vector_product_uv = compute_vectorial_product(u, v)
    print("vector_product_uv: ", vector_product_uv)
    vector_product_uw = compute_vectorial_product(u, w)
    print("vector_product_uw: ", vector_product_uw)
    vector_product_vw = compute_vectorial_product(v, w)
    print("vector_product_vw: ", vector_product_vw, "\n")

    convex_angle = get_convex_angle(u, v)

    # Check if u, v are collinear
    if vector_product_uv == 0:
        return 0

    # Check if u, v form a convex angle
    if vector_product_uw > 0 > vector_product_vw and convex_angle <= 2:
        return 1

    if vector_product_uw < 0 < vector_product_vw and convex_angle <= 2:
        return 1

    # Otherwise
    return 2


if __name__ == "__main__":
    # Default values
    u_vec = [1, 0.5]
    v_vec = [1, -0.5]
    w_vec = [2, 0.5]

    # Check if the correct number of arguments is provided
    if len(sys.argv) == 7:
        # Parse the command-line arguments
        u_vec = [float(sys.argv[1]), float(sys.argv[2])]
        v_vec = [float(sys.argv[3]), float(sys.argv[4])]
        w_vec = [float(sys.argv[5]), float(sys.argv[6])]

    # Vectors
    print("u: ", u_vec)
    print("v: ", v_vec)
    print("w: ", w_vec, "\n")

    # Call the check_vectorial_product function
    result = check_vectorial_product(u_vec, v_vec, w_vec)

    # Print the result
    print("Result:", result, "(where 0 means collinear, 1 means inside the convex angle and 2 otherwise)")
