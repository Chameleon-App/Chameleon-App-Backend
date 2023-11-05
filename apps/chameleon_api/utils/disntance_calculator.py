import numpy as np


class DistanceCalculator:
    @staticmethod
    def compute_euclidean_distance(x: np.array, y: np.array):
        dists = np.sqrt(
            -2 * (x @ y.T)
            + np.power(x, 2).sum(axis=1, keepdims=True)
            + np.power(y, 2).sum(axis=1, keepdims=True).T
        )

        return dists
