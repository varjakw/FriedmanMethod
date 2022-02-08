import tkinter as tk
from tkinter import ttk, font

from tkinter import CENTER


class app:

    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Vigenére Cipher")
        self.menu()
        self.messagetext = None
        self.keywordtext = None

    def menu(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = tk.Frame(self.master, width=300, height=300)
        self.frame1.pack()
        def_font = font.Font(family='MS Sans Serif')
        self.uppertext1 = tk.Label(self.frame1, text="Vigenére Cipher", font=def_font)
        self.uppertext1.pack()
        def_font = font.Font(family='MS Sans Serif')
        self.vigenere_btn = tk.Button(self.frame1, text="Test the Vigenére Cipher", font=def_font,
                                      command=self.vigenere)
        self.vigenere_btn.pack()

    def vigenere(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame3 = tk.Frame(self.master, width=300, height=300)
        self.frame3.pack()
        def_font = font.Font(family='MS Sans Serif')
        self.uppertext2 = tk.Label(self.frame3, text="Vigenére Cipher", font=def_font)
        self.uppertext2.pack()
        self.menu_btn = tk.Button(self.frame3, text="Main Menu", font=def_font, command=self.menu)
        self.menu_btn.pack()
        self.message_label = tk.Label(self.frame3, text="Enter the message to encrypt", font=def_font)
        self.keyword_label = tk.Label(self.frame3, text="Enter the keyword to encrypt with", font=def_font)
        self.key_label = tk.Label(self.frame3, text="Generated Key", font=def_font)
        self.ciphertext_label = tk.Label(self.frame3, text="Encrypted Text", font=def_font)
        self.message_entry = tk.Entry(font=(def_font, 25))  # width handled by place()
        self.keyword_entry = tk.Entry(font=(def_font, 25))

        self.message_label.pack(padx=20, pady=20)
        self.message_entry.place(x=120, y=95, width=250, height=40)
        #self.message_entry.pack()
        self.keyword_label.pack(padx=60, pady=50)
        self.keyword_entry.place(x=120, y=190, width=250, height=40)
        #self.keyword_entry.pack(padx=10, pady=10)
        self.encrypt_btn = tk.Button(self.frame3, text="Encrypt", font=def_font, command=self.printstuff)
        self.encrypt_btn.pack()

        self.key = tk.Entry(font=(def_font, 25))
        self.ciphertext = tk.Entry(font=(def_font, 25))
        self.key.place(x=120, y=300, width=250, height=40)
        self.ciphertext.place(x=120, y=380, width=250, height=40)

    def printstuff(self):
        messagetext = self.message_entry.get()
        keywordtext = self.keyword_entry.get()
        print("message: " + messagetext)
        print("keyword: " + keywordtext)
        generatedkey = self.generatekey(messagetext, keywordtext)
        encryptedtext = self.encrypt(messagetext, generatedkey)
        self.key.insert(0, generatedkey)
        self.ciphertext.insert(0, encryptedtext)

    def generatekey(self, plaintext, key):
        key = list(key)
        if len(plaintext) == len(key):
            return (key)
        else:
            for i in range(len(plaintext) -
                           len(key)):
                key.append(key[i % len(key)])
        return ("".join(key))

    def encrypt(self, plaintext, key):
        cipher_text = []
        for i in range(len(plaintext)):
            x = (ord(plaintext[i]) + ord(key[i])) % 26  # Ei = (Pi + Ki) mod 26
            x += ord('A')
            cipher_text.append(chr(x))
        return ("".join(cipher_text))

    def decrypt(self, cipher_text, key):
        orig_text = []
        for i in range(len(cipher_text)):
            x = (ord(cipher_text[i]) -
                 ord(key[i]) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
        return "".join(orig_text)


root = tk.Tk()
app(root)
root.mainloop()


# Vigenere's Cipher - simple variant with repeating key.




# key = generateKey(message, keyword).upper()

# ciphertext = encrypt(message, key).upper()

# plaintext = decrypt(ciphertext, key).upper()




