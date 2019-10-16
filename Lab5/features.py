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
    return 0

if __name__ == '__main__':
    pass