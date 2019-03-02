import io
import re
from collections import Counter
import nltk.data


# Loads the corpus into project.
def load_corpus(path):
    file = io.open(file=path, mode="r", encoding="utf8")
    txt = file.read()
    return txt


# Removes all special characters and numbers of the corpus.
def remove_special_characters(text):
    cleaned_text = re.sub("([-–,_\(\){}“”’:@\"$%?&\\\/*'\"]|\s+\([0-9]+\.[0-9]+\)|\s+([0-9]+\.[0-9]+)|\d)", "", text)
    # neat_text = re.sub("([\s])", " ", cleaned_text)
    return cleaned_text


# This function creates a domain specific stop words list
# by stripping most frequent and least frequent words.
# def make_stop_words_list(txt):
#     clean_text = remove_special_characters(txt)
#     words = []
#     counter = Counter(clean_text.lower().split())
#     # Most frequent 20% words
#     words.append(counter.most_common(1133))
#     # Least frequent 20% words
#     words.append(counter.most_common()[:-1134:-1])
#     path = "../resources/my-domain-specific-stopwords.txt"
#     # Sorting the words according to the frequency
#     sorted_keys = sorted(counter, key=counter.get, reverse=True)

# with io.open(path, 'w', encoding="utf8") as f:
#     for item in sorted_keys:
#         #Using rstrip for removing trailing dots.
#         f.write("%s\n" % item.rstrip('.'))

# This function gets the stop words from file.
def get_stop_words():
    stop_words_list = []
    path = "../resources/new-stop-words.txt"
    stop_words = io.open(file=path, mode="r", encoding="utf8")
    for stops in stop_words:
        stop_words_list.append(stops.rstrip("\n"))
    return stop_words_list


# Splittes the sentences of the corpus.
def write_sentences(preprocessed_text, path):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    processed_sentences = list('\n'.join(tokenizer.tokenize(preprocessed_text)))
    # print(sentences)
    # Writing sentences to file
    with io.open(path, 'w', encoding="utf8") as f:
        for s in processed_sentences:
            f.write(s)


# def remove_stop_words(sentence):
#     stop_list = get_stop_words()
#     words = str(sentence).split(" ")
#     clean_words = [w for w in words if w not in stop_list]
#     new_sentences = (" ").join(clean_words)
#     return new_sentences


def get_list_to_train(text):
    list_to_train = []
    words = str(text.lower()).split(" ")
    stop_list = get_stop_words()
    processed_words = [w for w in words if w not in stop_list]
    joined_words = (" ").join(processed_words)
    sentences_list = joined_words.split(".")
    for w in sentences_list:
        list_to_train.append(w.split(" "))
    print(list_to_train)
    return list_to_train

# get_list_to_train(load_corpus("AgriCorpusSentences"))
# write_sentences(remove_special_characters(load_corpus("AgriCorpus")))