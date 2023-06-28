# 3d pyramid with squared base of radius 5
vertices = {
    "V1": {"cord": [1.5, -1.5, 0], "av": "a1"},
    "V2": {"cord": [1.5, 1.5, 0], "av": "a2"},
    "V3": {"cord": [-1.5, 1.5, 0], "av": "a3"},
    "V4": {"cord": [-1.5, -1.5, 0], "av": "a4"},
    "V5": {"cord": [0, 0, 5], "av": "a5"}
}

faces = {
    "F1": "a1",
    "F2": "a2",
    "F3": "a3",
    "F4": "a5",
    "F5": "a4"
}

edges = {
    "a1": {
        "v1": "V1",
        "v2": "V2",
        "fccw": "F1",
        "fcw": "F5",
        "pccw": "a5",
        "nccw": "a6",
        "ncw": "a4",
        "pcw": "a2"
    },
    "a2": {
        "v1": "V2",
        "v2": "V3",
        "fccw": "F2",
        "fcw": "F5",
        "pccw": "a6",
        "nccw": "a7",
        "ncw": "a1",
        "pcw": "a3"
    },
    "a3": {
        "v1": "V3",
        "v2": "V4",
        "fccw": "F3",
        "fcw": "F5",
        "pccw": "a7",
        "nccw": "a8",
        "ncw": "a2",
        "pcw": "a5"
    },
    "a4": {
        "v1": "V4",
        "v2": "V1",
        "fccw": "F4",
        "fcw": "F5",
        "pccw": "a8",
        "nccw": "a5",
        "ncw": "a7",
        "pcw": "a1"
    },
    "a5": {
        "v1": "V1",
        "v2": "V5",
        "fccw": "F4",
        "fcw": "F1",
        "pccw": "a4",
        "nccw": "a8",
        "ncw": "a1",
        "pcw": "a6"
    },
    "a6": {
        "v1": "V2",
        "v2": "V5",
        "fccw": "F1",
        "fcw": "F2",
        "pccw": "a1",
        "nccw": "a5",
        "ncw": "a2",
        "pcw": "a7"
    },
    "a7": {
        "v1": "V3",
        "v2": "V5",
        "fccw": "F2",
        "fcw": "F3",
        "pccw": "a2",
        "nccw": "a6",
        "ncw": "a3",
        "pcw": "a8"
    },
    "a8": {
        "v1": "V4",
        "v2": "V5",
        "fccw": "F3",
        "fcw": "F4",
        "pccw": "a3",
        "nccw": "a7",
        "ncw": "a4",
        "pcw": "a5"
    }}

def get_face_vertices(face):

    # Retrieve the initial face from the faces dictionary
    initial_face = faces[face]
    current_face = initial_face

    # Initialize a list to store the found vertices
    found_vertices = [edges[current_face]["v1"], edges[current_face]['v2']]

    # Set a flag to control the loop termination
    stop_flag = False

    # Iterate until the stop_flag is True
    while not stop_flag:

        # Check if the next face in the counterclockwise direction (fccw) is the initial face
        if edges[current_face]["fccw"] == face:
            # Update the current_face to the next face in the counterclockwise direction (nccw)
            current_face = edges[current_face]["nccw"]
        else:
            # Update the current_face to the next face in the clockwise direction (ncw)
            current_face = edges[current_face]["ncw"]

        # Check if the vertex 1 of the current_face is not in the found_vertices list
        if edges[current_face]["v1"] not in found_vertices:
            # Add vertex 1 to the found_vertices list
            found_vertices.append(edges[current_face]["v1"])

        # Check if the vertex 2 of the current_face is not in the found_vertices list
        elif edges[current_face]["v2"] not in found_vertices:
            # Add vertex 2 to the found_vertices list
            found_vertices.append(edges[current_face]["v2"])

        # Check if the current_face is equal to the initial face
        if current_face == initial_face:
            # Set the stop_flag to True to exit the loop
            stop_flag = True

    # Return the found_vertices list containing the vertices of the face
    return found_vertices



def get_adjacent_vertices(vertex):
    adjacent_vertices = []
    
    # Iterate through each edge in the edges dictionary
    for edge_value in edges.values():

        # Check if the vertex is the first endpoint of the edge
        if edge_value['v1'] == vertex:

            # If it is, add the second endpoint to the adjacent_vertices list
            adjacent_vertices.append(edge_value['v2'])

        # Check if the vertex is the second endpoint of the edge
        elif edge_value['v2'] == vertex:

            # If it is, add the first endpoint to the adjacent_vertices list
            adjacent_vertices.append(edge_value['v1'])
    
    # Return the adjacent vertices
    return adjacent_vertices



print(get_face_vertices("F5"))
print(get_adjacent_vertices("V3"))