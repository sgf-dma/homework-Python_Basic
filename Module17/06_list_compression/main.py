
import random

lst = [0, 2, 1, 0, 0, 0, 1, 0, 2, 0]
n = int(input("Количество чисел в списке: "))
lst = [random.randint(0, 2) for _ in range(n)]
print("Список до сжатия:", lst)

# Closure, добавляющая ноль к результату предыдущий функции. По сути,
# композиция функций, добавляющих ноль.
def app_zero(k):
    def g(lst):
        k(lst).append(0)
        return lst
    return g

# Начинаем с identity, просто возвращающей свой аргумент.
def h(lst):
    return lst
result = []
for x in lst:
    if x != 0:
        result.append(x)
    else:
        h = app_zero(h)

result = h(result)
print("Список после перестановки нулей:", result)
print("Список после сжатия:", [x for x in result if x != 0])
