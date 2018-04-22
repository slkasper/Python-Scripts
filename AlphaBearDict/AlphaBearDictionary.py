# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 17:49:19 2018

@author: Sonya
"""
import json
from itertools import permutations
#from  more_itertools import unique_everseen

filename = "dictionary-master\dictionary.json"

def ask():
    '''docstring: explain what i do'''
    # then we need to output the words with the definitions.
    output_defs = str(input('What do you want to define? (press q to quit) >>> '))
    word_to_define = output_defs.upper()
    return word_to_define

# Fist we need to download a dictionary.
with open(filename) as json_data:
    websters = json.load(json_data)

# Then we need to write code that inputs a set of letters.
user_input_letters = str(input('Place Letters Here: --> '))
letters = user_input_letters.upper()

if letters.isalpha():
    all_words = []
    # checks all the permutations for the letters
    for i in range(2, len(letters) + 1):
        for perm in permutations(letters, i):
            check_is_word = ''.join(perm)
            # cache the permuted letters if is a word in the websters dict
            if check_is_word in websters:
                all_words.append(check_is_word)
    # print the words that are in websters
    for word in sorted(set(all_words)):
        print(word)

    # ask if the user wants to look up a word in websters
    # prompt user for which word, print defintion of word
    # runs in a loop until we hit q to quit
    ans = None
    while ans != 'Q' and len(all_words) > 0:
        ans = ask()
        if ans in websters and ans != 'Q':
            print(websters[ans])

else:
    print('only enter letters n00b!')
