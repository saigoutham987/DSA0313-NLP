def initial_tagger(sentence):
    return [(word, 'NN') for word in sentence.split()]

def transformation_rules(tagged_sentence):
    transformed = []
    for i, (word, tag) in enumerate(tagged_sentence):
        if word.endswith('ing'):
            tag = 'VBG'
        elif word.lower() in ['is', 'am', 'are']:
            tag = 'VB'
        transformed.append((word, tag))
    return transformed

sentence = "He is playing football"
initial = initial_tagger(sentence)
final_tags = transformation_rules(initial)

print("Initial Tags:", initial)
print("Final Tags:", final_tags)
