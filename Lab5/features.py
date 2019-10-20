#implement 3 different feature extractors
#run full loop on 1st extractor (most simple) and then implement other 2
    #lab 5 and 6 for 1st

import conll
import transition
import dparser
from sklearn.feature_extraction import DictVectorizer
from sklearn import linear_model
from sklearn import metrics

def extract_features_1(stack,queue,graph,feature_names,sentence):
    #word and pos for 1st in stack and 1st in queue, can-la, can-reduce
    stack_word = 'nil'
    stack_pos = 'nil'
    queue_word = 'nil'
    queue_pos = 'nil'
    canLa = transition.can_leftarc(stack,graph)
    canRe = transition.can_reduce(stack,graph)
    if stack:
        stack_word = stack[0]['form']
        stack_pos = stack[0]['postag']
    if queue:
        queue_word = queue[0]['form']
        queue_pos = queue[0]['postag']

    features = [stack_pos,stack_word,queue_pos,queue_word,canRe,canLa]
    return features

def extract_features_2(stack,queue,graph,feature_names,sentence):
    #2 elements from stack and 2 from input list, can-la, can-re
    stack_word_0 = 'nil'
    stack_pos_0 = 'nil'
    stack_word_1 = 'nil'
    stack_pos_1 = 'nil'
    queue_word_0 = 'nil'
    queue_pos_0 = 'nil'
    queue_word_1 = 'nil'
    queue_pos_1 = 'nil'
    canLa = transition.can_leftarc(stack,graph)
    canRe = transition.can_reduce(stack,graph)

    if stack:
        stack_word_0 = stack[0]['form']
        stack_pos_0 = stack[0]['postag']
        if(len(stack)>1):
            stack_word_1 = stack[1]['form']
            stack_pos_1 = stack[1]['postag']

    if queue:
        queue_word_0 = queue[0]['form']
        queue_pos_0 = queue[0]['postag']
        if(len(queue)>1):
            queue_word_1 = queue[1]['form']
            queue_pos_1 = queue[1]['postag']

    features = [stack_pos_0, stack_pos_1, stack_word_0, stack_word_1, queue_pos_0, queue_pos_1, queue_word_0, queue_word_1, canRe, canLa]
    return features

def extract_features_3(stack,queue,graph,feature_names,sentence):
    #extract at least two more features, one of them being the part of speech and the word form of the word following the top of the stack in the sentence order
    stack_word_0 = 'nil'
    stack_pos_0 = 'nil'
    stack_word_1 = 'nil'
    stack_pos_1 = 'nil'
    stack_word_2 = 'nil'
    stack_pos_2 = 'nil'
    queue_word_0 = 'nil'
    queue_pos_0 = 'nil'
    queue_word_1 = 'nil'
    queue_pos_1 = 'nil'
    queue_word_2 = 'nil'
    queue_pos_2 = 'nil'
    canLa = transition.can_leftarc(stack,graph)
    canRe = transition.can_reduce(stack,graph)

    if stack:
        stack_word_0 = stack[0]['form']
        stack_pos_0 = stack[0]['postag']
        if(len(stack)>1):
            stack_word_1 = stack[1]['form']
            stack_pos_1 = stack[1]['postag']
            if(len(stack>2)):
                stack_word_2 = stack[2]['form']
                stack_pos_2 = stack[2]['postag']

    if queue:
        queue_word_0 = queue[0]['form']
        queue_pos_0 = queue[0]['postag']
        if(len(queue)>1):
            queue_word_1 = queue[1]['form']
            queue_pos_1 = queue[1]['postag']
            if(len(queue)>2):
                queue_word_2 = queue[2]['form']
                queue_pos_2 = queue[2]['postag']

    features = [stack_pos_0, stack_pos_1, stack_pos_2, stack_word_0, stack_word_1, stack_word_2, queue_pos_0, queue_pos_1, queue_pos_2, queue_word_0, queue_word_1, queue_word_2, canRe, canLa]
    return features

def extract(stack,queue,graph,feature_names,sentence):
    if(feature_names == ["stack_pos","stack_word","queue_pos","queue_word,canRe,canLa"]):
        #word and pos for 1st in stack and 1st in queue, can-la, can-reduce
        stack_word = 'nil'
        stack_pos = 'nil'
        queue_word = 'nil'
        queue_pos = 'nil'
        canLa = transition.can_leftarc(stack,graph)
        canRe = transition.can_reduce(stack,graph)
        if stack:
            stack_word = stack[0]['form']
            stack_pos = stack[0]['postag']
        if queue:
            queue_word = queue[0]['form']
            queue_pos = queue[0]['postag']

        features = [stack_pos,stack_word,queue_pos,queue_word,canRe,canLa]
        return features
    if(feature_names == ["stack_pos_0", "stack_pos_1", "stack_word_0", "stack_word_1", "queue_pos_0", "queue_pos_1", "queue_word_0", "queue_word_1", "canRe", "canLa"]):
        #2 elements from stack and 2 from input list, can-la, can-re
        stack_word_0 = 'nil'
        stack_pos_0 = 'nil'
        stack_word_1 = 'nil'
        stack_pos_1 = 'nil'
        queue_word_0 = 'nil'
        queue_pos_0 = 'nil'
        queue_word_1 = 'nil'
        queue_pos_1 = 'nil'
        canLa = transition.can_leftarc(stack,graph)
        canRe = transition.can_reduce(stack,graph)

        if stack:
            stack_word_0 = stack[0]['form']
            stack_pos_0 = stack[0]['postag']
            if(len(stack)>1):
                stack_word_1 = stack[1]['form']
                stack_pos_1 = stack[1]['postag']

        if queue:
            queue_word_0 = queue[0]['form']
            queue_pos_0 = queue[0]['postag']
            if(len(queue)>1):
                queue_word_1 = queue[1]['form']
                queue_pos_1 = queue[1]['postag']

        features = [stack_pos_0, stack_pos_1, stack_word_0, stack_word_1, queue_pos_0, queue_pos_1, queue_word_0, queue_word_1, canRe, canLa]
        return features

    if(feature_names == ["stack_pos_0", "stack_pos_1", "stack_pos_2", "stack_word_0", "stack_word_1", "stack_word_2", "queue_pos_0", "queue_pos_1", "queue_pos_2", "queue_word_0", "queue_word_1", "queue_word_2", "canRe", "canLa"]):
        #extract at least two more features, one of them being the part of speech and the word form of the word following the top of the stack in the sentence order
        stack_word_0 = 'nil'
        stack_pos_0 = 'nil'
        stack_word_1 = 'nil'
        stack_pos_1 = 'nil'
        stack_word_2 = 'nil'
        stack_pos_2 = 'nil'
        queue_word_0 = 'nil'
        queue_pos_0 = 'nil'
        queue_word_1 = 'nil'
        queue_pos_1 = 'nil'
        queue_word_2 = 'nil'
        queue_pos_2 = 'nil'
        canLa = transition.can_leftarc(stack,graph)
        canRe = transition.can_reduce(stack,graph)

        if stack:
            stack_word_0 = stack[0]['form']
            stack_pos_0 = stack[0]['postag']
            if(len(stack)>1):
                stack_word_1 = stack[1]['form']
                stack_pos_1 = stack[1]['postag']
                if(len(stack>2)):
                    stack_word_2 = stack[2]['form']
                    stack_pos_2 = stack[2]['postag']

        if queue:
            queue_word_0 = queue[0]['form']
            queue_pos_0 = queue[0]['postag']
            if(len(queue)>1):
                queue_word_1 = queue[1]['form']
                queue_pos_1 = queue[1]['postag']
                if(len(queue)>2):
                    queue_word_2 = queue[2]['form']
                    queue_pos_2 = queue[2]['postag']

        features = [stack_pos_0, stack_pos_1, stack_pos_2, stack_word_0, stack_word_1, stack_word_2, queue_pos_0, queue_pos_1, queue_pos_2, queue_word_0, queue_word_1, queue_word_2, canRe, canLa]
        return features

if __name__ == '__main__':
    train_file = './swedish_talbanken05_train.conll'
    test_file = './swedish_talbanken05_test_blind.conll'
    column_names_2006 = ['id', 'form', 'lemma', 'cpostag', 'postag', 'feats', 'head', 'deprel', 'phead', 'pdeprel']
    column_names_2006_test = ['id', 'form', 'lemma', 'cpostag', 'postag', 'feats']

    sentences = conll.read_sentences(train_file)
    formatted_corpus = conll.split_rows(sentences, column_names_2006)
    X = []
    y = []
    for sentence in formatted_corpus:
        stack = []
        queue = list(sentence)
        graph = {}
        graph['heads'] = {}
        graph['heads']['0'] = '0'
        graph['deprels'] = {}
        graph['deprels']['0'] = 'ROOT'
        transitions = []
        trans = 'sh'
        while queue:
            X.append(extract_features_2(stack,queue,graph,[],sentence))
            y.append(trans)
            stack, queue, graph, trans = dparser.reference(stack, queue, graph)
            transitions.append(trans)
            #X.append(extract_features_2(stack,queue,graph,[],sentence))
            #y.append(trans)
            
        stack, graph = transition.empty_stack(stack, graph)
    
    #check against lab assignment
    y = y[1:]
    #print(y[:10])
    for i in range(9):
       print("X = ",X[i],", y = ",y[i])

    # evaluate model accuracies using scikit-learn
    # make sure works for all 3 (only using the 2nd function now bc matches assignment)

    '''classifier = linear_model.LogisticRegression(penalty='l2', dual=True, solver='liblinear')
    model = classifier.fit(X,y)
    print(model)'''
    
    
