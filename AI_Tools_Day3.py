import numpy as np

banana = np.array([1, 3, 6])
orange = np.array([0, 1, 4])
apple = np.array([-3, 6, 12])

distance = np.linalg.norm(banana - apple)
print(f"Distance = {distance:.2f}")

#output will be Distance = 7.81
