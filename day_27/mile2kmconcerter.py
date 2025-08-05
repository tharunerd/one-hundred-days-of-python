# ```python


from tkinter import *

def convert_miles_to_km():
    miles = float(mile_input.get())
    km = float(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=80, pady=40)

# Entry
mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)

# Labels
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Button
calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
