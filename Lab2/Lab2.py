#Lab2.py

import sys
import regex as re

def normalize(text):
    #split by sentences
    sentences = re.findall('\p{Lu}[^\.!\!\?]*[\.\?\!]',text)
    taggedSentences = []
    #remove punctuation
    for sentence in sentences:
        sentence = sentence.lower()
        sentence = re.sub(r'(\p{P})','',sentence)
        taggedSentences.append("<s> " + sentence + " </s>")
        
    return taggedSentences

"""
A word counting program
Usage: python count.py < corpus.txt
"""
__author__ = "Pierre Nugues"

def tokenize(text):
    words = re.findall('\p{L}+', text)
    return words


def count_unigrams(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def count_bigrams(words):
    bigrams = [tuple(words[inx:inx + 2])
               for inx in range(len(words) - 1)]
    frequencies = {}
    for bigram in bigrams:
        if bigram in frequencies:
            frequencies[bigram] += 1
        else:
            frequencies[bigram] = 1
    return frequencies

def count_ngrams(words, n):
    ngrams = [tuple(words[inx:inx + n])
              for inx in range(len(words) - n + 1)]
    # "\t".join(words[inx:inx + n])
    frequencies = {}
    for ngram in ngrams:
        if ngram in frequencies:
            frequencies[ngram] += 1
        else:
            frequencies[ngram] = 1
    return frequencies

'''
end of code written by Pierre Nugues
'''

#compute sentence's probability using unigrams
def unigramProb():
    #wi = unigram
    #C(wi) = frequency of unigram
    ##words = number of words
    #P(wi) = C(w1)/#words
    #Prob. unigrams = all P(wi) multiplied together
    return 0

#compute sentence's probability using bigrams
def bigramProb():
    #wi = 1st word in bigram
    #wi+1 = 2nd word in bigram
    #Ci,i+1 = frequency of bigram
    #C(i) = frequency of 2nd word in bigram
    #P(w1+1|w1) = Ci,i+1/C(i)
    # -if not in corpus, probability of the 2nd word (see assignment)
    #Prob. bigrams = all P(w1+1|w1) multiplied together
    return 0

if __name__ == '__main__':
    text = sys.stdin.read()
    taggedSentences = normalize(text)
    text = text.lower()
    words = tokenize(text)
    frequency = count_ngrams(words,1)
    for word in sorted(frequency, key=frequency.get, reverse=True):
        print(word, '\t', frequency[word])
    