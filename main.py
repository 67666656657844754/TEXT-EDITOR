from tkinter import*
from tkinter.filedialog import askopenfilename, asksaveasfilename


# Create the main window of the text editor.
root = Tk()
root.title("text editor")
root.geometry("650x550+90+90")
root.config(bg="white")


# Open a text file and load its contents into the editor.
def open_file(root, main):
    # Prompt the user to select a text file.
    fpath = askopenfilename(filetypes=[("Text files", "*.txt")])

    # Exit if the user cancels the dialog.
    if not fpath:
        return

    # Read the file and insert its content into the text widget.
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    main.delete(1.0, END)
    main.insert(END, content)

    # Update the window title to show the current file path.
    root.title(f"File: {fpath}")


# Save the current content of the editor to a text file.
def savef(root, main):
    # Ask the user where to save the file.
    fpath = asksaveasfilename(filetypes=[("Text files", "*.txt")])

    # Exit if the user cancels the save dialog.
    if not fpath:
        return

    # Write the editor content to the selected file.
    with open(fpath, "w") as f:
        content = main.get(1.0, END)
        f.write(content)

    # Update the title to reflect the saved file.
    root.title(f"File: {fpath}")


# Create a bottom panel for the buttons.
frame = Frame(root, relief=SOLID)
frame.pack(expand=True, fill="both", side=BOTTOM)

# Add buttons for saving and opening files.
save = Button(frame, text="save", command=lambda: savef(root, main))
openf = Button(frame, text="open", width=5, command=lambda: open_file(root, main))

# Arrange the buttons in the frame.
save.pack(expand=True, side=RIGHT, fill="both")
openf.pack(expand=True, side=LEFT, fill="both")


# Create the actual text area where the user types.
main = Text(root, font=("Arial", 10), relief=SOLID)
main.pack(expand=True, fill="both")


# Start the Tkinter event loop.
root.mainloop()
