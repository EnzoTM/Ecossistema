import numpy as np

#MSE = Mean Squared Error
class MSE:
    def __init__(self) -> None:
        pass

    def calculate(self, expected: np.ndarray, predicted: np.ndarray) -> np.ndarray:
        return np.mean(np.power(predicted - expected, 2)) / expected.size

    def gradient(self, expected: np.ndarray, predicted: np.ndarray) -> np.ndarray:
        return 2 * (predicted - expected) / expected.size
