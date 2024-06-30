from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.geometry('700x550')
root.config(bg='#d3f3f5')
root.title('Contact Book')
root.resizable(0, 0)

contactlist = []

Name = StringVar()
Number = StringVar()
Search = StringVar()

frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Arial', 14), bg="#f0fffc", width=20, height=20, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

def Selected():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])

def AddContact():
    if Name.get() != "" and Number.get() != "":
        contactlist.append([Name.get(), Number.get()])
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Added New Contact")
    else:
        messagebox.showerror("Error", "Please fill in the information")

def UpdateDetail():
    if Name.get() and Number.get():
        contactlist[Selected()] = [Name.get(), Number.get()]
        messagebox.showinfo("Confirmation", "Successfully Updated Contact")
        EntryReset()
        Select_set()
    else:
        if len(select.curselection()) == 0:
            messagebox.showerror("Error", "Please Select the Name")
        else:
            messagebox.showerror("Error", "Please fill in the information")

def Delete_Entry():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno('Confirmation', 'Do you want to delete the selected contact?')
        if result == True:
            del contactlist[Selected()]
            Select_set()
            EntryReset()
    else:
        messagebox.showerror("Error", "Please select a contact")

def VIEW(event):
    if len(select.curselection()) != 0:
        NAME, PHONE = contactlist[Selected()]
        Name.set(NAME)
        Number.set(PHONE)

def EXIT():
    root.destroy()

def EntryReset():
    Name.set("")
    Number.set("")

def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)

def SearchContact():
    search_term = Search.get().lower()
    search_results = [contact for contact in contactlist if search_term in contact[0].lower()]
    if search_results:
        select.delete(0, END)
        for name, _ in search_results:
            select.insert(END, name)
    else:
        messagebox.showinfo("Search Result", "No matching contacts found.")

# Add hover effect function
def on_enter(event, btn):
    btn.config(bg='#e57373')

def on_leave(event, btn):
    btn.config(bg='#e8c1c1')

# Function to load and resize icons
def load_icon(path, size=(32, 32)):
    img = Image.open(path)
    img = img.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

# Load icons
add_icon = load_icon('add-user.png')  # Update with the actual path to your icon
update_icon = load_icon('loop.png')  # Update with the actual path to your icon
delete_icon = load_icon('contact.png')  # Update with the actual path to your icon
search_icon = load_icon('search-user.png')  # Update with the actual path to your icon
exit_icon = load_icon('arrow.png')  # Update with the actual path to your icon

# Define button styles
button_style = {'font': ('Arial', 12, 'bold'), 'bg': '#e8c1c1', 'relief': 'ridge', 'borderwidth': 2}

# Add Labels and Entry widgets
Label(root, text="Name", font='arial 12 bold', bg="#d3f3f5").place(x=30, y=20)
Entry(root, textvariable=Name, font=('Arial', 12)).place(x=150, y=20)

Label(root, text="Phone", font='arial 12 bold', bg="#d3f3f5").place(x=30, y=70)
Entry(root, textvariable=Number, font=('Arial', 12)).place(x=150, y=70)

Label(root, text="Search", font='arial 12 bold', bg="#d3f3f5").place(x=30, y=400)
Entry(root, textvariable=Search, font=('Arial', 12)).place(x=150, y=400)

# Add Buttons with icons
btn_add = Button(root, text="Add", image=add_icon, compound=LEFT, **button_style, command=AddContact)
btn_add.place(x=30, y=120)
btn_add.bind("<Enter>", lambda event: on_enter(event, btn_add))
btn_add.bind("<Leave>", lambda event: on_leave(event, btn_add))

btn_update = Button(root, text="Update", image=update_icon, compound=LEFT, **button_style, command=UpdateDetail)
btn_update.place(x=30, y=170)
btn_update.bind("<Enter>", lambda event: on_enter(event, btn_update))
btn_update.bind("<Leave>", lambda event: on_leave(event, btn_update))

btn_delete = Button(root, text="Delete", image=delete_icon, compound=LEFT, **button_style, command=Delete_Entry)
btn_delete.place(x=30, y=220)
btn_delete.bind("<Enter>", lambda event: on_enter(event, btn_delete))
btn_delete.bind("<Leave>", lambda event: on_leave(event, btn_delete))

btn_search = Button(root, text="Search", image=search_icon, compound=LEFT, **button_style, command=SearchContact)
btn_search.place(x=30, y=450)
btn_search.bind("<Enter>", lambda event: on_enter(event, btn_search))
btn_search.bind("<Leave>", lambda event: on_leave(event, btn_search))

btn_exit = Button(root, text="Exit", image=exit_icon, compound=LEFT, **button_style, command=EXIT)
btn_exit.place(x=30, y=320)
btn_exit.bind("<Enter>", lambda event: on_enter(event, btn_exit))
btn_exit.bind("<Leave>", lambda event: on_leave(event, btn_exit))

# Bind the Listbox select event to VIEW function
select.bind('<<ListboxSelect>>', VIEW)

Select_set()
root.mainloop()
