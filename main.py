from tkinter import *
import pandas as pd

FONT_TEXT = ('Arial', 60, 'bold')
FONT_TITLE = ('Arial', 30, 'italic')
BG = '#f4f4f4'
df = pd.read_csv('data/french_words.csv')
current_card = df.sample()

# ------------------------- CUSTOM FUNCTIONS ------------------------- #
def next_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = df.sample()
    canvas.itemconfig(card, image=front_card_img)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_text, text=current_card.iloc[0]['French'], fill='black')
    flip_timer = window.after(3000, show_answer)

def show_answer():
    canvas.itemconfig(card, image=back_card_img)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_text, text=current_card.iloc[0]['English'], fill='white')

# ------------------------- BUTTON FUNCTIONS ------------------------- #

# ----------------------------- UI SETUP ----------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg=BG)
flip_timer = window.after(3000, show_answer)

# Images
front_card_img = PhotoImage(file='images/front_card.png')
back_card_img = PhotoImage(file='images/back_card.png')
like_img = PhotoImage(file='images/like_btn.png')
unlike_img = PhotoImage(file='images/unlike_btn.png')

# Canvas
canvas = Canvas(width=700, height=500, highlightthickness=0)
card = canvas.create_image(350, 250, image=front_card_img)
card_title = canvas.create_text(350, 150, text='', font=FONT_TITLE)
card_text = canvas.create_text(350, 250, text='', font=FONT_TEXT)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
like_btn = Button(image=like_img, borderwidth=0, highlightthickness=0, bd=0, command=next_card)
unlike_btn = Button(image=unlike_img, borderwidth=0, highlightthickness=0, bd=0, command=next_card)
like_btn.grid(row=1, column=1)
unlike_btn.grid(row=1, column=0)

next_card()

window.mainloop()
