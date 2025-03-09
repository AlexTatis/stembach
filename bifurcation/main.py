import matplotlib.pyplot as plt
import numpy as np

growth_rates = np.linspace(0.7, 4, 240000)
x_values = []
bacteria_counts = []

for growth_rate in growth_rates:
  x_values.append(growth_rate)

  population = np.random.random()
  for _ in range(1001):
    population = (growth_rate * population) * (1 - population)

  for _ in range(1051):
    population = (growth_rate * population) * (1 - population)

  bacteria_counts.append(population)

plt.title("Diagrama de bifurcación")
plt.plot(x_values, bacteria_counts, 'black', ls='', marker=',')
plt.xlabel("Velocidad de crecimiento (C)")
plt.ylabel("# Bacterias")
plt.show()
