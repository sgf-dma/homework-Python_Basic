def isalnum(string):
    return string.isalnum()


def not_isalnum(string):
    return not string.isalnum()


# Возвращает префикс списка, удовлетворяющий предикату p, и индекс начала
# оставшейся части.
def takeWhile(p, xs):
    i = 0
    for i, x in enumerate(xs):
        if not (p(x)):
            break
    else:
        i += 1
    return (xs[:i], i)


def encode(msg):
    res = []
    n = len(msg)
    k = 0
    while k < n:
        lex, i = takeWhile(isalnum, msg[k:])
        k += i
        res.append(lex[::-1])
        if k < n:
            lex, i = takeWhile(not_isalnum, msg[k:])
            k += i
        res.append(lex)
    return "".join(res)


msg = input("Сообщение: ")
res = encode(msg)
print(f"Новое сообщение: {res}")
