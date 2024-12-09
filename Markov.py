import random

import pgmpy
from pgmpy.models import MarkovNetwork
from pgmpy.factors.discrete import DiscreteFactor
from pgmpy.inference import VariableElimination
from pyvis.network import Network

def create_input_data(G):
    return G.edges(4)

def create_markov(edges):
    model = MarkovNetwork()
    model.add_edges_from(edges)

    for node in model.nodes:
        model.nodes[node]['label'] = str(node)
        model.nodes[node]['color'] = ("#%06x" % random.randint(0, 0xFFFFFF))

    for pair in model.edges:
        node1, node2 = pair[0], pair[1]
        factor = DiscreteFactor([node1, node2],
                            cardinality=[2,2],
                            values=[random.uniform(0.0, 1.0) for i in range(4)])

        model.add_factors(factor)

    if model.check_model():
        return model

def output(G):
    data = create_input_data(G)
    model = create_markov(data)

    print('NODES: ', model.nodes)
    print('EDGES: ', model.edges)
    print('FACTORS: ')
    for factor in model.factors:
        print(factor)


    inference = VariableElimination(model)
    print(inference.query(variables=[4], evidence={16: 1}))

    nt = Network(directed=False)
    nt.from_nx(model)
    print(nt.get_node(4))
    nt.show('graph4.html', notebook=False)


