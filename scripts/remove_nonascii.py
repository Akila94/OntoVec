import io
import os


path = "../data/non-ascii-corpus.txt"

# Loads the corpus into project.
def load_corpus(path):
    file = io.open(file=path, mode="r", encoding="utf8")
    txt = file.read()
    return txt


def remove_non_ascii_text(text):
    return ''.join(i for i in text if ord(i) < 128)


def remove_trailing_new_line(text):
    new_list = str(text).replace("\n", " ")
    print(new_list)


print(remove_trailing_new_line(remove_non_ascii_text(load_corpus(path))))