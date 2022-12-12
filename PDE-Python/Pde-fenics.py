from sympy import *

x, y, z = symbols('x y z')

# Définissez l'équation aux dérivées partielles
eq = Eq(diff(f(x, y), x, 2) + diff(f(x, y), y, 2), 0)

# Résolvez l'équation aux dérivées partielles
sol = dsolve(eq)

print(sol)



