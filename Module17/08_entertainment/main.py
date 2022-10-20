
def show_str(lst):
    res = ""
    for c in lst:
        res += c
    return res

n_pins = int(input("Количество палок: "))
n_throws = int(input("Количество бросков: "))
pins = ['I' for _ in range(n_pins)]
for t in range(n_throws):
    left   = int(input("Бросок " + str(t+1) + ". Сбиты палки с номера "))
    left  -= 1
    right  = int(input("по номер "))
    right -= 1
    pins = [p if i < left or i > right else '.' for i, p in enumerate(pins)]
print("Результат:", show_str(pins))
