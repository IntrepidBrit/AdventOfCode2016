def is_possible_triangle(triangle_definition):
    side_list = sorted([int(side) for side in triangle_definition.split()])
    return float(side_list[0]) + float(side_list[1]) > float(side_list[2])


def count_possible_triangles(triangle_data):
    triangle_data = triangle_data.split('\n')
    flat = [item for sublist in triangle_data for item in sublist.split()]
    rejigged = []
    for r in range(0, len(triangle_data), 3):
        for c in range(0, 3):
            rejigged.append("{0} {1} {2}".format(flat[3 * r + c], flat[3 * r + c + 3], flat[3 * r + c + 6]))

    return sum(map(is_possible_triangle, rejigged))
