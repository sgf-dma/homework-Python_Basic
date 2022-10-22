lst = input("Введите строку: ")

h_ixs = [i for i, c in enumerate(lst) if c == 'h']
h_between = lst[h_ixs[-1] - 1:h_ixs[0]:-1]
print("Развёрнутая последовательность между первым и последним h:", h_between)

# зачтено
