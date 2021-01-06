'''
2. Закодируйте любую строку по алгоритму Хаффмана.
'''
class MyNode:

    def __init__(self, left=None, right=None):
        self.left=left
        self.right=right

    def leaves(self):
        return self.left, self.right

def huffman(node, code=""):
    if isinstance(node, str):
        return {node: code}

    l, r = node.leaves()

    result = {}
    result.update(huffman(l, code + "0"))
    result.update(huffman(r, code + "1"))

    return result


S='Keep calm! Absolutely'
print(f'Строка: {S}')
stat = {}
d=[]
for char in S:
    if char not in stat:
        stat[char] = 0
    stat[char] += 1
# d.append(stat[char])

# tree = build(d)
tree = stat.items()
print(tree)

while len(tree) > 1:
    tree = sorted(tree, reverse=True, key=lambda x: x[1])
    char1, count1 = tree[-1]
    char2, count2 = tree[-2]
    tree = tree[:-2]
    tree.append((MyNode(char1, char2), count1 + count2))

code_table = huffman(tree[0][0])

coded = []
for char in S:
    coded.append(code_table[char])

print(f"Код: {''.join(coded)}")