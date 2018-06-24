# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 00:07:41 2018

@author: RTodinova
"""

import unittest
from parsers import ResponseParser


responses = {"hello": ["Hi", "Hello, nice to meet you"], 
             "what's your name": ["My name is Eve", "They call me Eve", "My name is Eve and I'm an AI chatbot"], 
             "are you a woman": ["Yes, I am", "How do you think"], 
             "how old are you": ["One day old", "24 hours old"], 
             "what's the weather": ["Rainy", "Sunny", "It's very cold", "Beach time"], 
             "question": ["I don't know :(", "Why do you ask?", "Why do you think that?"], 
             "statement": ["That's nice", "Are you kidding me?", "I don't think so", "Are you sure?"] }


class TestResponseParser(unittest.TestCase):

     def setUp(self):
        self.response_parser = ResponseParser() #TODO: make it with mock

        
     def test_search_existing_answer(self):
        user_input = "what's your name"
        self.assertTrue(self, self.response_parser.search_answer_in_responses(responses, user_input) in responses[user_input] )
        
        
     def test_search_question(self):
        user_input="are you going to talk with me?"
        self.assertTrue(self, self.response_parser.search_answer_in_responses(responses, user_input) in responses['question'] )
        
        
     def test_search_statement(self):
        user_input="you're georgeous"
        self.assertTrue(self, self.response_parser.search_answer_in_responses(responses, user_input) in responses['statement'] )

if __name__ == '__main__':
    unittest.main()