
# Возвращает список с указанным количеством элементов с начала списка (> 0) или с конца (< 0).
def take(list, n):
    result = []
    if n > 0:
        for i, v in enumerate(list):
            if i < n:
                result.append(v)
    else:
        for i in range(max(0, len(list) + n), len(list)):
            result.append(list[i])
    return result

def reverse(list):
    result = []
    for i in range(len(list) - 1, -1, -1):
        result.append(list[i])
    return result

# Возвращает "есть симметрия" (True и пустые head и tail), "частичная
# симметрия" (True и непустой head или tail с недостающими элементами) или
# "нет симметрии" (False).
# i <= j, i всегда двигается к началу списка, j - к концу.
def find_symmetry(list, i, j):
    head = []
    tail = []
    if i > j:
        return False, head, tail
    #print(i, j)
    while i >= 0 and j < len(list):
        if list[i] != list[j]:
            return False, head, tail
        i -= 1
        j += 1
        #print(i, j)
    if i >= 0:
        tail = reverse(take(list, i + 1))
    if j < len(list):
        head = reverse(take(list, 0 - (len(list) - j)))
    return True, head, tail

def symmetry_tail(list):
    j = len(list) // 2
    found = False
    if len(list)%2 == 0:
        i = j - 1
        found, head, tail = find_symmetry(list, i, j)
        #print(found, head, tail)
        if found:
            return tail

    while True:
        i = j
        found, head, tail = find_symmetry(list, i, j)
        #print(found, head, tail)
        if found:
            return tail

        j += 1
        found, head, tail = find_symmetry(list, i, j)
        #print(found, head, tail)
        if found:
            return tail

def symmetry_head(list):
    j = len(list) // 2
    i = j
    found = False
    if len(list)%2 == 0:
        i -= 1
        found, head, tail = find_symmetry(list, i, j)
        #print(found, head, tail)
        if found:
            return head

    while True:
        j = i
        found, head, tail = find_symmetry(list, i, j)
        #print(found, head, tail)
        if found:
            return head

        i -= 1
        found, head, tail = find_symmetry(list, i, j)
        #print(found, head, tail)
        if found:
            return head

n = int(input("Кол-во чисел: "))
list = []
for _ in range(n):
    x = int(input("Число: "))
    list.append(x)

print()
print("Последовательность:", list)
tail = symmetry_tail(list)
if tail:
    print("Нужно прписать чисел:", len(tail))
    print("Сами числа:", tail)
else:
    print("Последовательность симметрична.")
