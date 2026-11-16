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
["Json files", "*.json"], 
["PythonFille", "*.py"], 
["All files", "*.*"]
]


# Open file
def open_file(root, main):
    try:
        fpath = askopenfilename(
            filetypes=[(fltype[0]),  (fltype[1]), (fltype[2]), (fltype[3]),   (fltype[4])])

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
def save_file(root, main):
    try:
        fpath = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[(fltype[0]),  (fltype[1]), (fltype[2]), (fltype[3]),   (fltype[4])])

        if not fpath:
            return

        with open(fpath, "w", encoding="utf-8") as f:
            content = main.get(1.0, END)
            f.write(content)

        root.title(f"File: {fpath}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def new_fille(root, main):
    chkt = main.get("1.0", END).strip()
    if chkt == "":
        return
    else:
        yn = messagebox.askquestion("?", "Do you want to save the previous file before the new one")
    
    if yn == "yes":
        save_file(root, main)
        main.delete(1.0, END)
        root.title("New Fille") 


    else:
          main.delete(1.0, END)
          root.title("New Fille")        



# Bottom panel
frame = Frame(root)
frame.pack(expand=True, fill="x", side=BOTTOM)

# Buttons
save = Button(frame, text="Save File", command=lambda: save_file(root, main))
openf = Button(frame, text="Open File", command=lambda: open_file(root, main))
new_fb =  Button(frame, text="New file", command=lambda: new_fille(root, main))

new_fb.pack(expand=True, fill="x")
save.pack(expand=True, side=BOTTOM, fill="x")
openf.pack(expand=True, side=BOTTOM, fill="x")

# Text editor
main = Text(root, font=("Arial", 15), relief=SOLID)
main.pack(expand=True, fill="both")

# Main loop
root.mainloop()
