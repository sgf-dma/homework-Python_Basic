n = int(input("Введите количество человек: "))

gen_tree = dict()
for i in range(n):
    ws = input(f"{i + 1}-ая пара: ").split()
    child = ws[0]
    parent = ws[1]
    # print(child, parent)
    if parent not in gen_tree:
        gen_tree[parent] = []
    gen_tree[parent].append(child)

# print(gen_tree)

childs = [y for xs in gen_tree.values() for y in xs]
parents = gen_tree.keys()
rs = set(parents) - set(childs)
if len(rs) != 1:
    print(f"Несколько родоначальников.. {rs}")
else:
    root = rs.pop()
    # print(root)

    height = 0
    gen_height = dict()
    childs = [root]
    while childs != []:
        new_childs = []
        for y in childs:
            gen_height[y] = height
            new_childs.extend(gen_tree.get(y, []))
        height += 1
        childs = new_childs

    print("Высота каждого члена семьи:")
    print("\n".join([f"{name} {h}" for name, h in sorted(gen_height.items())]))

# зачтено
