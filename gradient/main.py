import numpy as np
from numpy import asarray
from numpy import arange
from numpy.random import rand
import matplotlib.pyplot as plt 

def f(x):
    return x**2.0

def df(x):
    return x * 2.0

inputs = []
outputs = []

solutions = [] #x
evaluations = [] #y

bounds = np.array([[-10.0, 10.0]])

for i in range(1000):
    x = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    y = objective(x)
    inputs.append(x)
    outputs.append(y)



x = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
for i in range(20):
    solutions.append(x)
    x_evaluation = f(x)
    evaluations.append(x_evaluation)

    gradient = df(x)
    new_x = x - 0.1*gradient
    x = new_x

plt.scatter(inputs, outputs)
plt.scatter(solutions, evaluations, color="red")
