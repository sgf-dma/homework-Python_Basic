
text = input("Введите строку: ").split()
longest_word = max(text, key=len)
print(f"Самое длинное слово: {longest_word}")
print(f"Длина этого слова: {len(longest_word)}")
