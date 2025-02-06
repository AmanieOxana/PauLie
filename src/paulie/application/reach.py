from paulie.application.classify import get_algebra
from scipy.linalg import block_diag

def is_in_so(A):
    return A.dot(A.T) == np.eye(A.shape)

def is_in_sp(A):
    D = A.shape[0]
    J = np.fliplr(block_diag(np.eye(D/2), np.eye(D/2)))
    return A.conj @ J @ A == J

def reachable(U, generators):
    """
    input: U as a numpy array, generator list
    output: whether it is reachable
    """
    if U.shape[0] > len(generators[0]):
        raise AssertionError("unitary can not be generated by generators of smaller dimensions")
    algebra = get_algebra(generators)
    if algebra == su:
        return True
    if algebra == so and is_in_so(U):
        return True
    if algebra == sp and is_in_sp(U):
        return True
    # the case of direct sum has to be worked out in detail
