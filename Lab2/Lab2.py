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
def unigramProb(unigramFreq,testText,numWords):
    print("Unigram model")
    print("=====================================================")
    print("wi C(wi) #words P(wi)")
    print("=====================================================")
    sentence = normalize(testText)[0]
    words = tokenize(sentence)
    words = words[1:-1]
    #words[0] = "<s>"
    #words[-1] = "</s>"
    #print(words)
    prob = {}
    cwi = 0
    for word in words:
        if(word not in unigramFreq):
            continue
        cwi = unigramFreq[word]
        prob[word] = float(cwi)/numWords
        print(word,cwi,numWords,prob[word])

    print("=====================================================")
    probUni = 1
    for key in prob:
        probUni *= prob[key]
    print("Prob. unigrams:   ",probUni)

    return prob
    #wi = unigram
    #C(wi) = frequency of unigram
    ##words = number of words
    #P(wi) = C(wi)/#words
    #Prob. unigrams = all P(wi) multiplied together

#compute sentence's probability using bigrams
def bigramProb(bigramFreq, unigramFreq, testText, uniProb):
    print("Bigram model")
    print("=====================================================")
    print("wi wi+1 Ci,i+1 C(i) P(wi+1|wi)")
    print("=====================================================")
    sentence = normalize(testText)[0]
    words = tokenize(sentence)
    words = words[1:-1]
    #words[0] = "<s>"
    #words[-1] = "</s>"
    testBFreq = count_bigrams(words)
    freqOfBigram = 0
    ci = 0
    prob = {}
    alternateProbs = []
    for key in testBFreq:
        if key not in bigramFreq:
            freqOfBigram = 0
            ci = unigramFreq[key[0]]
            prob[key] = "0.0 *backoff: " + str(uniProb[key[1]])
            alternateProbs.append(uniProb[key[1]])
            print(key[0],key[1],freqOfBigram,ci, prob[key])
        else:
            freqOfBigram = bigramFreq[key]
            ci = unigramFreq[key[0]]
            prob[key] = float(freqOfBigram)/ci
            print(key[0],key[1],freqOfBigram,prob[key])
    print("=====================================================")
    probBi = 1
    for key in prob:
        #print(prob[key])
        if(type(prob[key])==float):
            probBi *= prob[key]
    for i in alternateProbs:
        probBi*=i
    print("Prob. bigrams:   ",probBi)


    #wi = 1st word in bigram
    #wi+1 = 2nd word in bigram
    #Ci,i+1 = frequency of bigram
    #C(i) = frequency of 1st word in bigram
    #P(w1+1|w1) = Ci,i+1/C(i)
    # -if not in corpus, probability of the 2nd word (see assignment)
    #Prob. bigrams = all P(w1+1|w1) multiplied together
    return prob

if __name__ == '__main__':
    text = sys.stdin.read()
    taggedSentences = normalize(text)
    text = text.lower()
    words = tokenize(text)
    numWords = len(words)
    unigramFrequency = count_unigrams(words)
    bigramFrequency = count_bigrams(words)
    #print(unigramFrequency.keys())
    testText = "Det var en gång en katt som hette Nils."
    '''for word in sorted(frequency, key=frequency.get, reverse=True):
        print(word, '\t', frequency[word])'''
    up = unigramProb(unigramFrequency,testText,numWords)
    print()
    bp = bigramProb(bigramFrequency,unigramFrequency,testText,up)
    