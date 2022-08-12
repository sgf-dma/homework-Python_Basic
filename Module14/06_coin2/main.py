
def in_circle(r, x, y):
    return x*x + y*y <= r*r

print("Введите координаты монетки:")
x = float(input("X: "))
y = float(input("Y: "))
r = float(input("Введите радиус: "))

if in_circle(r, x, y):
    print("Монетка где-то рядом")
else:
    print("Монетки в области нет")
