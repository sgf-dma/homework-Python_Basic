inp = input("Введите строку: ")
char_count = dict()
for c in inp:
    char_count[c] = char_count.get(c, 0) + 1

odd_chars = [x for x in char_count.values() if x % 2 != 0]
if len(odd_chars) < 2:
    print("Можно сделать палиндромом")
else:
    print("Нельзя сделать палиндромом")
