# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 22:32:43 2018

@author: RTodinova

"""

from parsers import JsonParser, ResponseParser

class Chatbot:
    
    def __init__(self, responses):
        self.responses = responses
        self.response = ResponseParser()
    
    def respond(self, user_input):
        return self.response.search_answer_in_responses(self.responses, user_input)
            
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