"""
This line of code will take an input from the user using the input() function and print a greeting message.

print("Hello "+input("What is your name?")+"!")

"""

# name = input("What is your name?").__len__()
# print("Length of name "+str(name))

# name_length = len(name)
# print(name_length)

# print(len(input("What is your name?")))
import tkinter as tk


def run_band_generator_app():
    """Function to display greeting message when Run button is clicked"""
    print("Welcome to the Band Name Generator.\n")
    city_name = input("What's the name of the city you grew up in?\n")
    pet_name = input("What's your pet's name?\n")
    print("Your band name could be: " + city_name + " "+pet_name)

# Create the main window
root = tk.Tk()
root.title("Final Project")
root.geometry("300x150")

# Create a frame to hold the text and button inline
frame = tk.Frame(root)
frame.pack(pady=30)

# Create the first part of the text
label1 = tk.Label(frame, text="Click the ", font=("Arial", 12))
label1.pack(side=tk.LEFT)

# Create the Run button (smaller and inline)
run_button = tk.Button(
    frame, 
    text="Run", 
    command=run_band_generator_app,
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
    padx=8,
    pady=2
)
run_button.pack(side=tk.LEFT)

# Create the second part of the text
label2 = tk.Label(frame, text=" to run the final project you will build.:", font=("Arial", 12))
label2.pack(side=tk.LEFT)

# Start the GUI event loop
root.mainloop()
