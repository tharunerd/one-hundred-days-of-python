# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"  # Pleasant pastel background
FONT_TITLE = ("Ariel", 20, "italic")
FONT_WORD = ("Ariel", 30, "bold")

current_card = {}  # Stores the card currently being shown
to_learn = {}      # Stores all remaining cards

# ---------------------------- LOAD DATA ------------------------------- #
try:
    # Try loading the saved progress file
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # If progress file doesn't exist, load the original word list
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # If progress file exists, use that
    to_learn = data.to_dict(orient="records")

# ---------------------------- FUNCTIONS ------------------------------- #
def next_card():
    """Display the next random French word card."""
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Cancel the previous flip timer

    # Pick a random card from the list
    current_card = random.choice(to_learn)

    # Update card display to show French side
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    # Set a timer to flip the card after 3 seconds
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """Flip the current card to show the English translation."""
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    """Mark the current card as known and remove it from the learning list."""
    to_learn.remove(current_card)  # Remove from remaining words
    pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)  # Save progress
    next_card()  # Show next card


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy - Language Learning App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flip timer (initially set to flip after 3 seconds)
flip_timer = window.after(3000, func=flip_card)

# Canvas for card display
canvas = Canvas(width=500, height=400, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")  # French side
card_back_img = PhotoImage(file="images/card_back.png")    # English side
card_background = canvas.create_image(200, 263, image=card_front_img)  # Centered image
card_title = canvas.create_text(150, 150, text="", font=FONT_TITLE)
card_word = canvas.create_text(150, 263, text="", font=FONT_WORD)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Wrong button (user doesn't know the word)
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# Right button (user knows the word)
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)



# ---------------------------- START ------------------------------- #
next_card()  # Show first card
window.mainloop()
