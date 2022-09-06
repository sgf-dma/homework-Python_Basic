
def join_lists(xs, ys):
    i = 0
    j = 0
    z = []
    while i < len(xs) and j < len(ys):
        if xs[i] <= ys[j]:
            z.append(xs[i])
            i += 1
        else:
            z.append(ys[j])
            j += 1
    if i == len(xs):
        z.extend(ys[j:])
    else:
        z.extend(xs[i:])
    return z

height = 160
a = list(range(160, 177, 2))
b = list(range(162, 181, 3))

print("Отсортированный список учеников:", join_lists(a, b))
