#normalize.py

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

if __name__ == '__main__':
    text = sys.stdin.read()
    taggedSentences = normalize(text)
    for s in taggedSentences:
        print(s)
    