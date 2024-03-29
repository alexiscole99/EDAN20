"""
CoNLL-X and CoNLL-U file readers and writers
"""
__author__ = "Pierre Nugues"

import os


def get_files(dir, suffix):
    """
    Returns all the files in a folder ending with suffix
    Recursive version
    :param dir:
    :param suffix:
    :return: the list of file names
    """
    files = []
    for file in os.listdir(dir):
        path = dir + '/' + file
        if os.path.isdir(path):
            files += get_files(path, suffix)
        elif os.path.isfile(path) and file.endswith(suffix):
            files.append(path)
    return files


def read_sentences(file):
    """
    Creates a list of sentences from the corpus
    Each sentence is a string
    :param file:
    :return:
    """
    f = open(file).read().strip()
    sentences = f.split('\n\n')
    return sentences


def split_rows(sentences, column_names):
    """
    Creates a list of sentence where each sentence is a list of lines
    Each line is a dictionary of columns
    :param sentences:
    :param column_names:
    :return:
    """
    new_sentences = []
    root_values = ['0', 'ROOT', 'ROOT', 'ROOT', 'ROOT', 'ROOT', '0', 'ROOT', '0', 'ROOT']
    start = [dict(zip(column_names, root_values))]
    for sentence in sentences:
        rows = sentence.split('\n')
        sentence = [dict(zip(column_names, row.split('\t'))) for row in rows if row[0] != '#']
        sentence = start + sentence
        new_sentences.append(sentence)
    return new_sentences


def save(file, formatted_corpus, column_names):
    f_out = open(file, 'w')
    for sentence in formatted_corpus:
        for row in sentence[1:]:
            # print(row, flush=True)
            for col in column_names[:-1]:
                if col in row:
                    f_out.write(row[col] + '\t')
                else:
                    f_out.write('_\t')
            col = column_names[-1]
            if col in row:
                f_out.write(row[col] + '\n')
            else:
                f_out.write('_\n')
        f_out.write('\n')
    f_out.close()

def listOfSentences(formatted_corpus):
    sentences = []
    for sentence in formatted_corpus:
        temp = {}
        for word in sentence:
            temp[word['id']] = word
        sentences.append(temp)
    return sentences

def computeTotalGroups(groups):
    total = 0
    for val in groups.values():
        total += val
    print("Total pairs:",total)

def mostFrequentGroups(groups):
    mostFreq = []
    groups = sorted(groups.items() , reverse = True, key=lambda x: x[1])
    for g in groups:
        mostFreq.append((g[0],g[1]))
    mostFreq = mostFreq[0:5]
    print("Most Frequent: ")
    for m in mostFreq:
        print(m[0], m[1])

def subjectVerbPairs(sentences):
    pairs = {}
    for s in sentences:
        for word in s.values():
            if(word['deprel'] == 'SS'):
                temp = (word['form'].lower(),s[word['head']]['form'].lower())
                if temp in pairs:
                    pairs[temp] += 1
                else: 
                    pairs[temp] = 1
    return pairs

def subjectVerbObjectTriples(sentences):
    triples = {}
    for s in sentences:
        for word in s.values():
            if(word['deprel'] == 'SS'):
                subj = word
                verb = s[word['head']]['form'].lower()
                obj = ''
                for w in s.values():
                    if(w['deprel'] == 'OO' and w['head'] == subj['head']):
                        obj = w['form'].lower()
                        temp = (subj['form'].lower(),verb,obj)
                        if temp in triples:
                            triples[temp] += 1
                        else:
                            triples[temp] = 1
    return triples

def subjectVerbPairsMulti(sentences):
    pairs = {}
    for s in sentences:
        for word in s.values():
            if(word['deprel'] == 'nsubj'):
                temp = (word['form'].lower(),s[word['head']]['form'].lower())
                if temp in pairs:
                    pairs[temp] += 1
                else: 
                    pairs[temp] = 1
    return pairs

def subjectVerbObjectTriplesMulti(sentences):
    triples = {}
    for s in sentences:
        for word in s.values():
            if(word['deprel'] == 'nsubj'):
                subj = word
                verb = s[word['head']]['form'].lower()
                obj = ''
                for w in s.values():
                    if(w['deprel'] == 'obj' and w['head'] == subj['head']):
                        obj = w['form'].lower()
                        temp = (subj['form'].lower(),verb,obj)
                        if temp in triples:
                            triples[temp] += 1
                        else:
                            triples[temp] = 1
    return triples

if __name__ == '__main__':
    column_names_2006 = ['id', 'form', 'lemma', 'cpostag', 'postag', 'feats', 'head', 'deprel', 'phead', 'pdeprel']
    train_file = 'training_set.conll'
    #train_file = 'test_x'
    test_file = 'test_set.conll'
    sentences = read_sentences(train_file)
    formatted_corpus = split_rows(sentences, column_names_2006)
    #print(train_file, len(formatted_corpus))
    #print(formatted_corpus[0])
    #print(formatted_corpus[1])
    sentenceList = listOfSentences(formatted_corpus)
    print("-----SWEDISH-----")
    print("PAIRS")
    pairs = subjectVerbPairs(sentenceList)
    computeTotalGroups(pairs)
    mostFrequentGroups(pairs)
    print("TRIPLES")
    triples = subjectVerbObjectTriples(sentenceList)
    computeTotalGroups(triples)
    mostFrequentGroups(triples)

    column_names_u = ['id', 'form', 'lemma', 'upostag', 'xpostag', 'feats', 'head', 'deprel', 'deps', 'misc']
    files = get_files('./UniversalDependencies2.4/ud-treebanks-v2.4/UD_English-EWT/', 'train.conllu')
    print("-----ENGLISH-----")
    for train_file in files:
        sentences = read_sentences(train_file)
        formatted_corpus = split_rows(sentences, column_names_u)
        sentenceList = listOfSentences(formatted_corpus)
        #print(train_file, len(formatted_corpus))
        #print(formatted_corpus[0])
        print("PAIRS")
        pairs = subjectVerbPairsMulti(sentenceList)
        mostFrequentGroups(pairs)
        print("TRIPLES")
        triples = subjectVerbObjectTriplesMulti(sentenceList)
        mostFrequentGroups(triples)

    files = get_files('./UniversalDependencies2.4/ud-treebanks-v2.4/UD_German-GSD/', 'train.conllu')
    print("-----GERMAN-----")
    for train_file in files:
        sentences = read_sentences(train_file)
        formatted_corpus = split_rows(sentences, column_names_u)
        sentenceList = listOfSentences(formatted_corpus)
        #print(train_file, len(formatted_corpus))
        #print(formatted_corpus[0])
        print("PAIRS")
        pairs = subjectVerbPairsMulti(sentenceList)
        mostFrequentGroups(pairs)
        print("TRIPLES")
        triples = subjectVerbObjectTriplesMulti(sentenceList)
        mostFrequentGroups(triples)

    files = get_files('./UniversalDependencies2.4/ud-treebanks-v2.4/UD_French-GSD/', 'train.conllu')
    print("-----FRENCH-----")
    for train_file in files:
        sentences = read_sentences(train_file)
        formatted_corpus = split_rows(sentences, column_names_u)
        sentenceList = listOfSentences(formatted_corpus)
        #print(train_file, len(formatted_corpus))
        #print(formatted_corpus[0])
        print("PAIRS")
        pairs = subjectVerbPairsMulti(sentenceList)
        mostFrequentGroups(pairs)
        print("TRIPLES")
        triples = subjectVerbObjectTriplesMulti(sentenceList)
        mostFrequentGroups(triples)



# only use id, form, deprel, head