n_people = int(input("Кол-во человек: "))

k = int(input("Какое число в считалке? "))
# k - смещение индекса, поэтому начинается с 0.
k -= 1

people = list(range(1, n_people + 1))
i = 0
while n_people > 1:
    print("\nТекущий круг людей:", people)
    print("Начало счёта с номера", people[i])
    i = (i + k) % n_people
    print("Выбывает человек под номером", people[i])
    people.remove(people[i])
    n_people = len(people)
    i %= n_people

print("\nОстался человек под номером", people[i])

# зачтено
