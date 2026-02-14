import re

def rule_based_pos_tagger(sentence):
    tokens = sentence.split()
    tagged = []

    for word in tokens:
        if re.fullmatch(r'\d+', word):
            tag = 'NUM'
        elif re.fullmatch(r'.*ing', word):
            tag = 'VBG'
        elif re.fullmatch(r'.*ed', word):
            tag = 'VBD'
        elif re.fullmatch(r'.*ly', word):
            tag = 'ADV'
        elif re.fullmatch(r'(the|a|an)', word.lower()):
            tag = 'DET'
        elif re.fullmatch(r'(is|am|are|was|were)', word.lower()):
            tag = 'VB'
        else:
            tag = 'NN'
        tagged.append((word, tag))

    return tagged

sentence = "The boy is running quickly"
print(rule_based_pos_tagger(sentence))
