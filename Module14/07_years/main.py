def bad_years(year_start, year_end):
    if year_start > year_end or year_start < 1000 or year_end > 9999:
        print("Неправильный диапазон годов")
        return

    s0 = year_start // 100
    s1 = year_end // 100
    for y in range(s0, s1 + 1):
        a = y % 10
        b = y // 10
        if a != b:
            bad_years = [y * 100 + a * 10 + a, y * 100 + b * 10 + b]
        else:
            bad_years = [y * 100 + a * 10 + a]
        for year in bad_years:
            if year < year_start:
                continue
            if year > year_end:
                return
            print(year)


year_start = int(input("Введите первый год: "))
year_end = int(input("Введите второй год: "))

bad_years(year_start, year_end)

# зачтено
