# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 22:59:28 2018

@author: RTodinova
"""

import json

class JsonParser:
    
    def __init__(self):
        self.file_name = 'chatbot_knowledge.json'
        
    def parse_to_json(self, dictionary_with_responses):
        with open(self.file_name, 'w') as json_file:
            json.dump(dictionary_with_responses, json_file)
            
    def parse_to_dictionary(self):
        with open(self.file_name, 'r') as json_file:
            return json.load(json_file)