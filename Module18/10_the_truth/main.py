# Версия 2: для перебора всех вариантов я бы хотел использовать ограниченные
# продолжения (shift/reset) (https://okmij.org/ftp/continuations/#tutorial), с
# помощью которых можно останавливать вычисления и продолжать потом с того
# места, где остановились. Наиболее близким аналогом этого в Питоне, насколько
# мне удалось найти, являются генераторы и yield..


def shift_str(xs, k):
    k %= len(xs)
    return "".join([xs[-k:], xs[:-k]])


trans_tables = []


def ceaser_dec(word, k):
    global trans_tables
    return word.translate(trans_tables[k])


# init_tables() создаёт таблицы расшифровки для цезаря.
def init_tables():
    global trans_tables

    alphabet = []
    for c in range(97, 123):
        alphabet.append(chr(c))
    alphabet = "".join(alphabet)
    alphabet_upper = alphabet.upper()

    marks = []
    for c in range(33, 48):
        marks.append(chr(c))
    marks = "".join(marks)

    trans_tables = []
    for i, _ in enumerate(alphabet):
        t = str.maketrans(
            alphabet + alphabet_upper + marks,
            shift_str(alphabet, i) + shift_str(alphabet_upper, i) + shift_str(marks, i),
        )
        trans_tables.append(t)


# is_word() проверяет (по словарю) является ли лексема словом.
def is_word(lex):
    global all_words
    # Лексема может содержать знаки препинания, поэтому сперва надо оставить
    # только буквы.
    w = [c.lower() for c in lex if c.isalpha()]
    # Если 'w' пустая строка, тоже считаем это словом. Такое возможно, когда
    # лексема состояла только из знаков препинания, например, тире. Но тк
    # знаки препинания мы вообще не проверяем (их нет в словаре), то просто
    # возвращаем True.  (чтобы это сработало, all_words должен содержать
    # пустую строку)
    return "".join(w) in all_words


# decode_shift() расшифровывает бегущую строку.
# Если i > 0 пытаемся расшифровать с указанным смещением i, иначе перебираем
# все варианты.
def decode_shift(word, i):
    if i != -1:
        # print(f"Shifting with i={i}")
        dec = shift_str(word, i)
        if is_word(dec):
            # print(f"Found word '{dec}' at shift {i}")
            yield dec, i
        return

    # print(f"Guessing shift..")
    for i, _ in enumerate(word):
        dec = shift_str(word, i)
        # print(f"Guessing shift: i={i}: '{dec}'")
        if is_word(dec):
            # print(f"Found word '{dec}' at shift {i}")
            yield dec, i


# decode_word() расшифровывает слово, применяя цезаря и бегущую строку.
# Если смещение для цезаря k > 0 или смещения для бегущей строки i > 0,
# расшифровываем с указанными значениями, иначе перебираем все варианты.
def decode_word(word, k, i):
    global trans_tables

    if k != -1:
        dec_cs = ceaser_dec(word, k)
        # print(f"Decoding ceaser with k={k}/{i} -> {dec_cs}")
        dec, i = next(decode_shift(dec_cs, i), (None, None))
        if dec:
            yield dec, k, i
        return

    # print(f"Guessing ceaser..")
    for k, _ in enumerate(trans_tables):
        dec_cs = ceaser_dec(word, k)
        # print(f"Guessing ceaser: k={k}/{i} -> {dec_cs}")
        for dec, j in decode_shift(dec_cs, i):
            yield dec, k, j


# decode_text() расшифровывает каждую лексему (элемент) из списка.
def decode_text(text):
    result = []
    k, i = -1, -1
    for _, lex in enumerate(text):
        # Значки расшифровываем с ранее сохранённым смещением и не проверяем -
        # что получится, то и будет.
        if is_mark(lex):
            dec, _, _ = next(decode_word(lex, k, i), (None, None, None))
            if not dec:
                print(f"Can't decode '{word}'")
                return result

        # Для коротких слов или слов со знаками препинания получаем все
        # возможные варианты. Потому что часто короткие слова могут иметь
        # несколько правильных вариантов (now и own), а знаки препинания могут
        # оказаться не с той стороны, даже при правильной расшифровке
        # (.never).
        elif has_mark(lex) or len(lex) < 4:
            # Тк вариантов может быть много и выбирать из них будет другая
            # функция choose_variant(), мы не узнаем, какое смещение было у
            # выбранного варианта (и даже смогла ли она выбрать один). Поэтому
            # просто не сохраняем смещенеия.
            variants = [dec for dec, _, _ in decode_word(lex, -1, -1)]
            if variants == []:
                print(f"Can't decode '{word}'")
                return result
            dec = choose_variant(variants)

        # Длинные слова сначала расшифровываем с сохранённым смещением, если
        # не получилось, пробуем все смещения для бегущей строки, и потом все
        # смещения для цезаря и бегущей строки. Останавливаемся на первом
        # варианте.
        else:
            for ix in [[k, i], [k, -1], [-1, -1]]:
                dec, k, i = next(decode_word(lex, ix[0], ix[1]), (None, None, None))
                if dec:
                    break
            else:
                print(f"Can't decode '{word}'")
                return result

        result.append(dec)

    return result


def is_mark(lex):
    return [c for c in lex if c.isalpha()] == []


def has_mark(lex):
    return [c for c in lex if not c.isalpha()] != []


def has_title(lex):
    return [c for c in lex if c.istitle()] != []


def remove_longest_suffix(suffs, lex):
    xs = [lex.removesuffix(s) for s in suffs if lex.endswith(s)]
    if xs == []:
        return ""
    return min(xs, key=len)


def remove_longest_prefix(prefs, lex):
    xs = [lex.removeprefix(s) for s in prefs if lex.startswith(s)]
    if xs == []:
        return ""
    return min(xs, key=len)


# choose_variant() пытается угадать какие из вариантов расшифровки правильные.
# Если у неё не получается оставить один вариант, она объединит все оставшиеся
# в одну строку.
def choose_variant(variants):
    if len(variants) == 0:
        return ""

    # Различные префиксы и суффиксы со знаками препинания. После удаления
    # совпавших префиксов и суффиксов в слове должны остаться только буквы.
    prefixes = ["", "--", "*"]
    suffixes = [
        x + y + z
        for x in ["", "'s", "'re", "'m", "'ll", "n't"]
        for y in ["", ")", "*"]
        for z in ["", ".", ",", ";", ":", "!", "--"]
    ]

    vs = variants
    # Регистр букв не меняется при расшифровке, поэтому если в одном варианте
    # есть заглавная буква, то она есть и во всех остальных.
    if has_title(variants[0]):
        vs = [v for v in vs if v.istitle()]
        if len(vs) == 0:
            vs = variants

    # Значки шифруются только значками (также как буквы только буквами),
    # поэтому если значёк есть в одном из вариантов, он есть и во всех
    # остальных (но, возможно, другой).
    if has_mark(variants[0]):
        # После удаления совпавших префиксов и суффиксов в слове должны
        # остаться только буквы. Это нужно для того, чтобы отфильтровать
        # варианты с частично совпавшими префиксами или суффиксами (такие, как
        # '**right' или 'right**').
        vs = [
            v
            for v in vs
            if remove_longest_prefix(
                prefixes, remove_longest_suffix(suffixes, v)
            ).isalpha()
        ]
        if len(vs) == 0:
            vs = variants

    return "/".join(vs)


init_tables()

# Все известные слова.
f = open("./wordlist", "r")
# Пустое слово нужно, чтобы is_word() на отдельно стоящих знаках препинания,
# таких как тире, возвращал True.
all_words = [""]
for w in f:
    all_words.append(w.rstrip("\n"))

text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'.split()

res = decode_text(text)
print(f"{' '.join(res)}")
f.close()

# зачтено
