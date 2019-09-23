# Alexis Cole and Jonathan Moran
# Lab1

import regex as re
import pickle
import os 
import sys 
import math
import numpy as np
from numpy import linalg as npla
import operator

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
def pickleIndex(fileName):
    r = readFile(fileName)
    t = tokenize(r)
    indexDict = index(t)
    fileName = fileName[0:-4]
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

def dictToList(d):
    l = []
    for key in d:
        l.append(d[key])
    return l

def compareAllDocs(files, freq):
    print("=====MOST SIMILAR NOVELS=====")
    cosineSimDict = {}
    files.sort()
    for i in range(len(files)):
        for j in range(len(files)):
            f1 = files[i]
            f1tfidf = dictToList(freq[f1])
            f2 = files[j]
            f2tfidf = dictToList(freq[f2])
            valToAdd = cosineSim(f1tfidf,f2tfidf)
            keyToAdd = f1 + " & " + f2
            cosineSimDict[keyToAdd] = valToAdd
    #print(cosineSimDict)
    mostSim = ""
    mostSimVal = 0
    for key in cosineSimDict:
        if(cosineSimDict[key] < 1 and cosineSimDict[key] > mostSimVal):
            mostSim = key
            mostSimVal = cosineSimDict[key]
    print(mostSim)
    print("==========")

    return(cosineSimDict)

def cosineSimMatrix(files, freq):
    print("=====COSINE SIMILARITY MATRIX=====")
    m = np.ones((9,9))
    files.sort()
    for i in range(len(files)):
        for j in range(len(files)):
            if(i == j):
                continue
            f1 = files[i]
            f1tfidf = dictToList(freq[f1])
            f2 = files[j]
            f2tfidf = dictToList(freq[f2])
            valToAdd = cosineSim(f1tfidf,f2tfidf)
            m[i][j] = valToAdd
    print(m)
    print("==========")
    return m

def testMasterIndex1(m):
    print("=====TEST MASTER INDEX=====")
    print("samlar: ")
    print(m["samlar"])
    print("ände: ")
    print(m["ände"])
    print("==========")

def testtfIdf1(freq):
    print("=====TEST IFIDF=====")
    print("bannlyst.txt: ")
    print("känna ",freq["bannlyst.txt"]["känna"])
    print("gås ",freq["bannlyst.txt"]["gås"])
    print("nils ",freq["bannlyst.txt"]["nils"])
    print("et ",freq["bannlyst.txt"]["et"])

    print("gosta.txt: ")
    print("känna ",freq["gosta.txt"]["känna"])
    print("gås ",freq["gosta.txt"]["gås"])
    print("nils ",freq["gosta.txt"]["nils"])
    print("et ",freq["gosta.txt"]["et"])
    
    print("herrgard.txt: ")
    print("känna ",freq["herrgard.txt"]["känna"])
    print("gås ",freq["herrgard.txt"]["gås"])
    print("nils ",freq["herrgard.txt"]["nils"])
    print("et ",freq["herrgard.txt"]["et"])

    print("jerusalem.txt: ")
    print("känna ",freq["jerusalem.txt"]["känna"])
    print("gås ",freq["jerusalem.txt"]["gås"])
    print("nils ",freq["jerusalem.txt"]["nils"])
    print("et ",freq["jerusalem.txt"]["et"])

    print("nils.txt: ")
    print("känna ",freq["nils.txt"]["känna"])
    print("gås ",freq["nils.txt"]["gås"])
    print("nils ",freq["nils.txt"]["nils"])
    print("et ",freq["nils.txt"]["et"])

    print("==========")

#main function
def main(argv):
    files = get_files(argv,"txt")
    #print("hello")
    i = intermediate(files)
    m = masterIndex(i)
    freq = tfIdf(i,m,files)
    
    '''for word in m:
        print(str(word) + ': ', sep=' ', end='', flush=True)
        for fileName in m[word]:
            print(str(fileName) + ' ',sep=' ', end='', flush=True)
            for index in m[word][fileName]:
                print(index,' ',sep=' ', end='', flush=True)
        print()
    #freq = tfIdf(i,m,files)
    #print(freq)'''
    
    #use to demo completion
    #pickleIndex("nils.txt")
    testMasterIndex1(m)
    testtfIdf1(freq)
    compareAllDocs(files, freq)
    cosineSimMatrix(files,freq)


if __name__ == "__main__":
   main(sys.argv[1])

