from dataclasses import dataclass

from user_interface import ignore


@dataclass
class AutoCompleteData:
    def __init__(self, sentence, file, line):
        self.score = 0
        self.completed_sentence = sentence
        self.ignore_sentence = ignore(sentence)
        self.source_text = file
        self.offset = line

    def __str__(self):
        return self.completed_sentence + " " + "(" + self.source_text + " " + str(self.offset) + ")"

    def __lt__(self, other):
        return self.score < other.score

    def set_score(self, new_score):
        self.score = new_score
