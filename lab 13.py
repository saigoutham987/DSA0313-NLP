class Node:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children or []

    def print_tree(self, level=0):
        print("  " * level + self.label)
        for child in self.children:
            child.print_tree(level + 1)

tree = Node("S", [
    Node("NP", [
        Node("Det", [Node("the")]),
        Node("N", [Node("boy")])
    ]),
    Node("VP", [
        Node("V", [Node("eats")]),
        Node("NP", [
            Node("N", [Node("apple")])
        ])
    ])
])

tree.print_tree()
