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


class ChatbotRunner:

    def __init__(self):
        self.parser = JsonParser()
        responses = self.parser.parse_to_dictionary()
        self.chatbot = Chatbot(responses)


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
