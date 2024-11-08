import numpy as np
from pyvis.network import Network
import random
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
r = lambda: random.randint(0,255)
import lab1_2

def draw(G, pos, measures, measure_name):
    nodes = nx.draw_networkx_nodes(G, pos, node_size=250, cmap=plt.cm.plasma,
                                   node_color=list(measures.values()),
                                   nodelist=measures.keys())
    nodes.set_norm(mcolors.SymLogNorm(linthresh=0.01, linscale=1, base=10))
    label_dict = {}
    for node in G.nodes:
        label_dict[node] = G.nodes.get(node)['label']
    labels = nx.draw_networkx_labels(G, pos, labels = label_dict, font_size=6)
    edges = nx.draw_networkx_edges(G, pos)

    plt.title(measure_name)
    plt.colorbar(nodes)
    plt.axis('off')
    plt.show()

def degree_visualization(G):
    degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
    dmax = max(degree_sequence)

    fig = plt.figure("Degree of a random graph", figsize=(8, 8))

    ax2 = fig.add_subplot()
    ax2.bar(*np.unique(degree_sequence, return_counts=True))
    ax2.set_title("Degree histogram")
    ax2.set_xlabel("Degree")
    ax2.set_ylabel("# of Nodes")
    fig.tight_layout()
    plt.show()

#group_users_graph = Network(notebook=True, select_menu=True)
nx_graph = nx.Graph()

color_map = {
    1: '#FFB6C1',
    2: '#4169E1'
}

data = lab1_2.doLab2('all')
users = data[0]
cities = data[1]
del cities['NA']

cities_list = list(range(1, len(cities) + 1))
i = len(cities) + 1
for user in users:
    user['id'] = i
    i+=1



i = 1
for city in cities:
    nx_graph.add_node(i, label = city, shape = 'box', color = "#%06x" % random.randint(0, 0xFFFFFF))
    i+=1

nx_graph.add_nodes_from([(user['id'], {'label': user['first_name'], 'color': color_map[user['sex']]}) for user in users])


pos = nx.spring_layout(nx_graph, seed=675)


for user in users:
    for city in cities_list:
        if user.get('city'):
            if nx_graph.nodes.get(city)['label'] == user['city']['title']:
                nx_graph.add_edge(city, user['id'])

colors = []
for node in nx_graph.nodes:
    if 'sex' not in nx_graph.nodes.get(node):
        colors.append("#%06x" % random.randint(0, 0xFFFFFF))
    elif nx_graph.nodes.get(node)['sex'] == 1:
        colors.append(color_map[1])
    else:
        colors.append(color_map[2])

nt = Network()
nt.from_nx(nx_graph)
nt.show('graph2.html', notebook=False)



print('DEGREES:', nx_graph.degree)
degree_visualization(nx_graph)

isolated_nodes = list(nx.isolates(nx_graph))
print('ISOLATED NODES:', isolated_nodes)


degree_centrality = nx.degree_centrality(nx_graph)
print('CENTRALITY DEGREE:', degree_centrality)
degree_centrality_max = max(degree_centrality, key=degree_centrality.get)
print('MAX CENTRALITY DEGREE:', nx_graph.nodes.get(degree_centrality_max)['label'], degree_centrality[degree_centrality_max])

betweenness_centrality = nx.betweenness_centrality(nx_graph)
print('BETWEENNESS:', betweenness_centrality)
betweenness_centrality_max = max(betweenness_centrality, key=betweenness_centrality.get)
print('MAX BETWEENNESS:', nx_graph.nodes.get(betweenness_centrality_max)['label'], betweenness_centrality[betweenness_centrality_max])

closeness_centrality = nx.closeness_centrality(nx_graph)
print('CLOSENESS:', closeness_centrality)
closeness_centrality_max = max(closeness_centrality, key=closeness_centrality.get)
print('MAX CLOSENESS:', nx_graph.nodes.get(closeness_centrality_max)['label'], closeness_centrality[closeness_centrality_max])

eigenvector_centrality = nx.eigenvector_centrality(nx_graph)
print('EIGENVECTOR:', eigenvector_centrality)
eigenvector_centrality_max = max(eigenvector_centrality, key=eigenvector_centrality.get)
print('MAX EIGENVECTOR:', nx_graph.nodes.get(eigenvector_centrality_max)['label'], eigenvector_centrality[eigenvector_centrality_max])

katz_centrality = nx.katz_centrality(nx_graph)
print('KATZ:', katz_centrality)
katz_centrality_max = max(katz_centrality, key=katz_centrality.get)
print('MAX KATZ:', nx_graph.nodes.get(katz_centrality_max)['label'], katz_centrality[katz_centrality_max])

harmonic_centrality = nx.harmonic_centrality(nx_graph)
print('HARMONIC:', harmonic_centrality)
harmonic_centrality_max = max(harmonic_centrality, key=harmonic_centrality.get)
print('MAX HARMONIC:', nx_graph.nodes.get(harmonic_centrality_max)['label'], harmonic_centrality[harmonic_centrality_max])

draw(nx_graph, pos, nx.degree_centrality(nx_graph), 'Centrality degree')
draw(nx_graph, pos, nx.betweenness_centrality(nx_graph), 'Betweenness')
draw(nx_graph, pos, nx.closeness_centrality(nx_graph), 'Closeness')
draw(nx_graph, pos, nx.eigenvector_centrality(nx_graph), 'Eigenvector')
draw(nx_graph, pos, nx.katz_centrality(nx_graph, alpha=0.2), 'Katz')
draw(nx_graph, pos, nx.harmonic_centrality(nx_graph), 'harmonic')





