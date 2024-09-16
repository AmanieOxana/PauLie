import networkx as nx
from classifier.graphView import *
from common.pauli import *

def getSubgraphs(nodes):
    subgraphs = []
    vertices, edges, edge_labels = getGraphView(nodes)
    g = nx.Graph()
    g.add_nodes_from(vertices)
    g.add_edges_from(edges)
    string_subgraphs = sorted(nx.connected_components(g), key=len, reverse=True)
    for sb in string_subgraphs:
        subgraph = [] 
        for item in sb:
            subgraph.append(getPauliArray(item))
        subgraphs.append(subgraph)
    return subgraphs

