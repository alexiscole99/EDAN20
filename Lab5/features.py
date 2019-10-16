#implement 3 different feature extractors
#run full loop on 1st extractor (most simple) and then implement other 2
    #lab 5 and 6 for 1st

import conll
import transition
import dparser
import sklearn

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

    features = [stack_pos,stack_word,queue_pos,queue_word,canLa,canRe]
    return features

def extract_features_2(stack,queue,feature_names,sentence):
    return 0

def extract_features_3(stack,queue,feature_names,sentence):
    return 0

if __name__ == '__main__':
    pass