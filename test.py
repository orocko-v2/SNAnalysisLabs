import random

from pyvis.network import Network

import Bayes
import Markov
import lab2_1
import lab3
import MapReduce
import matplotlib.pyplot as plt
import networkx as nx
import json

graph = lab2_1.lab2_2(100)

labels = lab3.create_labels(graph)
# print(labels)
#
# print(lab3.iterative_classification(graph, labels, 30))

# print('---------------------------')
#
print(lab3.random_walk_classification(graph, labels, 5, 100))


# MapReduce.output(graph)
# Bayes.output(graph)
# Markov.output(graph)

import lab3_2
# print('compare: ', lab3_2.compare_labels(graph))
# print('mark: ',lab3_2.edge_mark(graph))
# print('jacard: ', lab3_2.jacard_coef(graph))
# print('cluster: ', lab3_2.cluster_coef(graph))
# print('shortest paths: ', dict(lab3_2.shortest_path(graph)))
# print('influence: ', lab3_2.influence(graph))
print(lab3_2.newman())



