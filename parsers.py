# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 22:59:28 2018

@author: RTodinova
"""

import json
import re
import random


class JsonParser:
    
    def __init__(self):
        self.file_name = 'chatbot_knowledge.json'
        
    def parse_to_json(self, dictionary_with_responses):
        with open(self.file_name, 'w') as json_file:
            json.dump(dictionary_with_responses, json_file)
            
    def parse_to_dictionary(self):
        with open(self.file_name, 'r') as json_file:
            return json.load(json_file)
        
    
class ResponseParser:
    
    day_names_short = 'mon|tue|wed|thu|fri|sat|sun'
    day_names = day_names_short + 'monday|tuesday|wednesday|thursday|friday|saturday|sunday'
    
    month_names_short = 'jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec' #There is no may, because it already exist in the month names below
    month_names = month_names_short + 'january|february|march|april|may|june|july|august|september|october|november|december'
    
    numbers = (
    '(one|two|three|four|five|six|seven|eight|nine|ten|'
    'eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|'
    'eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|'
    'eighty|ninety|hundred|thousand)'
    )
    
    greetings = 'hello|hi|hllo|helo'
    
    def __init__(self):
        self.previous_user_input = ''
    
    def to_lower(self, question):
        return question.lower()
    
    def search_answer_in_responses(self, responses, user_input):
        user_input = self.to_lower(user_input)
        if user_input in self.greetings:
            self.previous_user_input = user_input
            return random.choice(responses['hello'])
        elif user_input == "not correct":
            correct_answer = self.get_the_correct_answer_from_user()
            self.save_the_correct_answer(responses, correct_answer, self.previous_user_input)
            return 'Ok, thanks for the advise'
        elif user_input in responses:
            self.previous_user_input = user_input
            return random.choice(responses[user_input])
        elif user_input.endswith('?'):
            self.previous_user_input = user_input
            return random.choice(responses["question"])
        else:
            self.previous_user_input = user_input
            return random.choice(responses["statement"])
      
    def get_the_correct_answer_from_user(self):
        correct_answer = input('What should be my answer? \nUSER: ')
        return correct_answer
    
    def save_the_correct_answer(self, responses, correct_answer, previous_user_input):
        if previous_user_input in responses.keys():
            responses[self.previous_user_input].append(correct_answer)
        else:
            responses[self.previous_user_input] = []
            responses[self.previous_user_input].append(correct_answer)
            
            