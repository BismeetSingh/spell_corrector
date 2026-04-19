"""

In this optional step your goal is to track the time taken to suggest corrections to a list of words and present the correction and then calculate the time take and words per second, i.e.:

 % ./ccspell speiling misteke executionw mekanism coding chalenges
speiling spelling
misteke mistake
executionw execution
mekanism mechanism
coding coding
chalenges challenges
Time : 20.026833ms 299.6 words per second
"""
import os
import sys

# Add the project root directory to the Python path
# so that absolute imports from 'src' work when running this script directly

from src.main import SpellChecker
import time
import argparse

def run(words):
    spell_checker = SpellChecker()
    start_time = time.time()
    with open(words[0], 'r') as f:
        words = f.readlines()
    for word in words:
        print(word.strip(), spell_checker.correct_word(word.strip()))
    end_time = time.time()
    print("Time :", (end_time - start_time) * 1000, "ms", 1 / (end_time - start_time), "words per second")

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("file_path", nargs="+", help="Words to correct")
    args = arg_parser.parse_args()
    run(args.file_path)