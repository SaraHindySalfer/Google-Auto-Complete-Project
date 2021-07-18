import os

from Trie import Trie
from auto_complete_data import AutoCompleteData
from auto_complete_funcs import ignore


class Data:
    def __init__(self):
        self.word_by_letter = Trie()
        self.__sentence_by_word = {}

    def get_word_data(self):
        return self.__sentence_by_word

    def get_letter_data(self):
        return self.word_by_letter

    def insert_data_to_dict(self):
        print("Loading data please wait until done...")
        dir_path = os.path.dirname("./2021-archive/")
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                with open(root[2:] + '\\' + file, encoding='utf8') as text_file:
                    line_count = 0
                    for line in text_file.readlines():
                        line_count += 1
                        for word in line.split():
                            word = ignore(word)
                            if word not in self.__sentence_by_word.keys():
                                self.__sentence_by_word[word] = [
                                    AutoCompleteData(line.strip('\n'), file, line_count)]
                            else:
                                self.__sentence_by_word[word] += [
                                    AutoCompleteData(line.strip('\n'), file, line_count)]
                            self.word_by_letter.insert(word)
        print("the system is ready, please enter your text: ")
