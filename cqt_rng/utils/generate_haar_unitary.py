import numpy as np


def generate_haar_unitary(dim):
    """Generate a (dim, dim) Haar-random matrix using the QR decomposition.
    Source: https://pennylane.ai/qml/demos/tutorial_haar_measure.html

    Parameters:
        dim (int): the dimension of the matrix.
    """
    # Step 1
    A, B = np.random.normal(size=(dim, dim)), np.random.normal(size=(dim, dim))
    Z = A + 1j * B

    # Step 2
    Q, R = np.linalg.qr(Z)

    # Step 3
    Lambda = np.diag([R[i, i] / np.abs(R[i, i]) for i in range(dim)])

    # Step 4
    return np.dot(Q, Lambda)
