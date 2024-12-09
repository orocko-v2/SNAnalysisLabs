import random

import pgmpy

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
from pyvis.network import Network

import lab2_1


def create_input_data(G):
    return [edge[::-1] for edge in G.edges(4)]


def create_bayes(edges):
    model = BayesianNetwork()
    model.add_edges_from(edges)
    node_list = list(model.nodes)
    for node in model.nodes:
        model.nodes[node]['label'] = str(node)
        model.nodes[node]['color'] = ("#%06x" % random.randint(0, 0xFFFFFF))
        print(model.nodes[node])
    node_list.sort(reverse=True)
    cpd_1 = TabularCPD(node_list[0], variable_card=2, values=[[0.6], [0.4]])
    cpd_2 = TabularCPD(node_list[1], variable_card=2, values=[[0.2], [0.8]])
    cpd_3 = TabularCPD(node_list[2], variable_card=2, values=[[0.5], [0.5]])
    cpd_4 = TabularCPD(node_list[3], variable_card=2, values=[[0.7, 0.55, 0.85, 0.05, 0.6, 0.35, 0.25, 0.1],
                                                     [0.3, 0.45, 0.15, 0.95, 0.4, 0.65, 0.75, 0.9]],
                       evidence=[node_list[0], node_list[1], node_list[2]], evidence_card=[2, 2, 2])
    model.add_cpds(cpd_1, cpd_2, cpd_3, cpd_4)
    if model.check_model():
        return model

def output(G):
    data = create_input_data(G)
    bayes = create_bayes(data)
    print('NODES: ', bayes.nodes)
    print('EDGES: ', bayes.edges)
    print('CPD for node 4: ', bayes.get_cpds(4))

    node_list = list(bayes.nodes)
    node_list.sort(reverse=True)

    inference = VariableElimination(bayes)
    print(inference.query(variables=[4], evidence={node_list[0]: 0, node_list[1]: 0, node_list[2]: 1}))

    nt = Network(directed=True)
    nt.from_nx(bayes)
    print(nt.get_node(4))
    nt.show('graph3.html', notebook=False)
