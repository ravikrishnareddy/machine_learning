import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x**2

plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("X vs Y")