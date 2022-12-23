n = int(input("Введите количество заказов: "))

orders_db = dict()
for i in range(n):
    w = input(f"{i} заказ:").split()
    person = w[0]
    pizza = w[1]
    count = w[2]
    if person not in orders_db:
        orders_db[person] = []
    orders_db[person].append({'pizza': pizza, 'count': int(count)})
print(orders_db)

for person, orders in orders_db.items():
    print(f"{person}:")
    count_by_pizza = dict()
    for order in orders:
        pizza = order['pizza']
        count_by_pizza[pizza] = count_by_pizza.get(pizza, 0) + order['count']
    for pizza in sorted(count_by_pizza):
        print(f"\t{pizza}: {count_by_pizza[pizza]}")

