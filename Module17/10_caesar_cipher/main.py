alphabet_low = "абвгдеёжзийклмнопрстуфхцчшщыэюя"
alphabet_up = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯ"


def elem(c, lst):
    return len([x for x in lst if x == c]) > 0


def show_str(lst):
    res = ""
    for c in lst:
        res += c
    return res


def ceaser_code_v1(direction, shift, c):
    alpha = []
    if elem(c, alphabet_low):
        alpha = alphabet_low
    elif elem(c, alphabet_up):
        alpha = alphabet_up

    if alpha:
        shift %= len(alpha)
        return alpha[(alpha.index(c) + direction * shift) % len(alpha)]
    else:
        return c


# Наверно, очень неэффективно, зато много slice-ов.
def ceaser_code_v2(direction, shift, c):
    alpha = []
    if elem(c, alphabet_low):
        alpha = alphabet_low[::direction]
    elif elem(c, alphabet_up):
        alpha = alphabet_up[::direction]

    if alpha:
        shift %= len(alpha)
        if shift != 0:
            return (alpha * 2)[alpha.index(c)::shift][1]
        else:
            return c
    else:
        return c


def encode(shift, c):
    r1 = ceaser_code_v1(+1, shift, c)
    r2 = ceaser_code_v2(+1, shift, c)
    if r1 != r2:
        print("Что-то пошло не так при кодировании..")
        return
    else:
        return r1


def decode(shift, c):
    r1 = ceaser_code_v1(-1, shift, c)
    r2 = ceaser_code_v2(-1, shift, c)
    if r1 != r2:
        print("Что-то пошло не так при декодировании..")
        return
    else:
        return r1


shift = int(input("Введите сдвиг: "))
# msg = "это питон"
msg = input("Введите сообщение: ")
enc_msg = [encode(shift, c) for c in msg]
if list(msg) != [decode(shift, c) for c in enc_msg]:
    print("Ваше сообщение потрачено..")

print(show_str(enc_msg))

# зачтено
