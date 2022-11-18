while True:
    pw = input("Придумайте пароль: ")
    if (
            len(pw) > 7
            and len([c for c in pw if c.isupper()]) > 0
            and len([c for c in pw if c.isdigit()]) > 2
    ):
        print("Это надёжный пароль!")
        break
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")

# зачтено
