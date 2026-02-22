import matplotlib.pyplot as plt
import numpy as np

""" Derivada da função sigmoid logística """
x = np.linspace(-10, 10, 400)
sigmoid = 1 / (1 + np.exp(-x))
sigmoid_derivative = sigmoid * (1 - sigmoid)


dot = (0,0.25)

plt.plot(x, sigmoid_derivative, label="Derivada da Sigmoid Logística")
plt.scatter(*dot, color='orange')  # ponto máximo
plt.xlabel("z", size=16)
plt.ylabel("σ'(z)", size=16)
plt.grid(False)
plt.show()