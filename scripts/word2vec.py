import os
import gensim
from gensim.models import KeyedVectors
from scripts.Preprocessor import load_corpus
from scripts.Preprocessor import write_sentences
from scripts.Preprocessor import get_list_to_train
from scripts.Preprocessor import remove_special_characters

path_to_file_to_process = "../data/corpus.txt"
path_to_processed_file = "../results/corpora/corpus-sentences.txt"
path_to_trained_model = "../results/models/trained-model.wv"

list_to_train = []

if not os.path.isfile(path_to_file_to_process) or os.stat(path_to_file_to_process).st_size == 0:
    print("The corpus is empty, please feed some data...exiting!!!")
    exit()
else:
    if not os.path.isfile(path_to_processed_file):
        print("File does not exist, writing...")
        write_sentences(remove_special_characters(load_corpus(path_to_file_to_process)), path_to_processed_file)
        print("File written to " + path_to_processed_file + "...")
        list_to_train = get_list_to_train(load_corpus(path_to_processed_file))
        print("List returned!!!")
    else:
        print("File exists in " + path_to_processed_file + "...")
        if os.stat(path_to_processed_file).st_size == 0:
            print("File is empty, writing...")
            write_sentences(remove_special_characters(load_corpus(path_to_file_to_process)), path_to_processed_file)
            print("File written, returning list...")
            list_to_train = get_list_to_train(load_corpus(path_to_processed_file))
            print("List returned!!!")
        else:
            print("File exist and not empty, returning list...")
            list_to_train = get_list_to_train(load_corpus(path_to_processed_file))
            print("List returned!!!")

model = gensim.models.Word2Vec(
    list_to_train,
    size=50,
    window=10,
    min_count=1,
    workers=10)

if not os.path.isfile(path_to_trained_model):
    print("Training in progress....")
    model.train(list_to_train, total_examples=len(list_to_train), epochs=10)
    model.wv.save(path_to_trained_model)
    print("Training Completed, saved model to " + path_to_trained_model + "!!!")
else:
    print("Trained model exists, loading...")
    model1 = KeyedVectors.load(path_to_trained_model)
    print("Model loaded, doing stuff... ;-)")
    # do stuff here with model
    print(model1.wv.most_similar(positive="rain"))
    # print(model1.similarity("rain", "cultivation"))
