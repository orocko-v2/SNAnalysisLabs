import random

from pyvis.network import Network

import lab2_1

color_map = {
        1: '#FFB6C1',
        2: '#4169E1'
    }

def create_labels(G):
    labels = {}
    for node in G.nodes:
        if 'sex' in G.nodes.get(node):
            labels[node] = G.nodes.get(node)['sex']
        else:
            labels[node] = None
    return labels

def visualize_algorithm(G, labels, name):
    new_G = G.copy()
    for node in new_G.nodes():
        if labels[node] == 1:
            new_G.nodes.get(node)['color'] = color_map[1]
        elif labels[node] == 2:
            new_G.nodes.get(node)['color'] = color_map[2]
    nt = Network()
    nt.from_nx(new_G)
    nt.show(name, notebook=False)

def iterative_classification(G, labels, iterations):
    for _ in range(iterations):
        new_labels = labels.copy()
        non_labeled_nodes = [node for node in G.nodes() if labels[node] is None]
        for node in non_labeled_nodes:
            neigbour_labels = [labels[neighbour] for neighbour in G.neighbors(node)if labels[neighbour] is not None]
            if neigbour_labels:
                new_labels[node] = max(set(neigbour_labels), key = neigbour_labels.count)
        labels = new_labels
    visualize_algorithm(G, labels, 'iterative.html')
    return labels

def random_walk(G, start_node, walk_length, iterations):

    label_dict = {1: 0, 2: 0}
    for _ in range(iterations):
        current_node = start_node
        path = [current_node]
        for __ in range(walk_length):
            next_node = random.choice(list(G.neighbors(current_node)))
            path.append(next_node)
            current_node = next_node
        for node in path:
            if 'sex' in G.nodes.get(node):
                label_dict[G.nodes.get(node)['sex']] += 1
    return label_dict


def random_walk_classification(G, labels, walk_length, iterations):
    new_labels = labels.copy()
    for node in G.nodes():
        if labels[node] is None:
            start_node = node
            label_dict = random_walk(G, start_node=start_node, walk_length=walk_length, iterations=iterations)
            print(label_dict)
            new_labels[node] = max(label_dict, key=label_dict.get)
    visualize_algorithm(G, new_labels, 'random_walk.html')
    return new_labels


def rw_map_reduce(G, start_node, walk_length):

    label_dict = {1: 0, 2: 0}
    current_node = start_node
    path = [current_node]
    for __ in range(walk_length):
        next_node = random.choice(list(G.neighbors(current_node)))
        path.append(next_node)
        current_node = next_node
    for node in path:
        if 'sex' in G.nodes.get(node):
            label_dict[G.nodes.get(node)['sex']] += 1
    return label_dict
