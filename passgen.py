#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter
import random

root = tkinter.Tk()
root.resizable(width=False, height=False)
root.title("Password generator")
root.geometry("420x350+450+200")
text_box = tkinter.Text(height=15, width=50)

len_entry = tkinter.Entry(width=10, justify='center')
len_entry.insert(0, "24")
len_entry.grid(row=1, column=1, padx=1, pady=5)

len_label = tkinter.Label(text="Password length")
len_label.grid(row=1, column=0, padx=5, sticky="w")

chars = '+-/%*}{)(|!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


def erase_field():
    text_box.delete("1.0", "end")


def get_password():
    password = ""
    for i in range(int(len_entry.get())):
        password += random.choice(chars)
    text_box.insert("end", password)


def copy_clipboard():
    root.clipboard_clear()
    txt = text_box.get("1.0", "end")
    root.clipboard_append(txt)


pass_button = tkinter.Button(
    text="Get password", bg="#e6e6e6", command=get_password)
pass_button.grid(row=2, column=0, padx=5, pady=5, sticky="w")

erase_button = tkinter.Button(
    text="Erase all", bg="#e6e6e6", command=erase_field)
erase_button.grid(row=2, column=1, padx=15, pady=5, sticky="w")

copy_button = tkinter.Button(
    text="Copy to clipboard", bg="#e6e6e6", command=copy_clipboard)
copy_button.grid(row=2, column=2, sticky="w")

text_box.grid(row=4, column=0, sticky="nsew", columnspan=3)

scroll_bar = tkinter.Scrollbar(root, command=text_box.yview)
scroll_bar.grid(row=4, column=4, sticky="nsew")
text_box.configure(yscrollcommand=scroll_bar.set)

root.mainloop()