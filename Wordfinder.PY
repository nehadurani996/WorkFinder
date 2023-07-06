from Help_functions import *
import sys

if __name__ == "__main__":
   try:
    str_to_find=sys.argv[1]
    word_finder(str_to_find=str_to_find)
   except IndexError:
    print("The work not provided. Please provide the word as argument.\n"
    "Example prompt: WordFinder.py abc")

    
