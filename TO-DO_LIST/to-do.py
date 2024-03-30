'''
Python Program to create 
a To-do list application using Tkinter GUIs
'''
import os
import pickle

# import all components
# from the tkinter library
from tkinter import *
from tkinter.font import Font

# import filedialog module
from tkinter import filedialog

# create the tkinter module
root = Tk()
root.title('To-Do List by Charles Lughas')
root.iconbitmap()
root.geometry("700x500")
root.configure(background='#48C94E')

# define my fonts
my_font = Font(
    family='Chiller Regular',
    size=30,
    weight='normal'
)

# create frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# create list of todo
my_list = Listbox(
    my_frame,
    font=my_font,
    width=25,
    height=5,
    bg= "SystemButtonFace",
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground= "#C948C4",
    activestyle="none"
)
my_list.pack(side="left", fill="both")

# create default list
dummy_list = ["lunch", "dance", "go to temple", "swimming"]

# Add the default list to listbox
for task in dummy_list:
    my_list.insert(END, task)

# create functions
def add_task():
    '''function to add task to the list'''
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def delete_task():
    '''function to delete task to the list'''
    my_list.delete(ANCHOR)

def cross_out_task():
    '''function to cross out task to the list'''
    # cross out task
    my_list.itemconfig(
        my_list.curselection(),
        fg= "#dedede"
    )
    
     # get rid of selected task
    my_list.selection_clear(0, END)

def uncross_out_task():
    '''function to uncross out task to the list'''
    # uncross out task
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646"
    )
    # get rid of selected task
    my_list.selection_clear(0, END)
    
def delete_crossed_task():
    '''function to delete crossed out task to the list'''
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))

        else:
            count += 1


# Create menu functions
def save_list():
    '''function to save the list using filedialog module'''
    path = os.getcwd() # get file directory

    # create file name to save file
    file_name = filedialog.asksaveasfilename(
        initialdir= "path",
        title="Save File",
        filetypes=(
            ("Dat Files", ".dat"),
            ("All Files", "*.*")
        )
    )

    # check if file has ".dat" extension and add it
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'

    # delete crossed out task before saving
    delete_crossed_task()

    # grab all the tasks from the list
    tasks = my_list.get(0, END)

    # open the file
    output_file = open(file_name, 'wb')

    # actually add the tasks to the file using pickle
    pickle.dump(tasks, output_file)


def del_list():
    '''function to delete the entire list'''
    my_list.delete(0, END)
 

def open_list():
    '''
    function to open an existing to-do
    from file explorer
    '''
    # open file in file explorer
    file_name = filedialog.askopenfilename(
        initialdir= "path",
        title="Open File",
        filetypes=(
            ("Dat Files", ".dat"),
            ("All Files", "*.*")
        )
    )
    if file_name:
        # delete currently open list
        my_list.delete(0, END)

        # open the file
        file_input = open(file_name, 'rb')

        # load the data from the file
        stuff = pickle.load(file_input)

        # output stuff to the screen
        for task in stuff:
            my_list.insert(END, task)





# create scrollbar widget
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side="right", fill="both")


# Add scrollbar to my list
my_list.config(yscrollcommand=my_scrollbar)
my_scrollbar.config(command=my_list.yview)


# create entry box to add tasks to the list using Entry widget
my_entry = Entry(root, font=("Helvetica", 20), width=30)
my_entry.pack(pady=20)


# create a button frame
button_frame = Frame(root, bg='#48C94E')
button_frame.pack(pady=20)

# Add some buttons 
delete_button = Button(button_frame, background='#C948C4', text= "Delete Task",  fg='white',command=delete_task)
add_button = Button(button_frame, background='#C948C4', text= "Add Task", fg='white',command=add_task)
cross_out_button = Button(button_frame, background='#C948C4', text="Cross-Out Task", fg='white', command=cross_out_task)
uncross_out_button = Button(button_frame, background='#C948C4', text="Uncross-Out Task", fg='white', command=uncross_out_task)
delete_crossed_button = Button(button_frame, background='#C948C4', text="Delete Crossed-Out Task", fg='white', command=delete_crossed_task)

# make buttons to be in the same grid
delete_button.grid(row=0, column=0, padx=20)
add_button.grid(row=0, column=1, padx= 20)
cross_out_button.grid(row=0, column=2, padx= 20)
uncross_out_button.grid(row=0, column=3, padx= 20)
delete_crossed_button.grid(row=0, column=4, padx=20)


# create menu to root application
my_menu = Menu(root)
root.config(menu=my_menu)

# create and add file menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

# Add drop down items to file menu
file_menu.add_command(label="Open...", command=open_list)
file_menu.add_command(label="Save list", command=save_list)
file_menu.add_command(label="Clear list", command=del_list)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# create and add help menu
help_menu = Menu(my_menu)
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")
help_menu.add_command(label="Contact")





# calling the mainloop in tk methods
root.mainloop()
