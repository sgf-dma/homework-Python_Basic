n_friends = int(input("К-во друзей: "))
friends_balance = [0] * n_friends
n_debts = int(input("Долговых расписок: "))

i_from = 0
i_to = 1
i_amount = 2
debt_bills = []
for i in range(n_debts):
    print("\n", i + 1, "-я расписка", sep='')
    v_to = int(input("Кому: "))
    if v_to < 1 or v_to > n_friends:
        print("Нету такого друга")
        continue
    v_from = int(input("От кого: "))
    if v_from < 1 or v_from > n_friends:
        print("Нету такого друга")
        continue
    v_amount = int(input("Сколько: "))
    debt_bills.append([v_from - 1, v_to - 1, v_amount])

for bill in debt_bills:
    friends_balance[bill[i_from]] += bill[i_amount]
    friends_balance[bill[i_to]] -= bill[i_amount]

print("Баланс друзей:")
for i in range(n_friends):
    print(i + 1, ": ", friends_balance[i], sep='')

# зачтено
