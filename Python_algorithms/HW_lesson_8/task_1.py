"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""

from collections import Counter


the_spell = 'avada_kedavra_muggle'


class Huffman:

    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def make_code(root, codes=dict(), code=''):
    if root is None:
        return

    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    make_code(root.left, codes, code + '0')
    make_code(root.right, codes, code + '1')

    return codes


def code_tree(string):
    string_count = Counter(string)

    if len(string_count) <= 1:
        node = Huffman(None)

        if len(string_count) == 1:
            node.left = Huffman([key for key in string_count][0])
            node.right = Huffman(None)

        string_count = {node: 1}

    while len(string_count) != 1:
        node = Huffman(None)
        spam = string_count.most_common()[:-3:-1]

        if isinstance(spam[0][0], str):
            node.left = Huffman(spam[0][0])

        else:
            node.left = spam[0][0]

        if isinstance(spam[1][0], str):
            node.right = Huffman(spam[1][0])

        else:
            node.right = spam[1][0]

        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        string_count[node] = spam[0][1] + spam[1][1]

    return [key for key in string_count][0]


def coding(string, codes):
    res = ''

    for symbol in string:
        res += codes[symbol]

    return res


def decoding(string, codes):
    res = ''
    i = 0

    while i < len(string):

        for code in codes:

            if string[i:].find(codes[code]) == 0:
                res += code
                i += len(codes[code])

    return res


print(the_spell)
tree = code_tree(the_spell)

codes = make_code(tree)
print(codes)