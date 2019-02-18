import os
import gensim
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
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

# Function to display similar words
# def display_closest_words(model, word):
#     arr = np.empty((0, 300), dtype="f")
#     word_labels = [word]
#
#     # Get close words
#     close_words = model.similar_by_word(word)
#
#     # Add vectors of each similar words to array
#     arr = np.append(arr, np.array([model][word]), axis=0)
#     for word_score in close_words:
#         wrd_vector = model[word_score[0]]
#         word_labels.append(word_score[0])
#         arr = np.append(arr, np.array([wrd_vector]), axis=0)
#
#     print(arr)
#
#     # find tsne coords for 2 dimensions
#     tsne = TSNE(n_components=2, random_state=0)
#     np.set_printoptions(suppress=True)
#     Y = tsne.fit_transform(arr)
#
#     x_coords = Y[:, 0]
#     y_coords = Y[:, 1]
#
#     #display scatter plot
#     plt.scatter(x_coords, y_coords)
#
#     for label, x, y in zip(word_labels, x_coords, y_coords):
#         plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
#     plt.xlim(x_coords.min()+0.00005, x_coords.max()+0.00005)
#     plt.ylim(y_coords.min()+0.00005, y_coords.max()+0.00005)
#     plt.show()

#Method to visualize the model
# def visualize_model(model1):
#     vocab = list(model1.wv.vocab)
#     X = model1[vocab]
#     tsne = TSNE(n_components=2)
#     X_tsne = tsne.fit_transform(X)
#     df = pd.DataFrame(X_tsne, index=vocab, columns=['x', 'y'])
#     fig = plt.figure()
#     ax = fig.add_subplot(1, 1, 1)
#     ax.scatter(df['x'], df['y'])
#     for word, pos in df.iterrows():
#         ax.annotate(word, pos)
#     plt.show()


# def display_closestwords_tsnescatterplot(model, word):
#     arr = np.empty((0, 300), dtype='f')
#     word_labels = [word]
#
#     # get close words
#     close_words = model.similar_by_word(word)
#
#     # add the vector for each of the closest words to the array
#     arr = np.append(arr, np.array([model[word]]), axis=0)
#     for wrd_score in close_words:
#         wrd_vector = model[wrd_score[0]]
#         word_labels.append(wrd_score[0])
#         arr = np.append(arr, np.array([wrd_vector]), axis=0)
#
#     # find tsne coords for 2 dimensions
#     tsne = TSNE(n_components=2, random_state=0)
#     np.set_printoptions(suppress=True)
#     Y = tsne.fit_transform(arr)
#
#     x_coords = Y[:, 0]
#     y_coords = Y[:, 1]
#     # display scatter plot
#     plt.scatter(x_coords, y_coords)
#
#     for label, x, y in zip(word_labels, x_coords, y_coords):
#         plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
#     plt.xlim(x_coords.min() + 0.00005, x_coords.max() + 0.00005)
#     plt.ylim(y_coords.min() + 0.00005, y_coords.max() + 0.00005)
#     plt.show()
