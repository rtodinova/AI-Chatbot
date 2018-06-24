# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 22:59:28 2018

@author: RTodinova
"""

import json
import re


class JsonParser:
    
    def __init__(self):
        self.file_name = 'chatbot_knowledge.json'
        
    def parse_to_json(self, dictionary_with_responses):
        with open(self.file_name, 'w') as json_file:
            json.dump(dictionary_with_responses, json_file)
            
    def parse_to_dictionary(self):
        with open(self.file_name, 'r') as json_file:
            return json.load(json_file)
        
    
class QuestionParser:
    
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
    
    def to_lower(self, question):
        return question.lower()