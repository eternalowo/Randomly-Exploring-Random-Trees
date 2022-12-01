from random import randint
from math import sqrt, inf

MAXIMUM_X = 1200
MAXIMUM_Y = 700

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

STEP = 35


class Rectangle:
    def __init__(self, min_p, max_p):
        self.points = []
        self.min_p = min_p
        self.max_p = max_p
        self.points.append(min_p)
        self.points.append(max_p)
        self.points.append((min_p[0], max_p[1]))
        self.points.append((max_p[0], min_p[1]))

    def get_points(self):
        return self.points

    def if_inside(self, point):
        if not compute_out_code(point, self.min_p, self.max_p):
            return True
        else:
            return False


def p(a, b, c):
    return (a + b + c) / 2


def scalar_mult(first_vector, second_vector):
    if len(first_vector) != len(second_vector):
        return ''
    result = 0
    for i in range(0, len(first_vector)):
        result += first_vector[i] * second_vector[i]
    return result


def get_vector(first_point, second_point):
    return [second_point[0] - first_point[0], second_point[1] - first_point[1]]


def get_distance(first_point, second_point):
    return sqrt((second_point[0] - first_point[0]) ** 2 + (second_point[1] - first_point[1]) ** 2)


def get_height_point(point, segment_first, segment_second):
    component = scalar_mult(get_vector(segment_first, segment_second), get_vector(segment_first, point)) / \
                scalar_mult(get_vector(segment_first, segment_second), get_vector(segment_first, segment_second))
    vec = get_vector(segment_first, segment_second)
    vec[0] *= component
    vec[1] *= component
    return round(segment_first[0] + vec[0]), round(segment_first[1] + vec[1])


def compute_out_code(point, rect_min, rect_max):
    code = INSIDE
    if point[0] < rect_min[0]:
        code = code | LEFT
    elif point[0] > rect_max[0]:
        code = code | RIGHT
    if point[1] < rect_min[1]:
        code = code | BOTTOM
    elif point[1] > rect_max[1]:
        code = code | TOP
    return code


def cohen_sutherland_line_clip(segment_first, segment_second, rect_min, rect_max):
    out_code0 = compute_out_code(segment_first, rect_min, rect_max)
    out_code1 = compute_out_code(segment_second, rect_min, rect_max)
    segment_first = list(segment_first)
    segment_second = list(segment_second)
    collision = False

    while True:
        if not (out_code0 | out_code1):
            collision = True
            break
        elif out_code0 & out_code1:
            break
        else:
            if out_code1 > out_code0:
                outcode_out = out_code1
            else:
                outcode_out = out_code0
            if outcode_out & TOP:
                x = segment_first[0] + (segment_second[0] - segment_first[0]) * (rect_max[1] - segment_first[1]) / (
                        segment_second[1] - segment_first[1])
                y = rect_max[1]
            if outcode_out & BOTTOM:
                x = segment_first[0] + (segment_second[0] - segment_first[0]) * (rect_min[1] - segment_first[1]) / (
                        segment_second[1] - segment_first[1])
                y = rect_min[1]
            if outcode_out & RIGHT:
                y = segment_first[1] + (segment_second[1] - segment_first[1]) * (rect_max[0] - segment_first[0]) / (
                        segment_second[0] - segment_first[0])
                x = rect_max[0]
            if outcode_out & LEFT:
                y = segment_first[1] + (segment_second[1] - segment_first[1]) * (rect_min[0] - segment_first[0]) / (
                        segment_second[0] - segment_first[0])
                x = rect_min[0]
            if outcode_out == out_code0:
                segment_first[0] = x
                segment_first[1] = y
                out_code0 = compute_out_code(segment_first, rect_min, rect_max)
            else:
                segment_second[0] = x
                segment_second[1] = y
                out_code1 = compute_out_code(segment_second, rect_min, rect_max)
    return collision, list(map(round, segment_first)), list(map(round, segment_second))


def dijkstra_algorithm(g, start_node):
    unvisited_nodes = g.get_vertices()
    shortest_path = {}
    previous_nodes = {}
    for node in unvisited_nodes:
        shortest_path[node] = inf
    shortest_path[start_node] = 0

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node is None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        neighbours = g.get_adjacent(current_min_node)
        for neighbour in neighbours:
            tentative_value = shortest_path[current_min_node] + g.get_edge_weight(current_min_node, neighbour)
            if tentative_value < shortest_path[neighbour]:
                shortest_path[neighbour] = tentative_value
                previous_nodes[neighbour] = current_min_node

        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    path.append(start_node)

    return path, shortest_path[target_node]


def get_step(first_point, second_point, step=STEP):
    dist = get_distance(first_point, second_point)
    k = step / dist
    x = round(first_point[0] + k * (second_point[0] - first_point[0]))
    y = round(first_point[1] + k * (second_point[1] - first_point[1]))
    if x > MAXIMUM_X or x < 0 or y > MAXIMUM_Y or y < 0:
        _, p1, p2 = cohen_sutherland_line_clip(first_point, (x, y), (0, 0), (MAXIMUM_X, MAXIMUM_Y))
        if p1[0] == 0 or p1[0] == MAXIMUM_X or p1[1] == 0 or p1[1] == MAXIMUM_Y:
            return p1
        else:
            return p2
    return x, y


def get_shortest_distance(point, segment_first, segment_second):
    second_scalar = scalar_mult(get_vector(segment_second, segment_first), get_vector(point, segment_first))
    third_scalar = scalar_mult(get_vector(segment_first, segment_second), get_vector(point, segment_second))
    if second_scalar > 0 and third_scalar > 0:
        a = get_distance(point, segment_first)
        b = get_distance(point, segment_second)
        c = get_distance(segment_first, segment_second)
        hper = p(a, b, c)
        return 2 * (sqrt(hper * (hper - a) * (hper - b) * (hper - c))) / c


def nearest(g, x):
    minimum = inf
    vertex_edge = None
    result = None
    for vertex in g.get_vertices():
        if get_distance(vertex, x) < minimum:
            minimum = get_distance(vertex, x)
            result = vertex
    for edge in g.edges:
        if get_shortest_distance(x, edge[0], edge[1]) is not None:
            if get_shortest_distance(x, edge[0], edge[1]) < minimum:
                minimum = get_shortest_distance(x, edge[0], edge[1])
                vertex_edge = x
                to_remove1 = edge[0]
                to_remove2 = edge[1]
                graph_vertex = get_height_point(x, edge[0], edge[1])
    if vertex_edge is not None:
        g.remove_edge(to_remove1, to_remove2)
        g.add_edge(to_remove1, graph_vertex)
        g.add_edge(to_remove2, graph_vertex)
        result = graph_vertex
    return result


def steer(x, y, obstacles):
    z = get_step(x, y)
    for obstacle in obstacles:
        res = cohen_sutherland_line_clip(x, z, obstacle.min_p, obstacle.max_p)
        if res[0]:
            if get_distance(res[2], x) < get_distance(res[1], x):
                z = res[2]
            else:
                z = res[1]
    return tuple(z)


def random_sample():
    return randint(4, MAXIMUM_X - 3), randint(4, MAXIMUM_Y - 3)
