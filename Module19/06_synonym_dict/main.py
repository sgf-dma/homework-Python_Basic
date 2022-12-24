vocabulary = dict()
n = int(input("Введите количество пар слов: "))
for i in range(0, n):
    w = input(f"{i + 1}-ая пара: ").split()
    if len(w) < 3:
        print("Некорректная пара")
        continue
    vocabulary[w[0].lower()] = w[2].lower()
    vocabulary[w[2].lower()] = w[0].lower()

word = input("Введите слово: ")
while word != "":
    syn = vocabulary.get(word.lower(), None)
    if not syn:
        print("Такого слова в словаре нет.")
    else:
        print("Синоним:", syn)
    word = input("Введите слово: ")

# зачтено
