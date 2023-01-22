from tkinter import *
from tkinter import ttk
from python_stage8 import control_Group
from python_stage5 import Group

window = Tk()

GroupX = Group()
control_Group(GroupX)
pp_l = GroupX.Group_ret_list_persons()

class Option_control:
    option_1 = False
    option_2 = False
    option_3 = False
    
    def __init__(self):
        self.option_1 = False
        self.option_2 = False
        self.option_3 = False

def action_option1(op_con):
    if op_con.option_1 == False:
        op_con.option_1 = True
        op_con.option_2 = False
        op_con.option_3 = False
    else:
        op_con.option_1 = False
def action_option2(op_con):
    if op_con.option_2 == False:
        op_con.option_1 = False
        op_con.option_2 = True
        op_con.option_3 = False
    else:
        op_con.option_2 = False
def action_option3(op_con):
    if op_con.option_3 == False:
        op_con.option_1 = False
        op_con.option_2 = False
        op_con.option_3 = True
    else:
        op_con.option_3 = False

def display_text():
    global entry
    string= E1.get()
    if string != "":    
        print("H1:", string)
        E1.delete(0, END)
    
    string= E2.get()   
    if string != "":    
        print("H2:", string)
        E2.delete(0, END)
    
    string= E3.get()    
    if string != "":    
        print("H3:", string)
        E3.delete(0, END)
    
    string= E4.get()    
    if string != "":    
        print("H4:", string)
        E4.delete(0, END)
        
    print("H5: ", variable0.get())
    # L1.configure(text=string)
    
# Create Option varioable
Opp_C = Option_control()
    

port = Frame(master = window, width=100, height=100, bg="red")
port2 = Frame(master = window, width=100, height=100, bg="blue")
port2_0 = Frame(master = window, width=100, height=100, bg="blue")
port2_1 = Frame(master = window, width=100, height=100, bg="blue")
port2_2 = Frame(master = window, width=100, height=100, bg="blue")
port2_3 = Frame(master = window, width=100, height=100, bg="blue")
port3 = Frame(master = window, width=100, height=100, bg="GREEN")

port4 = Frame(master = window, width=100, height=100, bg="PINK")


greeting = Label(master=port, text="Hello, FATHER")
greetingM = Label(master=port2, text="Hello, MOTHER")
name = Entry(fg="yellow", bg="blue", width=50)
button = Button( text="Click me!", width=25, height=5, bg="blue",fg="black",)




L1 = Label(port, text="WELCOME to FINANCE", font=("Courier 22 bold"))
L1.pack( side = TOP)


variable0 = StringVar(window)
variable0.set("") # default value
L0 = Label(port2_0, text="PERSON")
L0.pack(side = LEFT)
E0 = OptionMenu(port2_0, variable0, *pp_l)
E0.pack(side = RIGHT)


L2 = Label(port2, text="STOCK")
L2.pack(side = LEFT)
E1 = Entry(port2, bd =5, width=100)
E1.pack(side = RIGHT)

L5 = Label(port2_1, text="PRICE")
L5.pack(side = LEFT)
E4 = Entry(port2_1, bd =5, width=100)
E4.pack(side = RIGHT)

L3 = Label(port2_2, text="QUANTITY")
L3.pack(side = LEFT)
E2 = Entry(port2_2, bd =5, width=100)
E2.pack(side = RIGHT)

L4 = Label(port2_3, text="DATE")
L4.pack(side = LEFT)
E3 = Entry(port2_3, bd =5, width=100)
E3.pack(side = RIGHT)



Button(port3, text= "Okay", width= 20, command= display_text).pack(pady=20)



button_op1 = Button(port4, text= "New Person", width= 20, command= action_option1(Opp_C)).pack(side = LEFT, pady=20)

button_op2 = Button(port4, text= "Insert Stock", width= 20, command= action_option2(Opp_C)).pack(side = LEFT, pady=20)

button_op3 = Button(port4, text= "Save File", width= 20, command= action_option3(Opp_C)).pack(side = LEFT, pady=20)


port.pack()
port2.pack()

port2_0.pack()
port2_1.pack()
port2_2.pack()
port2_3.pack()
port3.pack()
port4.pack()
# nameT = name.get()
# print("H", nameT)


# greeting.pack()
# greetingM.pack()
# button.pack()
# name.pack()
# port2.pack(fill=X)
# port.pack()







#PART 1
# canvas1 = Canvas(window, width=400, height=300)
# canvas1.pack()

# label1 = ttk.Label(window, text='Calculate the Square Root')
# label1.config(font=('helvetica', 14))
# canvas1.create_window(200, 25, window=label1)

# label2 = ttk.Label(window, text='Type your Number:')
# label2.config(font=('helvetica', 10))
# canvas1.create_window(200, 100, window=label2)

# entry1 = ttk.Entry(window) 
# canvas1.create_window(200, 140, window=entry1)

# def get_square_root():  
#     x1 = entry1.get()
    
#     label3 = ttk.Label(window, text=float(x1)**0.5)
#     canvas1.create_window(200, 230, window=label3)
    
#     label4 = ttk.Label(window, text=float(x1)**0.5, font=('helvetica', 10, 'bold'))
#     canvas1.create_window(200, 230, window=label4)
    
# button1 = ttk.Button(text='Get the Square Root', command=get_square_root, style="BW.TLabel")
# canvas1.create_window(200, 180, window=button1)


#PART 2
# notebook = ttk.Notebook(window)

# tab1 = Frame(notebook)
# tab2 = Frame(notebook)

# variable = StringVar(window)
# variable.set("one") # default value

# tab1 = OptionMenu(window, variable, "one", "two", "three")

# variableX = StringVar(window)
# variableX.set("one") # default value

# tab2 = OptionMenu(window, variableX, "one", "two", "three", "four", "five")

# notebook.add(tab1, text="Tab 1")
# notebook.add(tab2, text="Tab 2")
# notebook.pack()

window.mainloop()

