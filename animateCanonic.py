from common.pauli import *
from common.generator import *
from classifier.transform import *
from classifier.graphView import *
from classifier.drawing import *
from classifier.recording import *



def buildAndAnimate(nodes):
    record = RecordGraph()
    canonics = transformToCanonics(nodes, record = record)
    nodes = mergeCanonics(canonics)
    vertices, edges, edge_labels =  getGraphView(nodes)
    animationGraph(record)

generators = getAllCommutators(8, getAlgebra("a6"))
buildAndAnimate(generators)





