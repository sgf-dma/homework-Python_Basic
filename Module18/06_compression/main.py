text = input("Введите строку: ")

zipped = []
if text:
    prev = text[0]
    n = 0
    for c in text:
        if c == prev:
            n += 1
        else:
            zipped.append(''.join([prev, str(n)]))
            n = 1
            prev = c
    zipped.append(''.join([prev, str(n)]))
print(''.join(zipped))
