# About spellchecker.py
This file implements a brute-force spellchecker utilizing the dynamically programmed Damerau-Levenshtein algorithm for fuzzy string approximation.

# How to Write Your Own Test Cases
In the `lib` folder, you will see two different text files called 'candidate_words.txt' and 'incorrect_words.txt':

- The `candidate_words.txt` text file can contain an unlimited amount of CORRECTLY spelled words, with each word written on a new line.
- The `incorrect_words.txt` text file can contain an unlimited amount of INCORRECTLY spelled words, with each word written on a new line. However, each incorrectly spelled word in this list MUST have its correctly spelled counterpart contained somewhere in the 'candidate_words.txt' text file. It doesn't matter where, since the 'candidate_words.txt' file will be randomly shuffled anyway. 

In the `test` folder, you will see a text file called `target_words.txt`:

- The 'target_words.txt' file will contain the CORRECT spelling of each word contained in the 'incorrect_words.txt' text file, with each being on a new line in the same exact order that you inserted their incorrectly spelled counterparts in the 'incorrect_words.txt' text file. It is important that both the incorrectly and correctly spelled words are in the same order to be able to calculate the accuracy of the spell checker.

To view an example on how to create your own test cases, take a look at the files provided in either folder.

# How to Run the Program

Enter the folder's directory using your terminal. Then, simply run `python3 spellchecker.py`

- The only thing you will need to modify are the files in the `lib` and `test` folders if you want to try the program with your own test cases. The program does not need to be touched, unless you'd like to modify the global variable 'THRESHOLD', which is used as the threshold to find an incorrectly spelled word's closest approximation.
- The incorrectly spelled words in 'incorrect_words.txt' will be run through the program to find its closest lexical match from the `candidate_words.txt` text file using the Damerau-Levenshtein algorithm.
- The spellchecked words will then be, in order, cross checked against its intended counterparts in `target_words.txt` to calculate the overall accuracy of the spellchecking algorithm.

The results of the program will then be printed to your terminal.

## Dependencies
Ensure that you have `difflib` installed for python3.

## Final Words
Feel free to use or modify this program for your intended purposes!
