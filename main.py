BACKGROUND_COLOR = "#B1DDC6"

import tkinter as tk
from tkinter import messagebox
import pandas as pd

last_word = None
correct_words = []

def next_card_right():
    global last_word
    global correct_words
    global french_words
    if last_word is not None:
        mask = (french_words['French'] == last_word['French']) & (french_words['English'] == last_word['English'])
        french_words = french_words[~mask]
        correct_words.append(last_word)
    new_word = french_words.sample(1)
    new_word = {'French': new_word.iloc[0]['French'],
     'English': new_word.iloc[0]['English']}
    last_word = new_word
    canvas.itemconfig(flashcard, image=card_front_img)
    canvas.itemconfig(title_card, text="French")
    canvas.itemconfig(word_card, text=new_word['French'])
    window.after(3000, flip_card, new_word)

def next_card_wrong():
    new_word = french_words.sample(1)
    new_word = {'French': new_word.iloc[0]['French'],
     'English': new_word.iloc[0]['English']}
    global last_word
    last_word = new_word
    canvas.itemconfig(flashcard, image=card_front_img)
    canvas.itemconfig(title_card, text="French")
    canvas.itemconfig(word_card, text=new_word['French'])
    window.after(3000, flip_card, new_word)
    
def flip_card(word):
    canvas.itemconfig(flashcard, image=card_back_img)
    canvas.itemconfig(title_card, text="English")
    canvas.itemconfig(word_card, text=word['English'])
    
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tk.PhotoImage(file="/Users/anastasialinchik/Angela/flash-card-project-start/images/card_front.png")
card_back_img = tk.PhotoImage(file="/Users/anastasialinchik/Angela/flash-card-project-start/images/card_back.png")
flashcard = canvas.create_image(400, 263, image=card_front_img)


title_card = canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
french_words = pd.read_csv("/Users/anastasialinchik/Angela/flash-card-project-start/data/french_words.csv")
word_card = canvas.create_text(400, 263, text='Word', font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

#---------------------------------Buttons---------------------------------#
cross_image = tk.PhotoImage(file="/Users/anastasialinchik/Angela/flash-card-project-start/images/wrong.png")
wrong_button = tk.Button(image=cross_image, command=next_card_wrong, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, borderwidth=0)
wrong_button.grid(row=1, column=0)

check_image = tk.PhotoImage(file="/Users/anastasialinchik/Angela/flash-card-project-start/images/right.png")
right_button = tk.Button(image=check_image, command=next_card_right, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, borderwidth=0)
right_button.grid(row=1, column=1)





window.mainloop()
