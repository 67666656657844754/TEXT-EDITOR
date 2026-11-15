
from tkinter import*
from tkinter.filedialog import askopenfilename, asksaveasfilename


root = Tk()
root.title("text editor") 
root.geometry("650x550+90+90")
root.config(bg="white")





def open_file(root, main):
    

    fpath = askopenfilename(filetypes=[("Text files", "*.txt")] )
    
    if not fpath:
        return
     
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
     
    main.delete(1.0, END)
    main.insert(END, content)

   
    root.title(f"File: {fpath}")

def savef(root, main):
    
    fpath = asksaveasfilename(filetypes=[("Text files", "*.txt")])


    if not fpath:
        return

    with open(fpath, "w") as f:
        content = main.get(1.0, END)
        f.write(content)
    rootfb.title(f"File: {fpath}")



frame = Frame(root, relief=SOLID)
frame.pack(expand=True, fill="both", side=BOTTOM)
save = Button(frame, text="save", command=lambda: savef(root, main))
openf = Button(frame, text="open", width=5, command=lambda: open_file(root, main))
save.pack(expand=True, side=RIGHT, fill="both")
openf.pack(expand=True, side=LEFT, fill="both")



main = Text(root, font=("Arial", 10), relief=SOLID)
main.pack(expand=True, fill="both")



root.mainloop()
