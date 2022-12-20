
def show_dict(d):
    return "\n".join([f"{k}: {v}" for k, v in d.items()])

text = input("Введите текст: ")
freq = dict()
for c in text:
    freq[c] = freq.get(c, 0) + 1

char_by_freq = dict()
for c, fr in freq.items():
    if fr not in char_by_freq:
        char_by_freq[fr] = []
    char_by_freq[fr].append(c)

print("Оригинальный словарь частот:\n", show_dict(freq), sep='')
print("Инвертированный словарь частот:\n", show_dict(char_by_freq), sep='')
