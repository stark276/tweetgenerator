from dictogram import Dictogram
from random import choice
from histogram import open_file


class Markov():

    def __init__(self, text_file):
        self.content = open_file(text_file)
        self.markov = self.build_markov(self.content)


class Markov():

    def __init__(self, text_file):
        self.content = open_file(text_file)
        self.markov = self.chain(self.content)

    def chain(self, content):
        """MAKING MARKOV CHAIN"""
        markov_chain = {}
        for i in range(len(content)):
            if content[i] not in markov_chain:
                markov_chain[content[i]] = []
            if i < len(content) - 1:
                markov_chain[content[i]].append(content[i + 1])

        for key in markov_chain:
            markov_chain[key] = Dictogram(markov_chain[key])

        return markov_chain

    def walk(self, length):

        temp_list = []

        temp_list.append(choice(tuple(self.markov.keys())))
        for i in range(length - 1):
            temp_list.append(self.markov[temp_list[i]].sample())

        sentence = ""
        for word in temp_list:
            sentence += word + " "

        return sentence

if __name__ == '__main__':
    markov = Markov('words.txt')
    print(markov.walk(10))