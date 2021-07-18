from collections import deque

from auto_complete_funcs import ignore


class Node:
    def __init__(self, character, parent):
        self.character = character
        if self.character is not None:
            self.character = self.character.lower()
        self.parent = parent
        self.children = dict()
        self.isEndOfWord = False

    def add(self, child_node):
        self.children[child_node.character] = child_node


class Trie:

    def __init__(self):
        self._root = Node(None, None)

    def insert(self, word):
        if word:
            current_node = self._root
            for i, character in enumerate(word):
                if character in current_node.children:
                    current_node = current_node.children[character]
                else:
                    child_node = Node(character, current_node)
                    current_node.add(child_node)
                    current_node = child_node
            current_node.isEndOfWord = True

    def __contains__(self, item):
        current_node = self._root
        contained = True
        for symbol in item:
            if symbol in current_node.children:
                current_node = current_node.children[symbol]
            else:
                contained = False
                break
        return contained and current_node.isEndOfWord

    def _get_all_words(self, prefix, node, word_list):
        if node.character:
            prefix.append(node.character)
        for child in node.children.values():
            self._get_all_words(prefix, child, word_list)
        if node.isEndOfWord:
            word_list.append("".join([i[0] for i in prefix]))
        if len(prefix) > 0:
            prefix.pop()

    def get_possible_words(self, prefix):
        current_node = self._root
        found_prefix = True
        word_list = []
        prefix_deque = deque()
        for symbol in prefix:
            if symbol in current_node.children:
                current_node = current_node.children[symbol]
            else:
                found_prefix = False
                break
        if found_prefix:
            self._get_all_words(prefix_deque, current_node, word_list)
        word_list = list(map(lambda word: prefix[:len(prefix) - 1] + word, word_list))
        return word_list

    def get_all_words(self):
        word_list = []
        self._get_all_words(deque(), self._root, word_list)
        return word_list
