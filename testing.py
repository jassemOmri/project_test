import cmath  # Module pour manipuler les nombres complexes

def solve_cubic_equation(a, b, c, d):
    # Coefficients de l'équation cubique : ax^3 + bx^2 + cx + d = 0

    # Calcul du discriminant et des termes intermédiaires
    delta1 = b**2 - 3*a*c
    delta2 = 2*b**3 - 9*a*b*c + 27*a**2*d
    delta = delta2**2 - 4*delta1**3

    # Calcul des racines
    C = ((delta2 + cmath.sqrt(delta)) / 2)**(1/3)
    u1 = -1 + 1j * cmath.sqrt(3)
    u2 = -1 - 1j * cmath.sqrt(3)

    root1 = (-1 / (3 * a)) * (b + C + delta1 / C)
    root2 = (-1 / (3 * a)) * (u1 * (b + C) + u2 * delta1 / C)
    root3 = (-1 / (3 * a)) * (u2 * (b + C) + u1 * delta1 / C)

    return root1, root2, root3

# Exemple d'équation cubique : x^3 - 6x^2 + 11x - 6 = 0
a = 1
b = -6
c = 11
d = -6

solutions = solve_cubic_equation(a, b, c, d)

print("Solutions:", solutions)