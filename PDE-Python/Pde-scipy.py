import numpy as np
from scipy.pde import pdeint

# Définissez les limites de la zone de calcul
xmin, xmax = -1, 1
ymin, ymax = -1, 1

# Définissez les conditions aux limites
def bc(ya, yb):
    return ya[0], yb[0]

# Définissez l'équation différentielle
def f(x, y, z):
    return x**2 + y**2 + z

# Résolvez l'équation de Laplace
x, y, z = pdeint(f, bc, xmin, xmax, ymin, ymax)
