Introductory Tutorial
======================

This tutorial will illustrate how to use :code:`PauLie` to classify the dynamical Lie algebra of a circuit given
the generators consisting of Paulistrings.
A Paulistring is a tensor product of Pauli matrices

.. math::
    \bigotimes_i  \sigma_i \, \sigma_i \in \{I,X,Y,Z\}

and is represented as a string indicating the Pauli matrices successively.
Given a set of Paulistrings, the closure under the commutator defines a Lie algebra.

In `"Full classification of Pauli Lie algebras" <https://arxiv.org/abs/2408.00081>`_.
an efficent algorithm for classifying which Lie algerba is generated is given.
The function :code:`getAlgebra(generators, size=0)` returns exactly which algebra is generated when
given the generator set :code:`generators` which can be extended periodically to arbitray qubit numbers
specified by :code:`size`.