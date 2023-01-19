from tkinter import *
from tkinter import ttk

window = Tk()


port = Frame(master = window, width=100, height=100, bg="red")
port2 = Frame(master = window, width=100, height=100, bg="blue")
greeting = Label(master=port, text="Hello, FATHER")
greetingM = Label(master=port2, text="Hello, MOTHER")
name = Entry(fg="yellow", bg="blue", width=50)
button = Button( text="Click me!", width=25, height=5, bg="blue",fg="black",)



L1 = Label(window, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(window, bd =5)
E1.pack(side = RIGHT)

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

