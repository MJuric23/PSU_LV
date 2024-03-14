file_name = "song.txt"  

word_count = {}

try:
    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
except FileNotFoundError:
    print("Datoteka '{}' nije pronađena.".format(file_name))


words_appearing_once = [word for word, count in word_count.items() if count == 1]


print("Riječi koje se pojavljuju samo jednom u datoteci:")
for word in words_appearing_once:
    print(word)


unique_words_count = len(words_appearing_once)
print("Ukupno riječi koje se pojavljuju samo jednom:", unique_words_count)
