
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Main window
root = Tk()
root.title("Text Editor")
root.geometry("650x550+90+90")
root.config(bg="white")


fltype = [
["Text files", "*.txt"],
["Markdown files", "*.md"], 
["All files", "*.*"]
]

# Open file
def open_file(root, main):
    try:
        fpath = askopenfilename(
            filetypes=[(fltype[0]),  (fltype[1]), (fltype[2])])

        if not fpath:
            return

        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        main.delete(1.0, END)
        main.insert(END, content)

        root.title(f"File: {fpath}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Save file
def savef(root, main):
    try:
        fpath = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[(fltype[0]),  (fltype[1]), (fltype[2])])

        if not fpath:
            return

        with open(fpath, "w", encoding="utf-8") as f:
            content = main.get(1.0, END)
            f.write(content)

        root.title(f"File: {fpath}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Bottom panel
frame = Frame(root, relief=SOLID)
frame.pack(expand=True, fill="both", side=BOTTOM)

# Buttons
save = Button(frame, text="Save", command=lambda: savef(root, main))
openf = Button(frame, text="Open", command=lambda: open_file(root, main))

save.pack(expand=True, side=RIGHT, fill="both")
openf.pack(expand=True, side=LEFT, fill="both")

# Text editor
main = Text(root, font=("Arial", 15), relief=SOLID)
main.pack(expand=True, fill="both")

# Main loop
root.mainloop()
