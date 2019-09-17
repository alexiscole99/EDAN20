#normalize.py

import sys
import regex as re

def tokenize(text):
    #regex \p{Lu}.+?[\.\?\!]
    #split by sentences
    sentences = re.split('\p{Lu}.+?[\.\?\!]',text)
    #remove punctuation
    sentences = re.sub(r'[^\w\s]','',sentences)
    sentences = re.sub(r'\_','',sentences)
    #convert to lowercase
    sentences = re.sub()
    #may have to split afterwards or loop through list of sentences
    