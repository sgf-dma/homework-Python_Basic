xs = input("Первая строка: ")
zs = input("Вторая строка: ")
x = xs[0]
k = 0
while k != -1:
    if "".join([xs[-k:], xs[:-k]]) == zs:
        print(f"Первая строка получается из второй со сдвигом {k}.")
        break
    prev = k
    k = zs.find(x, prev + 1)
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")

# зачтено
