# Vigenere's Cipher - simple variant with repeating key.
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

ROOT = tk.Tk()
ROOT.withdraw()


def generateKey(plaintext, keyword):
    keyword = list(keyword)
    if len(plaintext) == len(keyword):
        return (keyword)
    else:
        for i in range(len(plaintext) - len(keyword)):
            keyword.append(keyword[i % len(keyword)])
            return "".join(keyword)


# the input dialog
message = input("What's your Message?")
key = input("What's your Keyword?")
print("The Key will now be generated from your keyword")
generateKey(message, key)
print("The Key is: " + key)
