# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 00:00:31 2018

@author: RTodinova
"""


from ..chatbot import Chatbot
#from statement import Statement
from ..parsers import JsonParser

class TextGeneratingChatbot(Chatbot):
    def __init__(self):
        parser = JsonParser('../json_files/text_generator_dictionary.json')
        self.word_sequences = parser.parse_to_dictionary()
        

class TextGeneratorTrainer:
    def __init__(self, text_to_learn):
        self.text_to_learn = text_to_learn
        
    
    def learn_from_text(self, word_sequence, text):
        tokens = text.split(" ")
        for word_index in range(0, len(tokens)-1):
            current_word = tokens[word_index]
            next_word = tokens[word_index+1]
        
        if current_word not in word_sequence:
            word_sequence[current_word] = {next_word : 1}
        else:
            all_next_words = word_sequence[current_word]
            if next_word not in all_next_words:
                word_sequence[current_word][next_word] = 1
            else:
                word_sequence[current_word][next_word] = word_sequence[current_word][next_word] + 1
        
        return word_sequence
        


class GeneratingText:
    pass