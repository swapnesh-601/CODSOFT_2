"""
Password Generator Application
using tkinter GUI.
You input the number of characters
required for your password and it generates
password using random integer converted to their ascii characters
"""

from tkinter import *
from random import randint
from tkinter import messagebox


# create the tkinter module
root = Tk()
root.title('Password Generator by Charles Lughas')
root.geometry('500x500')
root.iconbitmap()
root.configure(background="#190032")


# functions to generate password and copy to clipboard
def generate_pass():
    """
    generate random strong password
    collecting password length of characters
    and looping through the range of random integers before
    converting each output to their ascii values
    """
    # clear entry box
    pass_entry.delete(0, END)

    # get password length
    pass_length = int(my_entry.get()) # convert to integer

    # create a variable to hold the password
    the_password = ""

    # loop through the password length
    for item in range(pass_length):
        # generate random int between 33 to 126
        # and convert to the ascii character
        # before adding it to get password for each loop
        the_password += chr(randint(33, 126))

    # display password to the screen
    pass_entry.insert(0, the_password)


def copy_pass():
    """
    function to copy generated password
    to clipboard and give an alert
    """
    # clear the clipboard
    root.clipboard_clear()
    # copy to clipboard
    root.clipboard_append(pass_entry.get())
    popup()
    
    
def popup():
    """
    function to alert that text has
    been copied to clipboard
    """
    messagebox.showinfo("copy password", "password is copied to clipboard")



# create label frame for password length
label_frame = LabelFrame(root, text="How many characters?", font=("Helvetic", 20, "normal"))
label_frame.pack(pady=20)

# create entry box to assign label frame
my_entry = Entry(label_frame, font=("Helvetica", 25))
my_entry.pack(padx=20, pady=20)

# create label frame for output password
output_label_frame = LabelFrame(root, text="Your Password!", font=("Helvetic", 20, "bold"))
output_label_frame.pack(pady=10)

# create entry box from returned password
pass_entry = Entry(output_label_frame, text="", font=('Helvetica', 25), bd=0, bg="systemButtonFace")
pass_entry.pack(pady=20)

# create button frame
btn_frame = Frame(root, background="#190032")
btn_frame.pack(pady=20)

# create password generator buttons
gen_btn = Button(btn_frame, fg="green", text="Generate Strong Password", command=generate_pass)
gen_btn.grid(column=0, row=0, padx=20)

clip_btn = Button(btn_frame, fg="red", text="Copy to Clipboard", command=copy_pass)
clip_btn.grid(column=1, row=0, padx=10)




root.mainloop()