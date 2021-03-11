#! /usr/bin/python3

import pyperclip

def duplicate_count(text):
    text = text.lower()
    dups = 0
    for char in set(text):
        if text.count(char) > 1:
            dups += 1
    return dups

text = pyperclip.paste()
count = duplicate_count(text)
pyperclip.copy(count)