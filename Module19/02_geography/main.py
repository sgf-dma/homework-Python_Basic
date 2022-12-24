n_countries = int(input("Количество стран: "))
towns = dict()
for i in range(n_countries):
    l = input(f"{i + 1}-ая страна: ").split()
    country = l[0]
    for t in l[1:]:
        towns[t] = country

for greet in ["Первый", "Второй", "Третий"]:
    t = input(f"{greet} город: ")
    if t in towns:
        print(f"Город {t} расположен в стране {towns[t]}")
    else:
        print(f"По городу {t} данных нет.")

# зачтено
