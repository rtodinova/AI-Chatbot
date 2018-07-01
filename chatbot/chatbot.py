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
        
        
    def to_lower(self, question):
        return question.lower()


    def respond(self, user_input):
        return self.response.search_answer_in_responses(self.responses, user_input)


class ChatbotRunner:

    def __init__(self):
        self.parser = JsonParser()
        responses = self.parser.parse_to_dictionary()
        self.chatbot = Chatbot(responses)
        
        
    def get_type_of_chatbot_from_user_input(self):
        user_input = input('Hello there! We\'re three chatbots that can do different things. My name is Eve and I\'m a talking chatbot. My friends are Steve and ')
        return user_input

    def run(self):
        user_message = input("USER: ")
        while user_message != "exit":
            print(self.chatbot.respond(user_message))
            user_message = input("USER: ")

        self.parser.parse_to_json(self.chatbot.responses)


def main():
    chatbot = ChatbotRunner()
    chatbot.run()


if __name__ == "__main__": 
    main()
