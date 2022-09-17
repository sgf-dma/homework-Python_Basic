n_skates = int(input("Кол-во коньков: "))
skates = []
for i in range(n_skates):
    x = int(input("Размер " + str(i + 1) + "-й пары: "))
    skates.append(x)

n_foots = int(input("Кол-во людей: "))
foots = []
for i in range(n_foots):
    x = int(input("Размер ноги " + str(i + 1) + "-го человека: "))
    foots.append(x)

skates.sort()
n_people = 0
for foot in foots:
    for skate in skates:
        if foot <= skate:
            skates.remove(skate)
            n_people += 1
            break

print("Наибольшее кол-во людей, которые могут взять ролики:", n_people)

# зачтено
