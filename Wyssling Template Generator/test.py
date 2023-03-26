import tkinter as tk

def get_input():
    user_input = entry.get()
    print("User input:", user_input)

# Create a new Tkinter window
window = tk.Tk()
window.title("Wyssling Template Generator")
window.minsize(400,300)
window.resizable(False,False)

# Add a label to the window
label = tk.Label(window, text="Enter your name:")
label.pack()

# Add a text input field to the window
entry = tk.Entry(window)
entry.pack()

# Add a button to the window
button = tk.Button(window, text="Submit", command=get_input)
button.pack()

# Run the Tkinter event loop
window.mainloop()