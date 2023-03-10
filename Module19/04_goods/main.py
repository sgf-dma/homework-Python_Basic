goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


def sum_total(lst):
    count = 0
    price = 0
    for el in lst:
        count += el['quantity']
        price += el['quantity'] * el['price']
    return count, price


for name, gid in goods.items():
    count, price = sum_total(store[gid])
    print(f"{name} - {count} штук, стоимость {price:,} рубля")

# зачтено
