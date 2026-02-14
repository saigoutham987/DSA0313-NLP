grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP']],
    'Det': [['the']],
    'N': [['boy'], ['apple']],
    'V': [['eats']]
}

def earley_parser(sentence):
    words = sentence.split()
    chart = [set() for _ in range(len(words) + 1)]

    chart[0].add(('S', tuple(grammar['S'][0]), 0, 0))

    for i in range(len(words) + 1):
        for state in list(chart[i]):
            lhs, rhs, dot, start = state
            if dot < len(rhs):
                symbol = rhs[dot]
                if symbol in grammar:
                    for prod in grammar[symbol]:
                        chart[i].add((symbol, tuple(prod), 0, i))
                elif i < len(words) and symbol == words[i]:
                    chart[i + 1].add((lhs, rhs, dot + 1, start))
            else:
                for st in chart[start]:
                    slhs, srhs, sdot, sstart = st
                    if sdot < len(srhs) and srhs[sdot] == lhs:
                        chart[i].add((slhs, srhs, sdot + 1, sstart))

    return ('S', tuple(grammar['S'][0]), 1, 0) in chart[len(words)]

sentence = "the boy eats apple"
print("Valid Sentence:", earley_parser(sentence))
