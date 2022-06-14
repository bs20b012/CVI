import torch
import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

# function to tokenize or break a sentence into words
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

# function to lower all words and stem them
def stem(word):
    return stemmer.stem(word.lower())

#
def bag_of_words(tokenized_sentence,all_words):
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx,w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx]=1
    return bag

