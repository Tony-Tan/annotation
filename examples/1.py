# # Quadratic Formula
#
# This section demonstrates the use of the quadratic formula:
#
#
# $$
# x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
# $$
#
# It solves equations of the form $ ax^2 + bx + c = 0 $.
# This section demonstrates the use of the quadratic formula:
#
#
# $$
# x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
# $$
#
# It solves equations of the form $ ax^2 + bx + c = 0 $.
# This section demonstrates the use of the quadratic formula:
#
#
# $$
# x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
# $$
#
# It solves equations of the form $ ax^2 + bx + c = 0 $.
import math


def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print("No real roots.")
        return None

    # Calculate the two roots using the quadratic formula
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)



    return (root1, root2)


# Example Usage
# Let's solve the equation $ 2x^2 + 3x - 2 = 0 $
a = 2
b = 3
c = -2

roots = solve_quadratic(a, b, c)
print("The roots of the equation are:The roots of the equation are:The roots of the equation are:The roots of the equation are:The roots of the equation are:The roots of the equation are:The roots of the equation are:", roots)


# Example Usage
# Let's solve the equation $ 2x^2 + 3x - 2 = 0 $
