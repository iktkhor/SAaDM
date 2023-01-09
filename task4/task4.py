from io import StringIO
import csv
import math


def csv_to_array(datafile):
    result = []
    reader = csv.reader(datafile, delimiter=",")

    for row in reader:
        result.append(row)

    return result


def read_csv_string(string_data):
    string_stream = StringIO(string_data)

    return csv_to_array(string_stream)


def get_node_list(graph):
    node_map = {}

    for [parent, child] in graph:
        node_map[parent] = True
        node_map[child] = True

    return list(node_map.keys())


def get_child(node, graph):
    found = []

    for [parent, child] in graph:

        if parent == node:
            found.append(child)

    return found


def get_parent(node, graph):
    found = []

    for [parent, child] in graph:

        if child == node:
            found.append(parent)

    return found


def get_ancestor(node, graph):
    found = []
    parents = get_parent(node, graph)

    for parent in parents:
        grand_parents = get_parent(parent, graph)

        if (len(grand_parents) > 0):
            found.extend(grand_parents)
            found.extend(get_ancestor(parent, graph))

    return found


def get_descendant(node, graph):
    found = []
    children = get_child(node, graph)

    for child in children:
        grand_children = get_child(child, graph)

        if (len(grand_children) > 0):
            found.extend(grand_children)
            found.extend(get_ancestor(child, graph))

    return found


def get_neighbours(node, graph):
    parents = get_parent(node, graph)
    neighbours = []

    for parent in parents:
        children = get_child(parent, graph)
        children.remove(node)
        neighbours.extend(children)

    return neighbours


def get_entropy(graph_stats):
    total_sum = 0
    n = len(graph_stats)

    for [node, stats] in graph_stats:
        in_sum = 0

        for j in stats:
            p = j / (n - 1)
            
            if p > 0:
                b = math.log(p, 2)
                in_sum += p * b
        total_sum += in_sum

    return -total_sum


def task(str_graph):
    graph = read_csv_string(str_graph)
    node_list = get_node_list(graph)
    result = []

    for node in node_list:
        r1 = get_child(node, graph)
        r2 = get_parent(node, graph)
        r3 = get_descendant(node, graph)
        r4 = get_ancestor(node, graph)
        r5 = get_neighbours(node, graph)
        result.append(["n" + node, [len(r1), len(r2), len(r3), len(r4), len(r5)]])

    entropy = get_entropy(result)

    return entropy