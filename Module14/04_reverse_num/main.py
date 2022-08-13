def reverse_str(s):
    rev_s = ''
    for c in s:
        rev_s = c + rev_s
    return rev_s


def drop_leading_zeros(s):
    s1 = ''
    nonzero = False
    for c in s:
        if not nonzero:
            if c == '0':
                continue
            else:
                nonzero = True
        s1 += c
    if s1 == '':
        s1 = "0"
    return s1


# Для целого числа нули в начале не имеют значения. Для дробного - наоборот,
# нули в конце не имеют значения. Поэтому если удалять нули просто
# преобразованием в int, то у дробной части он удалит нули не с того конца.
def reverse_float(n_str):
    rev_z = 0
    rev_dec = 0
    dot_found = False
    cur = ''
    for c in n_str:
        if c == '.':
            rev_z = int(reverse_str(drop_leading_zeros(cur)))
            dot_found = True
            cur = ''
            continue
        cur += c
    else:
        if dot_found:
            rev_dec = float("0." + drop_leading_zeros(reverse_str(cur)))
        else:
            rev_z = int(reverse_str(drop_leading_zeros(cur)))
    return rev_z + rev_dec


n1 = input("Введите перве число: ")
n2 = input("Введите второе число: ")

rev_n1 = reverse_float(n1)
print("Первое число наоборот:", rev_n1)

rev_n2 = reverse_float(n2)
print("Второе число наоборот:", rev_n2)

print("Сумма:", rev_n1 + rev_n2)

# зачтено
