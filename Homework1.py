from math import radians, sqrt, cos
a = float(input("Введите длину первой стороны треугольника в см: "))
b = float(input("Введите длину второй стороны треугольника в см: "))
corner = int(input("Введите угол между первой и второй стороной треугольника в градусах: "))
x = radians(corner)
c = sqrt(a**2 + b**2 - 2 * a * b * cos(x))
print("Длина третьей стороны=", c)
