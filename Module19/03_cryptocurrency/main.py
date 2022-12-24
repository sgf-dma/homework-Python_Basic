data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4,
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False,
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0,
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False,
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0,
        },
    ],
}


# Функция call_formatter() ищет подходящий для данного типа formatter в
# словаре и вызывает его.
def call_formatter(path, v):
    global type_formatters

    ty = type(v).__name__
    fmt, show = type_formatters.get(ty, None)
    if not fmt:
        print(f"Unknown type {ty}")
        return []
    return fmt(path, show, v)


# Форматирование базовых типов, вроде int, str и bool. Функция show принимает
# префикс и значение и выводит список результатов.
def format_prim(path, show, v):
    return show(path, v)


# Функция show для format_prim(), которая выводит значение.
def show_val(path, v):
    return [path + "=" + str(v)]


# Функция show для format_prim(), которая выводит значение без ключей.
def show_val_no_key(_, v):
    return [str(v)]


# Функция show для format_prim(), которая ничего не выводит.
def no_show_val(*_):
    return []


# Функция show для format_prim(), которая выводит путь текущего значения.
def show_path(path, _):
    return [path]


# Функция traverse_iter() идёт по итератору, вызывая функцию show_key для
# каждого ключа. Функция show_key принимает префикс и ключ и выводит новый
# префикс и отформатированную строчку для этого ключа.
def traverse_iter(path, show_key, enum):
    res = []
    for k, v in enum:
        new_path, n = show_key(path, k)
        if n:
            res.append(n)
        res.extend(call_formatter(new_path, v))
    return res


# Функция show_key для traverse_iter(), которая выводит ключ.
def show_iter_key(path, k):
    new_path = path + f"[{k}]"
    name = new_path
    return new_path, name


# Функция show_key для traverse_iter(), которая ничего не выводит.
def no_show_iter_key(path, k):
    new_path = path + f"[{k}]"
    return new_path, None


# Форматирование списков. Элементы списков не имеют ключей, поэтому мы их не
# выводим.
def format_list(path, _, lst):
    return traverse_iter(path, no_show_iter_key, enumerate(lst))


# Форматирование словарей. Тк для самого словаря ничего выводить не надо, то
# этот formatter просто принимает функцию show_key, которая нужна для
# traverse_iter().
def format_dict(path, show_key, d):
    return traverse_iter(path, show_key, d.items())


type_formatters = dict()

fmt_all_keys = {
    "int": (format_prim, no_show_val),
    "str": (format_prim, no_show_val),
    "bool": (format_prim, no_show_val),
    "dict": (format_dict, show_iter_key),
    "list": (format_list, show_iter_key),
}

type_formatters = fmt_all_keys
print("1. Все ключи:\n{}".format("\n".join(call_formatter("data", data))))
print()

fmt_all_leaf_keys = {
    "int": (format_prim, show_path),
    "str": (format_prim, show_path),
    "bool": (format_prim, show_path),
    "dict": (format_dict, no_show_iter_key),
    "list": (format_list, no_show_iter_key),
}

type_formatters = fmt_all_leaf_keys
print("или только конечные ключи:\n{}".format("\n".join(call_formatter("data", data))))
print()

fmt_all_values = {
    "int": (format_prim, show_val_no_key),
    "str": (format_prim, show_val_no_key),
    "bool": (format_prim, show_val_no_key),
    "dict": (format_dict, no_show_iter_key),
    "list": (format_list, no_show_iter_key),
}

type_formatters = fmt_all_values
print("2. Все значения:\n{}".format("\n".join(call_formatter("data", data))))
print()

fmt_all_values = {
    "int": (format_prim, show_val),
    "str": (format_prim, show_val),
    "bool": (format_prim, show_val),
    "dict": (format_dict, no_show_iter_key),
    "list": (format_list, no_show_iter_key),
}

type_formatters = fmt_all_values
print("или все значения с ключами:\n{}".format("\n".join(call_formatter("data", data))))
print()

data["tokens"][0]["fst_token_info"]["name"] = "doge"
print(
    "3. [fst_token_info][name] = {}\n".format(
        data["tokens"][0]["fst_token_info"]["name"]
    )
)

data["ETH"]["total_out"] = data["tokens"][0]["total_out"]
data["tokens"] = [
    {k: v for k, v in tok.items() if k != "total_out"} for tok in data["tokens"]
]
print(
    "4. ['ETH']['total_out'] = {}, data[tokens] = {}\n".format(
        data["ETH"]["total_out"], [v.keys() for v in data["tokens"]]
    )
)

data["tokens"][1]["sec_token_info"]["new_price"] = data["tokens"][1][
    "sec_token_info"
].pop("price")
print("5. ['sec_token_info'] = {}".format(data["tokens"][1]["sec_token_info"].keys()))

# зачтено
