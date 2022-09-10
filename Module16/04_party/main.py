
def elem(y, xs):
    for x in xs:
        if x == y:
            return True
    return False

def work(reply):
    if reply == "пришёл":
        guest = input("Имя гостя: ")
        if len(guests) >= 6:
            print("Прости, ", guest, ", но мест нет.", sep='')
            return True
        guests.append(guest)
        print("Привет,", guest)
    elif reply == "ушёл":
        guest = input("Имя гостя: ")
        if not elem(guest, guests):
            print("Такого гостя не было.")
            return True
        guests.remove(guest)
        print("Пока,", guest)
    elif reply == "Пора спать":
        print("Вечеринка закончилась, все легли спать.")
        return False
    else:
        print("Не понимаю о чём речь..")
    return True

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

cont = True
while cont == True:
    print("Сейчас на вечеринке", len(guests), "человек:", guests)
    reply = input("Гость пришёл или ушёл? ")
    cont = work(reply)
    print()

