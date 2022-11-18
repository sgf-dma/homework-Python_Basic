filename = input("Название файла: ")

if filename:
    if filename[0] in "@№$%^&\*()":
        print("Ошибка: название начинается на один из специальных символов.")
    elif not (filename.endswith(".txt") or filename.endswith(".docx")):
        print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")
    else:
        print("Файл назван верно.")

# зачтено
