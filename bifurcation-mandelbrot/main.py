import matplotlib.pyplot as plt
import numpy as np
S=np.linspace(0.7,4,240000) # 240000

X = []
C = []

for s in S:

    X.append(s)

    m = np.random.random()
    for n in range(1001):
      m=(s*m)*(1-m)

    for l in range(1051):
      m=(s*m)*(1-m)

    C.append(m)

plt.title("Diagrama de bifurcación")

plt.plot(X, C, 'black' ,ls='', marker=',')
plt.xlabel("Velocidad de crecimiento (C)")
plt.ylabel("# Bacterias")
plt.show()