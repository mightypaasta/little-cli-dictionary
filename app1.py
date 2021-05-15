# from typing import Collection
# import pandas as pd
# import os
# import time
# from spellchecker import SpellChecker

# spell=SpellChecker()
# print(spell.unknown(spell.split_words('I am tehre foor yoou')))
        # if spellChecker(word, data)[0] in data.keys():
        #     return data[spellChecker(word,data)[0]]
        # else:
        #     return 'Search not found'

        
import json
from difflib import get_close_matches

# data will store the json object in dictionary format
data=json.load(open("data.json"))

# this function will return the most appropriate word for the typo
def spellChecker(word,data):
    return get_close_matches(word,data,1,0.8)

# flag will track whether the word has typo or it is meaningless or it is correct 
# flag=0 if word is correct
# flag=1 if word has typo
# flag=2 if word is meaningless
flag=0

# finder fucntion will return the meaning of words including typo otherwise returning "Search not found" for meaningless words
def finder(word):
    global flag
    corrected_word=spellChecker(word, data)
    if word in data.keys():
        flag=0
        return data[word]
    else:
        if corrected_word != []:
            flag=1
            print('Did you mean %s'%corrected_word[0])
            return data[corrected_word[0]]
        else:
            flag=2
            return "Search not found"



# This loop will continue to ask for the words to user until given '\exit' to break the loop and exit the proram
while True:
    word=input("Enter the word to search: ")
    if word == '\exit':
        break
    else:
        if flag==2:
            print(word+": "+"Search not found")
        else:
            if flag==0:
                print(word+":          "+finder(word)[0])
            else:
                print(spellChecker(word, data)[0].title()+":\t"+' '.join(str(elem) for elem in finder(word)))
    print(flag)     
    print('\n')       





