import numpy as np
from scipy import linalg


if __name__ == "__main__":
    a = np.array([[165, 25],[25,5]])
    b = np.array([96,16])
    x = linalg.solve(a, b)
    print("y=", x[0], "x+", x[1])