import sys
sys.path.append('..')

from common.ext2local import *

for g in gen2localString(4, "XY"):
    print(f"{g}")

generators = get2localStringAlgebraGenerators(4, "b0")
print(f"{generators}")
