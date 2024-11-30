import sys
sys.path.append('..')

from common.extKlocal import *
from stuff.drawing import *

#XYI;IXY; YIX
for g in genKlocalString(6, "XXX"):
    print(f"{g}")

generators = getKlocalStringGenerators(6, ["XYI", "IXY", "YIX"])
print(f"{generators}");

generators = getKlocalGenerators(6, ["XYI", "IXY", "YIX"])
print(f"{generators}");

generators = getKlocalGenerators(6, ["XYI", "IXY", "YIX"])
plotGraphByNodes(generators)

