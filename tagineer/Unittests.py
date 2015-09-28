__author__ = 'Josh'
from tagineer.POS_tagger import *

#Test for properly functioning word structure

def word_test(input="apples", expected_word="apples", expected_tag=None):
    sample = Word(input)
    if sample.word == expected_word and sample.tag == expected_tag:
        return "passed"
    else:
        return "failed"

#Test for correct Sentence structure

def sentence_test(input="The apples appear to be red.", expected="the apples appear to be red"):
    sample = Sentence(input)
    if str(sample) == expected:
        return "passed"
    else:
        return "failed"

def tag_test(input="The sea is an amazing place", expected=[('the', 'article'), ('apples', 'noun'), ('appear', 'verb'), ('to', 'subord_conj'), ('be', 'verb'), ('red', 'noun')]):
    sample = Sentence(input)
    sample = tag_sentence(sample)
    if sample.show_tags() == expected:
        return "passed"
    else:
        return "failed"
