def fill_list(greet, list, n):
    for i in range(n):
        x = int(input("Введите " + str(i + 1) + "-е число для " + greet + " списка: "))
        list.append(x)


list1 = []
list2 = []

fill_list("первого", list1, 3)
fill_list("второго", list2, 7)

print("Первый список:", list1)
print("Второй список:", list2)

list1.extend(list2)
for x in list1:
    while list1.count(x) - 1 > 0:
        list1.remove(x)
print(list1)

# зачтено
