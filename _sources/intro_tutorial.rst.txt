Introductory Tutorial
======================

This tutorial will illustrate how to use :code:`PauLie` to classify the dynamical Lie algebra of a circuit given
the generators consisting of Paulistrings.
A Paulistring is a tensor product of Pauli matrices

.. math::
    P = \bigotimes_i  \sigma_i \, \sigma_i \in \{I,X,Y,Z\}

and is represented as a string indicating the Pauli matrices successively.
Given a set of Paulistrings, the closure under the commutator defines a Lie algebra.

In `"Full classification of Pauli Lie algebras" <https://arxiv.org/abs/2408.00081>`_ [1].
an efficient algorithm for classifying which Lie algebra is generated is given.
The function :code:`getAlgebra(generators, size=0)` returns exactly which algebra is generated when
given the generator set :code:`generators` which can be extended periodically to arbitrary qubit numbers
specified by :code:`size`.
We can reproduce Example I.5 in `"Classification of dynamical Lie algebras of 2-local spin systems on linear, circular and fully connected topologies" <https://www.nature.com/articles/s41534-024-00900-2>`_.

.. code-block:: python

    from PauLie import getAlgebra
    size = 2
    generators = ["XY"]
    algebra = getAlgebra(generators, size=size)
    print(f"size = {size} algebra = {algebra}")

outputs

.. code-block:: bash

    size = 2 algebra = u(1)

whereas changing to a three qubit system, results another algebra:

.. code-block:: python

    size = 3
    algebra = getAlgebra(generators, size=size)
    print(f"size = {size} algebra = {algebra}")

outputs

.. code-block:: bash

    size = 3 algebra = so(3)

The algorithms is based on the concept of an anticommutation graph. Given a set of n-qubit Paulistrings
:math:`\mathcal{G} = \{P_1,\dots ,P_{n_G}\}`, the anticommutation graph has as a vertex set :math:`\mathcal{G}`
and edges between all vertices that do not commute. Now the edge between :math:`P_i` and :math:`P_j` can be contracted
by mapping :math:`P_i \mapsto \pm \frac{1}{2} i [P_i,P_j] = P_i^\star`. Now if :math:`P_i^\star` is already in :math:`\mathcal{G}`,
the size of the generator set has been reduced while leaving the Lie algebra invariant.
We can illustrate this for the generating set :code:`["XYI", "IXY", "XZY"]` via the function :code:`animationAntiCommutationGraph(generators)`.
As the third Paulistring is proportional to the commutator of the first two Paulistrings it can be contracted.

.. raw:: html
    :file: media/example.html

For any generator set consisting of Paulistrings, the anticommutation graph can be transformed to four canonical types (Theorem 1, [1]).
In the example the resulting graph is a line graph with two vertices and no single vertices. Therefore it is of type A and the
according to Theorem 2 [1], it corresponds to :math:`\mathfrak{so}(3)`.

The Lie algebra plays a pivotal role in quantum control theory to understand the reachability of states.
Also measure based on operator spread capturing quantum circuit complexity rely on this concept.
Furthermore, determining moments of circuits can be significantly simplified when the Lie algebra is known.
All these three applications are to be added as functionalities of :code:`PauLie` in the future.






