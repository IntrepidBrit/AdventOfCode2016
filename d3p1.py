def is_possible_triangle(triangle_definition):
    side_list = sorted([int(side) for side in triangle_definition.split()])
    return float(side_list[0]) + float(side_list[1]) > float(side_list[2])


def count_possible_triangles(triangle_data):
    return sum(map(is_possible_triangle, triangle_data.split('\n')))
