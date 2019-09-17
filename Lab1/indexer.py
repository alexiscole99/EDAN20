# Alexis Cole and Jonathan Moran
# Lab1

import regex as re
import pickle
import os 
import sys 
import math
import numpy as np
from numpy import linalg as npla

#read content of folder
def get_files(dir, suffix):
    """
    Returns all the files in a folder ending with suffix
    :param dir:
    :param suffix:
    :return: the list of file names
    """
    files = []
    for file in os.listdir(dir):
        if file.endswith(suffix):
            files.append(file)
    #print(files)
    return files

#use .toLower().strip() in main also time clock in main
def readFile(file):
    try:
        #print("in readFile")
        f = open('Selma/'+file)
        #print("after open")
    except:
        print("file not found")
        exit(0)
    text = f.read().lower().strip()
    return text

#tokenization
def tokenize(text):
    wordsIt = re.finditer('\p{L}+',text)
    return wordsIt

#indexing one file
def index(wordsIt):
    wIndex = {}
    for word in wordsIt:
        #non-unique words
        try:
            wIndex[word.group()].append(word.start())
        #unique words
        except KeyError:
            newList = []
            newList.append(word.start())
            #wIndex.append(word,newList)
            wIndex[word.group()] = newList
    return wIndex

#save dictionary to pickle file
def pickleIndex(indexDict, fileName):
    pickle.dump(indexDict, open(str(fileName) + ".idx","wb"))

#create an intermediate index that sorts by filename
def intermediate(files):
    intermediate = {}
    for file in files:
        #read file
        #print("intermediate")
        r = readFile(file)
        #tokenize file
        #print("i2")
        t = tokenize(r)
        #create individual index for file
        singIndex = index(t)
        #add individual index to a dictionary
        #intermediate.append(file,singIndex)
        intermediate[file] = singIndex
    return intermediate


#creating master index that sorts by word
def masterIndex(intermediate):
    m = {}
    #iterate through all files
    for fileName in intermediate:
        #iterate through all words in single file
        for word in intermediate[fileName]:
            try:
                #if the word is already in the master index, add new fileName:index pair
                #m[word].append(fileName,intermediate[fileName][word])
                m[word][fileName]=intermediate[fileName][word]
            except KeyError:
                #if the word isn't in the master index, add nested dictionary
                toAdd = {fileName:intermediate[fileName][word]}
                #m.append(word,toAdd)
                m[word] = toAdd
    return m

#tf-idf
def tfIdf(intermediate,master,files):
    freq = {}
    WORDS = []
    for word in master:
        WORDS.append(word)
    for file in files:
        newDict = {}
        #freq.append(file,newDict)
        freq[file] = newDict
        #freq['nils.txt'] = newDict
        for word in WORDS:
            #find the number of times word appears in doc
            try:
                a = len(intermediate[file][word])
            except KeyError:
                a = 0
            
            #find total number of words in doc
            totalWords = len(intermediate[file])

            #find total number of documents
            totalDocs = len(files)

            #find number of docs with the word
            docsWithWord = len(master[word])

            #calculate tf-idf
            tfidf = (a/totalWords) * math.log10(totalDocs/docsWithWord)

            #update dictionary
            #freq[file].append(word, tfidf)
            freq[file][word] = tfidf
    return freq


#comparing documents using cosine similarity
def cosineSim(freqA,freqB):
    '''
    use numpy
    dot(a,b)/(norm(a)*norm(b))
    '''
    cs = np.dot(freqA,freqB)/((npla.norm(freqA)*(npla.norm(freqB))))
    return cs

#main function
def main(argv):
    files = get_files(argv,"txt")
    #print("hello")
    i = intermediate(files)
    m = masterIndex(i)
    
    for word in m:
        print(str(word) + ': ', sep=' ', end='', flush=True)
        for fileName in m[word]:
            print(str(fileName) + ' ',sep=' ', end='', flush=True)
            for index in m[word][fileName]:
                print(index,' ',sep=' ', end='', flush=True)
        print()
    #freq = tfIdf(i,m,files)
    #print(freq)


if __name__ == "__main__":
   main(sys.argv[1])

