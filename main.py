import tkinter as tk
from tkinter import ttk, font

from tkinter import CENTER


class app:

    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Friedman's Method")
        self.menu()

    def menu(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = tk.Frame(self.master, width=300, height=300)
        self.frame1.pack()
        def_font = font.Font(family='MS Sans Serif')
        self.uppertext1 = tk.Label(self.frame1, text="Friedman's Method and the Vigenére Cipher", font=def_font)
        self.uppertext1.pack()
        self.friedman_btn = tk.Button(self.frame1, text="Test Friedman's Method",font=def_font, command=self.friedman)
        self.friedman_btn.pack()
        def_font = font.Font(family='MS Sans Serif')
        self.vigenere_btn = tk.Button(self.frame1, text="Test the Vigenére Cipher", font=def_font, command=self.vigenere)
        self.vigenere_btn.pack()

    def friedman(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = tk.Frame(self.master, width=300, height=300)
        self.frame2.pack()
        def_font = font.Font(family='MS Sans Serif')
        self.reg_txt2 = tk.Label(self.frame2, text="Friedman's Method on Vigenére Cipher", font=def_font)
        self.reg_txt2.pack()
        self.menu_btn = tk.Button(self.frame2, text="Go to Main Menu", font=def_font, command=self.menu)
        self.menu_btn.pack()

    def vigenere(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame3 = tk.Frame(self.master, width=300, height=300)
        self.frame3.pack()
        def_font = font.Font(family='MS Sans Serif')
        self.uppertext2 = tk.Label(self.frame3, text="Vigenére Cipher",font=def_font)
        self.uppertext2.pack()
        self.menu_btn = tk.Button(self.frame3, text="Main Menu", font=def_font, command=self.menu)
        self.menu_btn.pack()
        self.message_entry = tk.Entry(font=(def_font,25)) #width handled by place()
        self.keyword_entry = tk.Entry(font=(def_font,25))
        self.message_entry.place(x=30, y=100, width=250, height=40)
        self.keyword_entry.place(x=30, y=160, width=250, height=40)
        #messagetext = self.message_entry.get()
        #keywordtext = self.keyword_entry.get()
        #self.encrypt_btn = tk.Button(self.frame3, text="Encrypt", font=def_font,command=print(messagetext + keywordtext))
        #self.encrypt_btn.pack()


root = tk.Tk()
app(root)
root.mainloop()
