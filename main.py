from tkinter import *
from tkinter import messagebox
import pandas as pd

FONT_TEXT = ('Arial', 60, 'bold')
FONT_TITLE = ('Arial', 30, 'italic')
BG = '#f4f4f4'

# ------------------------- CUSTOM FUNCTIONS ------------------------- #
def read_file():
    try:
        data_ = pd.read_csv('data/words_to_learn.csv')
        card_ = data_.sample()
    except (FileNotFoundError, ValueError):
        data_ = pd.read_csv('data/french_words.csv')
        card_ = data_.sample()
    return data_, card_

# ------------------------- BUTTON FUNCTIONS ------------------------- #
def next_card():
    global flip_timer, current_card, df, window
    window.after_cancel(flip_timer)

    try:
        current_card = df.sample()
    except ValueError:
        retry = messagebox.askretrycancel(title='Completed', message="Congratulations!\n"
                                                                     "You've master 100 French words!\n"
                                                                     "Do you wish to retry the game?")
        if retry:
            df, current_card = read_file()
        else:
            current_card = None
            window.destroy()
            return

    canvas.itemconfig(card, image=front_card_img)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_text, text=current_card.iloc[0]['French'], fill='black')
    flip_timer = window.after(3000, show_answer)


# noinspection PyUnresolvedReferences
def show_answer():
    canvas.itemconfig(card, image=back_card_img)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_text, text=current_card.iloc[0]['English'], fill='white')

def correct():
    global current_card, df
    df = df.drop(current_card.index.values[0])
    df.to_csv('data/words_to_learn.csv', index=False)
    next_card()

# ----------------------------- UI SETUP ----------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg=BG)
flip_timer = window.after(3000, show_answer)
df, current_card = read_file()

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
like_btn = Button(image=like_img, borderwidth=0, highlightthickness=0, bd=0, command=correct)
unlike_btn = Button(image=unlike_img, borderwidth=0, highlightthickness=0, bd=0, command=next_card)
like_btn.grid(row=1, column=1)
unlike_btn.grid(row=1, column=0)

next_card()

window.mainloop()
