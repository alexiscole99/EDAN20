#normalize.py

import sys
import regex as re

def tokenize(text):
    #regex \p{Lu}.+?[\.\?\!]
    #split by sentences
    sentences = re.split('\p{Lu}.+?[\.\?\!]',text)
    #remove punctuation
    for sentence in sentences:
        #sentence = re.sub(r'\n','', sentence)
        sentence = re.sub(r'[^\w]','',sentence)
        #sentence = re.sub(r'\_','',sentence)
    #convert to lowercase
    #sentences = re.sub()
    #may have to split afterwards or loop through list of sentences
    return sentences

if __name__ == '__main__':
    text = sys.stdin.read()
    sentences = tokenize(text)
    print(sentences)
    #for sentence in sentences:
    #    print(sentence)
    