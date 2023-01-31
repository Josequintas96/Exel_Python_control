from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
from python_stage8 import control_Group
from python_stage5 import Group
from python_stage10 import *


root = Tk()
root.title('YAHOO FINANCE CONTROLLER')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("800x600")

my_menu = Menu(root)
root.config(menu = my_menu)

GroupX = Group()
control_Group(GroupX)

Title = Label(root, text="WELCOME to FINANCE", font=("Courier 22 bold")).pack( side = TOP)

def print_value(Group_var):
    ent1 = b1_variable0.get() #person variable
    print(ent1)
    ent2 = b1_entry2.get() #stock variable
    print(ent2)
    b1_entry2.delete(0,END)
    ent3 = b1_entry3.get()  #price variable
    print(ent3)
    b1_entry3.delete(0,END) 
    # ent2_5 = b1_entry2_5.get()  #price variable
    # print(ent2_5)
    # b1_entry2_5.delete(0,END) 
    ent4 = b1_entry4.get() #quantity variable
    print(ent4)
    b1_entry4.delete(0,END) 
    ent5 = b1_entry5.get() #date variable
    print(ent5)
    b1_entry5.delete(0,END)
    if Group_var.Group_stock_verification(ent2):
        result1 = Group_var.Group_insert_Stock(ent1, ent2, ent3, ent4, ent5)
        if result1:
            messagebox.showinfo("SUCCEED", "Succeed")
        else:
            messagebox.showerror("error", "Wrong Input")
    else:
        messagebox.showerror("error", "STOCK MAY NOT EXIST")
        
def Add_person(Group_var, List):
    ent1 =  b2_entry.get() #name variable
    print(ent1)
    b2_entry.delete(0,END)
    ent2 = b2_entry2.get()  #acronym variable
    print(ent2)
    b2_entry2.delete(0,END) 
    result2 = Group_var.Group_create_person(ent1)
    Group_var.Group_add_person_acronym(ent2, result2-1)
    Group_var.Group_command_action(3)
    List.append(ent1)
    # if result1:
    #     messagebox.showinfo("SUCCEED", "Succeed")
    # else:
    #     messagebox.showerror("error", "Wrong Input")
    print(List)
        

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
    button1_frame.pack_forget()
    button2_frame.pack_forget()
    button3_frame.pack_forget()
    # b1_label.pack_forget()
    
def hide_all_control():
    file_new_frame.pack_forget()
    edit_new_frame.pack_forget()
    input_frame.pack_forget()
    
    
def input_control():
    hide_all_frames()
    input_frame.pack()
    b1_label.pack()
    E0 = OptionMenu(input_frame, b1_variable0, "one", "two", "three")
    E0.pack()

def button1_control(Group_var):
    hide_all_frames()
    button1_frame.pack(padx=20, pady = 20)
    
    # pp_l = Group_var.Group_ret_list_persons()
    # b1_p_list.configure( *pp_l )
    
    b1_f1.pack( pady=6, expand=True)
    b1_p_list['menu'].delete(0, 'end')
    pp_l = Group_var.Group_ret_list_persons()
    # var = StringVar()
    for x0 in pp_l:
        b1_p_list['menu'].add_command(label=x0, command= lambda x= x0: b1_variable0.set(x))
    b1_label.pack( padx=9, side=LEFT)
    b1_p_list.pack( padx=9, side=RIGHT)
    
    # b1_space.pack()
    b1_f2.pack( pady=6, expand=True)
    b1_label2.pack( padx=9, side=LEFT)
    b1_entry2.pack( padx=9, side=RIGHT)
    b1_entry2.focus_force() #this line make visible all entries inmideately
    
    # b1_f2_5.pack( pady=6, expand=True)
    # b1_label2_5.pack( padx=9, side=LEFT)
    # b1_entry2_5.pack( padx=9, side=RIGHT)
    
    b1_f3.pack( pady=6, expand=True)
    b1_label3.pack( padx=9, side=LEFT)
    b1_entry3.pack( padx=9, side=RIGHT)
    
    
    b1_f4.pack( pady=6, expand=True)
    b1_label4.pack( padx=10, side=LEFT)
    b1_entry4.pack( padx=10, side=RIGHT)
    
    b1_f5.pack( pady=6, expand=True)
    b1_label5.pack(side=LEFT)
    b1_entry5.pack(side=RIGHT)
    b1_button.pack(pady=6)
    
    
    
    # b1_f2.pack( expand=True)
    # b1_label2R.pack(side=LEFT)
    # b1_p_listR.pack(side=RIGHT)
    # b1_f2.pack( expand=True)
    # # b1_f2.pack( expand=True)
    # b1_label2RR.pack(side=LEFT)
    # b1_entry2R.pack(side=RIGHT)

    
    
def button2_control(Group_var):
    hide_all_frames()
    button2_frame.pack()
    b2_f1.pack(pady=6)
    b2_label.pack( padx=9, side=LEFT)
    b2_entry.pack( padx=9, side=RIGHT)
    b2_f2.pack(pady=6)
    b2_label2.pack( padx=9, side=LEFT)
    b2_entry2.pack( padx=9, side=RIGHT)
    b2_button.pack(pady=6)
    
def button3_control(Group_var):
    hide_all_frames()
    button3_frame.pack()
    b3_button.pack()
    b3_button2.pack()
    # Group_var.Group_command_action(2)
    
    
def buttonF(Group_var):
    # print("SUPER")
    Group_var.Group_command_action(3)
    
def buttonF2(Group_var):
    # print("SUPER")
    Group_var.Group_command_action(1)
    
def buttonF3(Group_var):
    # print("SUPER")
    Group_var.Group_command_action(2)
    
def buttonFE(Group_var):
    Exel_production(Group_var)
    
def buttonF3_2(Group_var):
    # print("SUPER")
    Group_var.Group_command_action(4)
    
# def update_option_menu(gr):
    # b1_p_list.configure(button1_frame, b1_variable0, *pp_l)
    # menu = self.om["menu"]
    # menu.delete(0, "end")
    # for string in self.options:
    #     menu.add_command(label=string, command=lambda value=string: self.om_variable.set(value))


    
    

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




file_new_frame = Frame(root, width=600, height=500, )
edit_new_frame = Frame(root, width=600, height=500,)
input_frame = Frame(root, width=600, height=500, )



button_frame = Frame(root, width=600, height=500, )
button1_frame = Frame(root, width=600, height=500, )
b1_f1 = Frame(button1_frame, width=100, height=100, )
b1_f2 = Frame(button1_frame, width=100, height=100, )
# b1_f2_5 = Frame(button1_frame, width=100, height=100, )
b1_f3 = Frame(button1_frame, width=100, height=100, )
b1_f4 = Frame(button1_frame, width=100, height=100, )
b1_f5 = Frame(button1_frame, width=100, height=100, )

button2_frame = Frame(root, width=600, height=500, )
b2_f1 = Frame(button2_frame, width=100, height=100, )
b2_f2 = Frame(button2_frame, width=100, height=100, )

button3_frame = Frame(root, width=600, height=500, )
# b3_f1 = Frame(button3_frame, width=100, height=100, bg="red")


button_op1 = Button(button_frame, text= "Insert Stock", width= 20, command= lambda: button1_control(GroupX)).pack(side = LEFT, pady=20)
button_op2 = Button(button_frame, text= "New Person", width= 20, command= lambda: button2_control(GroupX)).pack(side = LEFT, pady=20)
button_op3 = Button(button_frame, text= "Record Value", width= 20, command= lambda: button3_control(GroupX)).pack(side = LEFT, pady=20)
# button_op3 = Button(button_frame, text= "Modify Existing Stock", width= 20).pack(side = LEFT, pady=20)
# button_op4 = Button(button_frame, text= "Print on Exel", width= 20).pack(side = LEFT, pady=20)

button_F = Button(button_frame, text= "Print on Terminal", width= 20, command= lambda: buttonF(GroupX)).pack(side = LEFT, pady=20)
button_F2 = Button(button_frame, text= "Save on txt", width= 20, command= lambda: buttonF2(GroupX)).pack(side = LEFT, pady=20)
button_F3 = Button(button_frame, text= "Save on Exel", width= 20, command= lambda: buttonFE(GroupX)).pack(side = LEFT, pady=20)


button_frame.pack()


#button 1 labels and variables to use
b1_label = Label(b1_f1, text="PERSON")
b1_variable0 = StringVar(root)
b1_variable0.set("") # default value
pp_l = [0]
b1_p_list = OptionMenu(b1_f1, b1_variable0, *pp_l)

# pp_l = GroupX.Group_ret_list_persons()
# print("SSS: ", pp_l)

# b1_label2R = Label(b1_f1, text="STOCK")
# b1_p_listR = OptionMenu(b1_f1, b1_variable0, 0,1,2,3)

# b1_label2RR = Label(b1_f2, text="STOCK")
# b1_entry2R = Entry(b1_f2, bd =5, width=50)





b1_space = Label(button1_frame, text="...", width=100, height=2)

b1_label2 = Label(b1_f2, text="STOCK")
b1_entry2 = Entry(b1_f2, bd =5, width=50)
# b1_label2_5 = Label(b1_f2_5, text="NAME")
# b1_entry2_5 = Entry(b1_f2_5, bd =5, width=50)
b1_label3 = Label(b1_f3, text="PRICE")
b1_entry3 = Entry(b1_f3, bd =5, width=50)
b1_label4 = Label(b1_f4, text="QUANTITY")
b1_entry4 = Entry(b1_f4, bd =5, width=50)
b1_label5 = Label(b1_f5, text="DATE")
b1_entry5 = DateEntry(b1_f5, selectmode="day", bd =5, width=50)
b1_button = Button(button1_frame, text= "enter", width= 25, height=3, command= lambda :print_value(GroupX))


#button 2 labels and variables to use
b2_label = Label(b2_f1, text="PERSON")
b2_entry = Entry(b2_f1, bd =5, width=50)
b2_label2 = Label(b2_f2, text="ACRONYMN")
b2_entry2 = Entry(b2_f2, bd =5, width=50)
b2_button = Button(button2_frame, text= "Enter New Person", width= 25, height=3, command= lambda :Add_person(GroupX, pp_l))

#button 3 labels and variables to use
b3_button = Button(button3_frame, text= "Record in History of Value", width= 20, command= lambda: buttonF3(GroupX))

b3_button2 = Button(button3_frame, text= "Erase Record in History of Value", width= 20, command= lambda: buttonF3_2(GroupX))


# messagebox.showerror("error", "try again")



root.mainloop()
