#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------------------
#The purpose of this code is to implement a brute-force spell checker by utilizing the
#dynamic programming Damerau-Levenshtein distance algorithm.
#
#
#Copyright (C) 2021, released under MIT License
#Author: Raihan Ahmed, Chicago, IL
#email: rahmed10@neiu.edu
#-------------------------------------------------------------------------------------------

import sys
import time
from difflib import SequenceMatcher

FILE_PATH = 'lib/'

#Damerau-LV Distance outputs minimum cost of converting on string into another utilizing
#insertions, deletions, substitutions, and transpositions
def damerau_levenshtein(s1, s2):
    """ This function provides an implementation of the Damerau-Levenshtein aglorithm """

    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in range(-1,lenstr2+1):
        d[(-1,j)] = j+1

    for i in range(lenstr1):
        for j in range(lenstr2):
            #recursively called functions:
            #indicator function
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1

            d[(i,j)] = min(d[(i-1,j)] + 1, # deletion
                           d[(i,j-1)] + 1, # insertion
                           d[(i-1,j-1)] + cost, # substitution
                          )

            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition

    return d[lenstr1-1,lenstr2-1]

def spellcheck(incorrect_words, correct_words):
    """ This function serves as the helper method for the Damerau-Levenshtein algorithm to find
        the best match from the correct_words list for each word in the incorrect_words list. """

    #Creating a dictionary to store each word from the list and its distance from the input word
    dict = {}
    spellchecked = []

    for word in incorrect_words:
        for x in correct_words:
            dict.update({x : damerau_levenshtein(x, word)})

        #Sorting dictionary by value, from smallest to largest distance
        sorted_d = sorted(dict.items(), key=lambda x: x[1])

        if SequenceMatcher(None, sorted_d[0][0], word).ratio() >= 0.75:
            spellchecked.append(sorted_d[0][0])
        else:
            dict = {}

    return spellchecked

def read_file(file):
    """ Function used to extract the words from the input file and put them into a list"""

    lines = []

    try:
        with open(file, 'r') as f:
            lines = f.read()
    except IOError:
        print("Error: The input file: " + file + ", does not appear to exist! Operation terminated.")
    else:
        lines = [line.strip() for line in lines.splitlines() if len(line.strip()) != 0]

        return lines

def get_wordlists(word_files):
    """ Function used to extract the list of incorrect words and the list of correct words
        to be later used for the Damerau-Levenshtein text correction algorithm"""

    incorrect_words = read_file(word_files[0])
    correct_words = read_file(word_files[1])

    return incorrect_words, correct_words

if __name__ == '__main__':
    start = time.perf_counter()

    # #read input and output files
    # input_files = sys.argv[1:]

    word_files = [FILE_PATH + 'incorrect_words.txt', FILE_PATH + 'correct_words.txt']

    # incorrect_words, correct_words = get_wordlists(input_files)
    incorrect_words, correct_words = get_wordlists(word_files)

    spellchecked_words = spellcheck(incorrect_words, correct_words)

    print(spellchecked_words)

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 3)} second(s)')