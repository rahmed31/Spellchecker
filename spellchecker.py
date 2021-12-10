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

import time
import random as rnd
from difflib import SequenceMatcher

LIB_PATH = 'lib/'
TEST_PATH = 'test/'

def spellcheck(incorrect_words, correct_words):
    """ This function serves as the helper method for the Damerau-Levenshtein algorithm to find
        the best match from the correct_words list for each word in the incorrect_words list. """

    def damerau_levenshtein(s1, s2):
        """ Damerau-LV Distance outputs minimum cost of converting one string into another utilizing
            insertions, deletions, substitutions, and transpositions """

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

    #Creating a dictionary to store each word from the list and its distance from the input word
    dict = {}
    spellchecked = []

    #shuffle correct words list
    rnd.shuffle(correct_words)

    for word in incorrect_words:
        for x in correct_words:
            dict.update({x : damerau_levenshtein(x, word)})

        #Sorting dictionary by value, from smallest to largest distance
        sorted_d = sorted(dict.items(), key=lambda x: x[1])

        #Applying threshold of >= 0.70 to find most accuracate word from dictionary
        if SequenceMatcher(None, sorted_d[0][0], word).ratio() >= 0.70:
            spellchecked.append(sorted_d[0][0])
        else:
            spellchecked.append("Could not match word")

        dict = {}

    return spellchecked

def read_file(file):
    """ Function used to extract the words from the input file and put them into a list to
        be later used by the Damerau-Levenshtein text correction algorithm"""

    lines = []

    try:
        with open(file, 'r') as f:
            lines = f.read()
    except IOError:
        print("Error: The input file: " + file + ", does not appear to exist! Operation terminated.")
    else:
        lines = [line.strip() for line in lines.splitlines() if len(line.strip()) != 0]

        return lines

def calculate_accuracy(test_tags, model_tags):
    """ Function to calculate the accuracy of the Viterbi algorithm by comparing the output of the POS tagger to the actual tags
        provided in the test set. """

    num_correct = 0
    total = 0

    for test_taglist, model_taglist in zip(test_tags, model_tags):
        for test_pos, model_pos in zip(test_taglist, model_taglist):
            if test_pos == model_pos:
                num_correct += 1

            total += 1

    accuracy = round(num_correct/float(total), 3) * 100

    return accuracy

def calculate_accuracy(test_words, spellchecked_words):
    """ Function to find the accuracy of the spellchecked words returned from the Damerau-Levenshtein
        algorithm by comparing each spellchecked word to its intended word"""

    num_correct = 0
    total = 0

    for test_word, spellchecked_word in zip(test_words, spellchecked_words):
        if test_word == spellchecked_word:
            num_correct += 1

        total += 1

    accuracy = round(num_correct/float(total), 4) * 100

    return accuracy

if __name__ == '__main__':
    start = time.perf_counter()

    word_files = [LIB_PATH + 'incorrect_words.txt', LIB_PATH + 'correct_words.txt']

    incorrect_words = read_file(word_files[0])
    correct_words = read_file(word_files[1])
    spellchecked_words = spellcheck(incorrect_words, correct_words)
    accuracy = calculate_accuracy(read_file(TEST_PATH + 'test_words.txt'), spellchecked_words)

    print("================================================")
    print("LIST OF INCORRECT WORDS:")
    print(incorrect_words)
    print("LIST OF SPELLCHECKED WORDS:")
    print(spellchecked_words)
    print("SPELL CHECKER ACCURACY:")
    print(str(accuracy) + "%")
    print("================================================")

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 3)} second(s)')
