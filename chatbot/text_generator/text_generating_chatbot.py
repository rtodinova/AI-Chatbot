# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 00:00:31 2018

@author: RTodinova
"""


from ..chatbot import Chatbot
from statement import Statement

class TextGeneratingChatbot(Chatbot):
    def __init__(self):
        self.word_sequences = {}