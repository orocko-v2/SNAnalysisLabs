import random

from pyvis.network import Network

import Bayes
import Markov
import lab2_1
import lab3
import MapReduce
import matplotlib.pyplot as plt
import networkx as nx

graph = lab2_1.lab2_2()

labels = lab3.create_labels(graph)
# print(labels)
#
# print(lab3.iterative_classification(graph, labels, 10))
#
# print('---------------------------')
#
# print(lab3.random_walk_classification(graph, labels, 5, 100))


# MapReduce.output(graph)
# Bayes.output(graph)
Markov.output(graph)


