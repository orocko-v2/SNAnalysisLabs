import networkx as nx
from pyvis.network import Network


def compare_labels(G):
    labels = nx.get_node_attributes(G, 'sex')
    print(labels)
    label_dict = {}
    for label in labels.values():
        label_dict[label] = label_dict.get(label, 0) + 1
    return label_dict

def edge_mark(G):
    labels = nx.get_node_attributes(G, 'label')
    edge_label_dict = {}
    for u, v in G.edges():
        edge_label_dict[(u, v)] = f'{labels[u]}-{labels[v]}'
    return edge_label_dict

def jacard_coef(G):
    return list(nx.jaccard_coefficient(G))

def cluster_coef(G):
    return nx.clustering(G)

def shortest_path(G):
    return nx.all_pairs_all_shortest_paths(G)

def influence(G):
    return {node: len(list(G.neighbors(node))) for node in G.nodes()}

def newman():
    G = nx.generators.random_graphs.newman_watts_strogatz_graph(15, 4, 0.5)
    nt = Network()
    nt.from_nx(G)
    nt.show('newman.html', notebook=False)
    return G

