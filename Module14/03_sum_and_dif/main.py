
def sum_digits(n):
    summ = 0
    while n > 0:
        summ += n % 10
        n = n // 10
    return summ

def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

n = int(input("Введите целое положительное число: "))

if n < 0:
    print("Число должно быть положительное.")
else:
    summ = sum_digits(n)
    count = count_digits(n)
    print("Сумма чисел:", summ)
    print("Количество цифр в числе:", count)
    print("Разность суммы и количества цифр:", summ - count)
