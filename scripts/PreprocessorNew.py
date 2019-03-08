import io
import re
# First remove non ascii characters
# The remove characters between parenthesis
# Then remove special characters, numbers. Dots in decimals etc..
# Then remove non english words (not practical in my research)
# Remove trailing new lines
# Then remove stop words
# Then formulate the word of lists.

# words = set(nltk.corpus.words.words())
#
# sent = "Io andiamo to the abcd IUPAC beach with my amico."
# print(" ".join(w for w in nltk.wordpunct_tokenize(sent) \
#          if w.lower() in words or not w.isalpha()))
# 'Io to the beach with my'

# Loads the corpus into project.
def load_corpus(path):
    file = io.open(file=path, mode="r", encoding="utf8")
    txt = file.read()
    return txt


# Removes non ascii characters
def remove_non_ascii_text(text):
    return ''.join(i for i in text if ord(i) < 128)


# Removes characters between parenthesis
def remove_characters_between_parenthesis(text):
    test = re.sub(r'\([^()]*\)', '', text)
    return test


# Removes all special characters and numbers of the corpus.
def remove_special_characters(text):
    cleaned_text = re.sub("([-–+=,_\(\){}“”’:@\"$%?&\\\/*'\"]|\s+\([0-9]+\.[0-9]+\)|\s+([0-9]+\.[0-9]+)|\d)", "", text)
    # neat_text = re.sub("([\s])", " ", cleaned_text)
    return cleaned_text


# This function gets the stop words from file.
def get_stop_words():
    stop_words_list = []
    path = "../resources/new-stop-words.txt"
    stop_words = io.open(file=path, mode="r", encoding="utf8")
    for stops in stop_words:
        stop_words_list.append(stops.rstrip("\n"))
    return stop_words_list


def remove_trailing_new_line(text):
    new_list = str(text).replace("\n", "")
    return new_list


# Remove stop words
def remove_stop_words(text):
    stop_list = get_stop_words()
    words = str(text.lower()).split(" ")
    processed_words = [w for w in words if w not in stop_list]
    joined_words = (" ").join(processed_words)
    return joined_words


# Make the list to train
def make_list(joined_words):
    list_to_train = []
    sentences_list = str(joined_words).split(".")
    for w in sentences_list:
        list_to_train.append(w.split(" "))
    return list_to_train


def preprocess(path):
    text = load_corpus(path)
    ascii_text = remove_non_ascii_text(text)
    symbol_free_text = remove_special_characters(ascii_text)
    one_lined_text = remove_trailing_new_line(symbol_free_text)
    words = remove_stop_words(one_lined_text)

    with io.open("../results/corpora/processedT.txt", 'w', encoding="utf8") as f:
        for s in words:
            f.write(s)

    final_list = make_list(words)
    return final_list
