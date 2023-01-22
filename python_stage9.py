from tkinter import *

root = Tk()
root.title('YAHOO FINANCE CONTROLLER')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("800x400")

my_menu = Menu(root)
root.config(menu = my_menu)

Title = Label(root, text="WELCOME to FINANCE", font=("Courier 22 bold")).pack( side = TOP)

def our_comand():
    my_label = Label(root, text="You Clicked here!!").pack()
    
def file_new():
    hide_all_frames()
    file_new_frame.pack(fill="both", expand=1)
    my_label = Label(file_new_frame, text="You file edit!!").pack()
        
def edit_cut():
    hide_all_frames()
    edit_new_frame.pack(fill="both", expand=1)
    my_label = Label(edit_new_frame, text="You file edit!!").pack()
    
def edit_cut():
    hide_all_frames()
    edit_new_frame.pack(fill="both", expand=1)
    my_label = Label(edit_new_frame, text="You file edit!!").pack()

def hide_all_frames():
    file_new_frame.pack_forget()
    edit_new_frame.pack_forget()
    input_frame.pack_forget()
    input_frame2.pack_forget()
    L0.pack_forget()
    
def hide_all_control():
    file_new_frame.pack_forget()
    edit_new_frame.pack_forget()
    input_frame.pack_forget()
    
    
def input_control():
    hide_all_frames()
    input_frame.pack()
    L0.pack(side = LEFT)
    E0 = OptionMenu(input_frame, variable0, "one", "two", "three")
    E0.pack(side = RIGHT)

def input_control2():
    hide_all_frames()
    input_frame2.pack()
    L0.pack(side = LEFT)
    

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=file_new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_command(label="Copy", command=our_comand)

option_menu = Menu(my_menu)
my_menu.add_cascade(label="Option", menu=option_menu)
option_menu.add_command(label="Input", command=input_control)
option_menu.add_command(label="Find Next", command=our_comand)

variable0 = StringVar(root)
variable0.set("") # default value



file_new_frame = Frame(root, width=600, height=500, bg="red")
edit_new_frame = Frame(root, width=600, height=500, bg="blue")
input_frame = Frame(root, width=600, height=500, bg="green")

button_frame = Frame(root, width=600, height=500, bg="green")

button_op1 = Button(button_frame, text= "New Person", width= 20, command=input_control2).pack(side = LEFT, pady=20)
button_op2 = Button(button_frame, text= "Insert Stock", width= 20).pack(side = LEFT, pady=20)
button_op3 = Button(button_frame, text= "Save File", width= 20).pack(side = LEFT, pady=20)


button_frame.pack()


input_frame2 = Frame(root, width=600, height=500, bg="green")
L0 = Label(input_frame2, text="PERSON2")


root.mainloop()

