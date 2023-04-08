import numpy as np
import matplotlib.pyplot as plt
import random as rnd
rho = 0.9
k = 1000
D = 5
N = 1000
G = {}
X = np.zeros(k)
for _ in range(N): X[rnd.randint(0, k - 1)] += 1
for i in range(k):
  G[i] = {}
  for j in range(k):
    if j != i and rnd.uniform(0, 1) < rho:
      l = rnd.randint(0, k - 1)
      while i == l or j == l: l = rnd.randint(0, k - 1)
      G[i][j] = l
X = list(X.astype(int))
for y in range(11):
  while np.sum(X) < 2*N:
    for z in range(D):
      i, j = np.random.choice(k, 2, p=X/np.sum(X))
      if j in G[i] and rnd.uniform(0, 1) < rho and X[i] > 0:
        X[i] -= 1
        X[G[i][j]] += 1
    X[0] += 1
  r = rnd.uniform(0, 1)
  X = [int(x*r) for x in X]
X = sorted(X, reverse=True)
plt.plot(range(1, k + 1), X)
plt.xscale("log")
plt.xlim(1, k)
plt.yscale("log")
plt.show()
