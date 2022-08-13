def min_divider(n):
    if n <= 1:
        print("Число должно быть больше или равно 1")
        return 0
    for d in range(2, n + 1):
        if n % d == 0:
            return d


n = int(input("Введите число: "))
print("наименьший делитель, отличный от единицы:", min_divider(n))

# зачтено
