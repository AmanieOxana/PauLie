import sys
sys.path.append('..')

from common.extKlocal import *
from stuff.drawing import *


generators = getKlocalAlgebraGenerators(2, "a13")
nestedNodes = getKlocalNestedNodesInAgebraGenerator(2, "a13")
plotGraphByNodes(nestedNodes, generators)