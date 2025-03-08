import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x):
    return r * x * (1 - x)

def plot_population_evolution(ax, r, x0, n_iterations):
    x_values = [x0]
    x = x0
    for _ in range(n_iterations):
        x = logistic_map(r, x)
        x_values.append(x)
    
    ax.plot(range(n_iterations + 1), x_values, '-o')
    ax.set_title(f'Evolución de la Población (r={r})')
    ax.set_xlabel('Tiempo (iteraciones)')
    ax.set_ylabel('Población')

if __name__ == "__main__":
    r_values = [1, 2, 3, 3.99]
    x0 = 0.5
    n_iterations = 100

    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    axs = axs.flatten()

    for i, r in enumerate(r_values):
        plot_population_evolution(axs[i], r, x0, n_iterations)

    plt.tight_layout()
    plt.show()
    fig.savefig('./logistic.png')