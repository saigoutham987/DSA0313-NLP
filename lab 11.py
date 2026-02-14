tokens = []
pos = 0

def match(expected):
    global pos
    if pos < len(tokens) and tokens[pos] == expected:
        pos += 1
        return True
    return False

def S():
    return NP() and VP()

def NP():
    return match('the') and match('boy')

def VP():
    return match('eats') and match('apple')

sentence = "the boy eats apple"
tokens = sentence.split()
pos = 0

if S() and pos == len(tokens):
    print("Sentence is valid")
else:
    print("Sentence is invalid")
