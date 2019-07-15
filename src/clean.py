#!/usr/bin/python3
import sys

CHARS = "abcdefghijklmnopqrstuvwxyz"

def clean_word(word):
    result = ""
    for c in word.lower():
        if c in CHARS:
            result += c
        else:
            result += '_'
    return result

def main():
    if len(sys.argv) < 2:
        print("one parameter required")
        return
    
    word = sys.argv[1]
    print(clean_word(word))

main()