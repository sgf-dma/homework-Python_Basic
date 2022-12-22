import random

max_num = int(input("Введите максимальное натуральное число: "))

# Число, которое загадал Артём.
artem_num = random.randint(1, max_num)
print(f"Артём загадал {artem_num}")

# Количество ходов, после которых Борис сдаётся.
max_turns = random.randint(3, 5)
# Максимальное количество чисел, которые Борис называет за один раз.
guess_len = random.randint(2, 5)
print(f"max_turns={max_turns}, guess_len={guess_len}")

# Количество чисел, которые спрашивает Борис всегда должно быть меньше общего
# количества возможных вариантов, чтобы на основе ответа можно было исключить
# какие-то числа из списка возможных.
if max_num <= guess_len:
    guess_len = max_num - 1
    print(f"Reducing guess_len to {guess_len}")

# Борис просто выбирает произвольный набор чисел.
def boris_guess():
    global guess_len
    global max_num

    guesses = set()
    while len(guesses) < guess_len:
        guesses.add(random.randint(1, max_num))

    return guesses


# Если Борис будет спрашивать числа только из оставшихся возможно правильных
# вариантов, он сможет угадывать быстрее..
def boris_guess_v2(variants):
    global guess_len

    # В этом алгоритме количество возможных вариантов может быть меньше, чем
    # max_num, поэтому условие, что "количество чисел, которые спрашивает
    # Борис, всегда дожно быть меньше количества возможных вариантов"
    # проверяем каждый раз.
    if len(variants) <= guess_len:
        guess_len = len(variants) - 1
        # print(f"Reducing guess_len to {guess_len}")

    vs = list(variants)
    guesses = set()
    while len(guesses) < guess_len:
        guesses.add(random.choice(vs))

    return guesses


def ask_artem(guesses):
    return artem_num in guesses


if max_num > 1:
    possible_nums = set(range(1, max_num + 1))

    for _ in range(0, max_turns):
        print(f"Current possible nums: {possible_nums}")
        guesses = boris_guess()
        #guesses = boris_guess_v2(possible_nums)
        print(
            "Нужное число есть среди вот этих чисел: {}".format(
                " ".join([str(i) for i in guesses])
            )
        )
        yes = ask_artem(guesses)
        print(f"Ответ Артёма: {'Да' if yes else 'Нет'}")

        if yes:
            possible_nums &= guesses
        else:
            possible_nums -= guesses

        if len(possible_nums) == 1:
            boris_num = possible_nums.pop()
            if artem_num != boris_num:
                print(f"Что-то пошло не так.. {boris_num} (Борис) != {artem_num} (Артем)")
            else:
                print(f"Угадал! Это {boris_num}")
            break

    else:
        print("Нужное число есть среди вот этих чисел: Помогите!")
        print(f"Current possible nums: {possible_nums}")

else:
    print(f"Угадал! Это 1")
