
def elem(c, list):
    return len([x for x in list if x == c]) > 0

text = input("Введите текст: ")
vowels = "аеёиыоуэюя"

text_vowels = [c for c in text if elem(c, vowels)]
print("Список гласных букв:", text_vowels)
print("Длина списка:", len(text_vowels))
