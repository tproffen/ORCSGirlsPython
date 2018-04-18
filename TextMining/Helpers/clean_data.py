
def remove_special_characters(word):
    good_characters = []
    for character in word:
        if character.isalpha() or character.isspace() or character == "'":
            good_characters.append(character)
    return ''.join(good_characters)


def remove_stopwords(words):
    with open('Data/stopwords.txt') as stopwords_file:
        stopwords = stopwords_file.read().split()
    no_stopwords = []
    for word in words:
        if word not in stopwords and word:
            no_stopwords.append(word)
    return no_stopwords


def get_word_pairs(words):
    pairs = list(zip(words, words[1:]))
    return [pair[0] + ' ' + pair[1] for pair in pairs]
