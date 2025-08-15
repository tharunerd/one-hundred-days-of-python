# Import everything from tkinter for GUI and requests for API calls
from tkinter import *
import requests

# Function to fetch a Kanye quote from the API
def get_quote():
    # Send a GET request to the Kanye REST API
    response = requests.get("https://api.kanye.rest")
    # If there is any error (like 404 or server down), this will stop the program
    response.raise_for_status()
    # Convert the API response to a Python dictionary
    data = response.json()
    # Extract the "quote" value from the dictionary
    quote = data["quote"]
    # Update the text on the canvas to display the quote
    canvas.itemconfig(quote_text, text=quote)

# ------------------- GUI SETUP -------------------

# Create the main window
window = Tk()
window.title("Kanye Says...")  # Set the window title
window.config(padx=50, pady=50)  # Add padding around the window

# Create a canvas widget to hold background and text
canvas = Canvas(width=300, height=414)

# Load the background image
background_img = PhotoImage(file="background.png")
# Place the background image in the middle of the canvas
canvas.create_image(150, 207, image=background_img)

# Add placeholder text for the quote (centered)
quote_text = canvas.create_text(
    150, 207,                          # Position in the middle
    text="Kanye Quote Goes HERE",      # Initial text before API fetch
    width=250,                         # Wrap text so it doesn't overflow
    font=("Arial", 30, "bold"),        # Styling for the text
    fill="white"                       # White text color
)

# Add the canvas to the window
canvas.grid(row=0, column=0)

# Load the Kanye button image
kanye_img = PhotoImage(file="kanye.png")
# Create a button with the Kanye image, no border highlight, runs get_quote() when clicked
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# Position the button below the canvas
kanye_button.grid(row=1, column=0)

# Keep the window open until the user closes it
window.mainloop()
