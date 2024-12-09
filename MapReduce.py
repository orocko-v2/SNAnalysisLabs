import functools

import lab3

def map_reduce_old(graph, start_node, walk_length, iterations):

    def reducer(a, b):
        return {1: a[1]+b[1], 2: a[2]+b[2]}

    mapper = lambda a: lab3.rw_map_reduce(graph, start_node, walk_length)
    mapped = map(mapper, range(iterations))
    reduced = functools.reduce(reducer, mapped)
    return reduced

def map_reduce(graph):

    def reducer(a, b):
        return a | b

    mapper = lambda a: {a : [x for x in graph.neighbors(a)]}
    mapped = map(mapper, graph.nodes())
    reduced = functools.reduce(reducer, mapped)
    return reduced

def output(graph):
    print(map_reduce(graph))


