# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 22:32:43 2018

@author: RTodinova

"""

import random

from json_parser import JsonParser

class Chatbot:
    
    def __init__(self, responses):
        self.responses = responses
    
    def respond(self,message):
        if message in self.responses:
            return random.choice(self.responses[message])
        elif message.endswith('?'):
            return random.choice(self.responses["question"])
        else:
            return random.choice(self.responses["statement"])
            
def main():
    parser = JsonParser()
    responses = parser.parse_to_dictionary()
    chatbot_runner = Chatbot(responses)
    
    user_message = input("USER: ")
    while user_message != "exit":
        print(chatbot_runner.respond(user_message))
        user_message = input("USER: ")
        
    parser.parse_to_json(chatbot_runner.responses)
        
if __name__ == "__main__": main()