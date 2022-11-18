def shift_str(xs, k):
    k %= len(xs)
    return "".join([xs[-k:], xs[:-k]])


def ceaser_dec(word, k):
    global trans_tables
    return word.translate(trans_tables[k])


def decode_shift(word, i):
    if i != -1:
        print(f"Shifting with i={i}")
        dec = shift_str(word, i)
        if is_word(dec):
            print(f"Found word '{dec}' at shift {i}")
            return dec, i
    else:
        print(f"Guessing shift..")
        for i, _ in enumerate(word):
            # print(f"Guessing shift: i={i}")
            dec = shift_str(word, i)
            if is_word(dec):
                print(f"Found word '{dec}' at shift {i}")
                return dec, i
    return None, -1


def decode_word(word, k, i):
    global trans_tables
    if k != -1:
        print(f"Decoding ceaser with k={k}")
        dec, i = decode_shift(ceaser_dec(word, k), i)
        if dec:
            return dec, k, i
    else:
        print(f"Guessing ceaser..")
        for k, _ in enumerate(trans_tables):
            dec = ceaser_dec(word, k)
            print(f"Guessing ceaser: k={k} -> {dec}")
            dec, i = decode_shift(dec, i)
            if dec:
                return dec, k, i
    return None, -1, -1


def is_word(word):
    global all_words
    w = [c.lower() for c in word if c.isalpha()]
    if w:
        return "".join(w) in all_words
    else:
        return True


def decode_text(text):
    result = []
    dec, k, i = decode_word(text[0], -1, -1)
    result.append(dec)
    for _, word in enumerate(text[1:]):
        for ix in [[k, i], [k, -1], [-1, -1]]:
            dec, k, i = decode_word(word, ix[0], ix[1])
            if dec:
                break
        else:
            print(f"Can't decode '{word}'")
            return result
        result.append(dec)
    return result


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

    # Таблицы для str.translate().
    trans_tables = []
    for i, _ in enumerate(alphabet):
        t = str.maketrans(
            alphabet + alphabet_upper + marks,
            shift_str(alphabet, i) + shift_str(alphabet_upper, i) + shift_str(marks, i)
        )
        trans_tables.append(t)

init_tables()

# Все слова.
f = open("./wordlist", "r")
all_words = []
for w in f:
    # В .dic файлах hunspell-а после / указаны какие-то буквы. И хотя в
    # результате я взял другой файл, но пусть разделение останется..
    w = w.rstrip("\n").split("/")[0]
    all_words.append(w)

text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'.split()
#text = 'Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ '.split()

res = decode_text(text)
print(f"{' '.join(res)}")
f.close()
