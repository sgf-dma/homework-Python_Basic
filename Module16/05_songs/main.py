violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

i_name = 0
i_duration = 1

cnt = int(input("Сколько песен выбрать? "))
total_duration = 0
for i in range(cnt):
    song = input("Название " + str(i + 1) + "-й песни: ")
    for v in violator_songs:
        if v[i_name] == song:
            total_duration += v[i_duration]
            break
    else:
        print("Нету такой песни.")

print("Общее время звучания песен:", round(total_duration, 2), "минуты")

# зачтено
