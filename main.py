from tkinter import *
import pandas as pd

FONT_TEXT = ('Arial', 60, 'bold')
FONT_TITLE = ('Arial', 30, 'italic')
BG = '#f4f4f4'
df = pd.read_csv('data/french_words.csv')

# ------------------------- CUSTOM FUNCTIONS ------------------------- #

# ------------------------- BUTTON FUNCTIONS ------------------------- #

# ----------------------------- UI SETUP ----------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg=BG)

# Images
front_card_img = PhotoImage(file='images/front_card.png')
back_card_img = PhotoImage(file='images/back_card.png')
like_img = PhotoImage(file='images/like_btn.png')
unlike_img = PhotoImage(file='images/unlike_btn.png')

# Canvas
canvas = Canvas(width=700, height=500, highlightthickness=0)
canvas.create_image(350, 250, image=front_card_img)
title_text = canvas.create_text(350, 150, text='French', font=FONT_TITLE)
word_text = canvas.create_text(350, 250, text='trouve', font=FONT_TEXT)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
like_btn = Button(image=like_img, borderwidth=0, highlightthickness=0, bd=0, command=new_vocab)
unlike_btn = Button(image=unlike_img, borderwidth=0, highlightthickness=0, bd=0, command=new_vocab)
like_btn.grid(row=1, column=1)
unlike_btn.grid(row=1, column=0)

window.mainloop()
