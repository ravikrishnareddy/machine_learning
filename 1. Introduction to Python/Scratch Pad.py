# List references
x = ['a', 'b', 'c']
y = x
y = x[0:2]
print(x, y)

# Numpy
import numpy as np
height = [1.61, 1.65, 1.69, 1.73, 1.77, 1.81]
weight = [40, 45, 50, 55, 60, 65]
height_np = np.array(height)
weight_np = np.array(weight)
bmi = weight_np/height_np**2
print(np.round(bmi,2))