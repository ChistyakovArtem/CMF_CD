import numpy as np


class Strategy:

    def predict(self, position_a, position_b, data):
        a = np.random.uniform(-1, 1)
        b = np.random.uniform(-1, 1)
        return [a, b]
