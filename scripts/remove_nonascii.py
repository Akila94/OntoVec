import io
import os


path = "../data/2003_ASDA-min.txt"

# Loads the corpus into project.
def load_corpus(path):
    file = io.open(file=path, mode="r", encoding="utf8")
    txt = file.read()
    return txt


def remove_non_ascii_text(text):
    return ''.join(i for i in text if ord(i) < 128)


def remove_trailing_new_line(text):
    new_list = str(text).replace("\n", " ")
    with io.open("../results/corpora/new.txt", "w", encoding="utf8") as f:
        for s in new_list:
            f.write(s)

remove_trailing_new_line(remove_non_ascii_text(load_corpus(path)))