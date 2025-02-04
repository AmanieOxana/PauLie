from paulie.common.algebras import get_algebra_generators
from paulie.application.charges import non_commuting_charges
from paulie.common.pauli import commutant


#a_8, a_9 posses non-commuting charges for all n
generators = get_algebra_generators("a8")
assert len(non_commuting_charges(generators)) != 0
generators = get_algebra_generators("a9")
assert len(non_commuting_charges(generators)) != 0
