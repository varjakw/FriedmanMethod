# Vigenere's Cipher - simple variant with repeating key.
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

ROOT = tk.Tk()
ROOT.withdraw()


def generateKey(plaintext, key):
    key = list(key)
    if len(plaintext) == len(key):
        return(key)
    else:
        for i in range(len(plaintext) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))


def encrypt(plaintext, key):
    cipher_text = []
    for i in range(len(plaintext)):
        x = (ord(plaintext[i]) + ord(key[i])) % 26 # Ei = (Pi + Ki) mod 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

def decrypt(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))


# the input dialog
#message = input("What's your Message?").upper()
#keyword = input("What's your Keyword?").upper()
#print("The Key will now be generated from your keyword")
#key = generateKey(message, keyword).upper()
#print("The Key is: " + key)
#ciphertext = encrypt(message, key).upper()
#print("The ciphertext is: " + ciphertext)
#plaintext = decrypt(ciphertext, key).upper()
#print("The plaintext is: " + plaintext)