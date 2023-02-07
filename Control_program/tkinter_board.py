from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
from read_file import control_Group
from Group import Group
from Excel_code import *


root = Tk()
root.title('YAHOO FINANCE CONTROLLER')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("1000x600")


# photo = PhotoImage(file = 'icon_pinball.png')
# root.wm_iconphoto(False, photo)

# root.iconbitmap("Exel_Python_control/icon_pinball.png")
root.iconphoto(False, PhotoImage(file='Exel_Python_control/icon_pinball.png'))



my_menu = Menu(root)
root.config(menu = my_menu)

GroupX = Group()
control_Group(GroupX)

Title = Label(root, text="Bienvenido a tu Cuenta de Finanza", font=("Courier 22 bold")).pack( side = TOP)

def Save_value(Group_var):
    ent1 = b1_variable0.get() #person variable
    print(ent1)
    ent2 = b1_entry2.get() #stock variable
    print(ent2.upper())
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
    ent5X = ent5.split("/")
    ent5 = "20"+ent5X[2]+"-"+ent5X[1]+"-"+ent5X[0]
    print(ent5)
    b1_entry5.delete(0,END)
    if Group_var.Group_stock_verification(ent2.upper()):
        result1 = Group_var.Group_insert_Stock(ent1, ent2.upper(), ent3, ent4, ent5)
        if result1:
            messagebox.showinfo("SUCCEED", "Accion Guardada")
        else:
            messagebox.showerror("error", "Uno de los Valores es incorrecto")
    else:
        messagebox.showerror("error", "Accion probablemente no exista")
        
def Add_person(Group_var, List):
    ent1 =  b2_entry.get() #name variable
    print(ent1)
    b2_entry.delete(0,END)
    ent2 = b2_entry2.get()  #acronym variable
    print(ent2)
    b2_entry2.delete(0,END) 
    
    result_h = Group_var.Group_person_exist(ent1, ent2.upper()) #evita repeticion de nombres y acronimos
    
    if result_h:
        result2 = Group_var.Group_create_person(ent1)
        Group_var.Group_add_person_acronym(ent2.upper(), result2-1)
        # Group_var.Group_command_action(3) #print stocks to prove that person was added
        List.append(ent1)
        messagebox.showinfo("SUCCEED", "Persona ha sido Agregada")
    else:
        messagebox.showerror("error", "Persona o Acronimo ya existe")

    
def delete_person(Group_var):
    ent4 = b4_entry3.get()
    Group_var.Group_delete_stock(b4_variable0.get(), b4_variable2.get(), ent4)
    b4_entry3.delete(0,END) 
    pp_D = []
    pp_D2 = []
    hide_all_frames()
    button4_frame_Extra.pack()
        

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
    button4_frame.pack_forget()
    button4_frame_Extra.forget()
    button5_frame.pack_forget()
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
    b1_f0.pack( pady=6, expand=True)
    b1_label0.pack()
    b1_f1.pack( pady=6, expand=True)
    b1_p_list['menu'].delete(0, 'end')
    pp_l = Group_var.Group_ret_list_persons()
    # var = StringVar()
    for x0 in pp_l:
        b1_p_list['menu'].add_command(label=x0, command= lambda x= x0: b1_variable0.set(x))
    b1_label.pack( padx=9, side=LEFT)
    b1_p_list.pack( padx=9, side=RIGHT)
    
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
    

    
    
def button2_control(Group_var):
    hide_all_frames()
    button2_frame.pack()
    b2_f0.pack()
    b2_label0.pack()
    b2_f1.pack(pady=6)
    b2_label.pack( padx=9, side=LEFT)
    b2_entry.pack( padx=9, side=RIGHT)
    b2_entry.focus_force()
    b2_f2.pack(pady=6)
    b2_label2.pack( padx=9, side=LEFT)
    b2_entry2.pack( padx=9, side=RIGHT)
    b2_entry2.focus_force()
    b2_button.pack(pady=6)
    
def button3_control(Group_var):
    hide_all_frames()
    button3_frame.pack()
    b3_f0.pack()
    b3_label0.pack(pady=9)
    b3_button.pack()
    b3_button2.pack()
    # Group_var.Group_command_action(2)
    
def button4_control(Group_var):
    hide_all_frames()
    button4_frame.pack()
    b4_f0.pack( pady=6, expand=True)
    b4_label0.pack()
    b4_f1.pack( pady=6, expand=True)
    b4_p_list['menu'].delete(0, 'end')
    pp_D = Group_var.Group_ret_list_persons()
    # var = StringVar()
    for x0 in pp_D:
        b4_p_list['menu'].add_command(label=x0, command= lambda x= x0: b4_variable0.set(x))
    b4_label.pack( padx=9, side=LEFT)
    b4_p_list.pack( padx=9, side=RIGHT)
    
    button_op4_2.pack()

def button4_control2(Group_var):
    b4_f2.pack( pady=6, expand=True)
    b4_p_list2['menu'].delete(0, 'end')
    print("KK2: ", b4_variable0.get())
    run_person = Group_var.Group_get_peron_run_person(b4_variable0.get())
    # print("KK: ", run_person)
    pp_D2 = Group_var.Group_get_person_history_stocks(run_person)
    print(pp_D2)
    # print("KK3: ", run_person)
    # var = StringVar()
    if pp_D2 != None:
        for x0 in pp_D2:
            b4_p_list2['menu'].add_command(label=x0, command= lambda x= x0: b4_variable2.set(x))
    b4_label2.pack( padx=9, side=LEFT)
    b4_p_list2.pack( padx=9, side=RIGHT)
    
    b4_f3.pack( pady=6, expand=True)
    b4_label3.pack(padx=9, side=LEFT)
    b4_entry3.pack(padx=9, side=RIGHT)
    
    b4_button.pack()
    
    

def button5_control(Group_var):
    hide_all_frames()
    button5_frame.pack()
    b5_label.pack( )
    # b5_label2.pack( )
    b5_label3.pack( )
    # b5_label4.pack( )
    b5_label5.pack( )
    b5_label6.pack()
    b5_f1.pack( pady=2, expand=True)
    # b5g_f2.pack( pady=2, expand=True)
    # b5_f2.pack( pady=2, expand=True)
    # button5_frame2.pack()
    b5g_f3.pack( pady=2, expand=True)
    b5_f3.pack( pady=2, expand=True)
    button5_frame3.pack()
    # b5g_f4.pack( pady=6, expand=True)
    # b5_f4.pack( pady=6, expand=True)
    # button5_frame4.pack()
    b5g_f5.pack( pady=6, expand=True)
    b5_f5.pack( pady=6, expand=True)
    button5_frame5.pack()
    b5g_f6.pack( pady=6, expand=True)
    b5_f6.pack( pady=6, expand=True)
    button5_frame6.pack()
    
    
def buttonF(Group_var):
    # print("SUPER")
    Group_var.Group_command_action(3)
    
def buttonF2(Group_var):
    # print("SUPER")
    Group_var.Group_command_action(1)
    messagebox.showinfo("SUCCEED", "Documento txt se ha creado")
    
def buttonF3(Group_var):
    # print("SUPER")
    Group_var.Group_command_action(2)
    messagebox.showinfo("SUCCEED", "Acciones se han actualizado")
    
def buttonFE(Group_var):
    # BB = False
    Exel_production(Group_var)
    # try:
    #     Exel_production(Group_var)
    # except ValueError:
    #     messagebox.showerror("error", "Error ha ocurrdo, intenta otra o llama ha tu hijo")
    #     return False
    # else:
    messagebox.showinfo("SUCCEED", "Documento Excel se ha creado")
    
def buttonFE2(Group_var):
    Group_var.Group_command_action(1)
    messagebox.showinfo("SUCCEED", "Documento txt se ha creado")
    Exel_production(Group_var)
    messagebox.showinfo("SUCCEED", "Documento Excel se ha creado")
    
def buttonF3_2(Group_var):
    # print("SUPER")
    Group_var.Group_command_action(4)
    messagebox.showinfo("SUCCEED", "Historial previo ha sido borrado")
    
def buttonFE3(Group_var):
    Group_var.Group_Sort_Person()        
    messagebox.showinfo("SUCCEED", "Acciones se han organizado")
    
    
    

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
b1_f0 = Frame(button1_frame, width=100, height=100, )
b1_f1 = Frame(button1_frame, width=100, height=100, )
b1_f2 = Frame(button1_frame, width=100, height=100, )
# b1_f2_5 = Frame(button1_frame, width=100, height=100, )
b1_f3 = Frame(button1_frame, width=100, height=100, )
b1_f4 = Frame(button1_frame, width=100, height=100, )
b1_f5 = Frame(button1_frame, width=100, height=100, )

button2_frame = Frame(root, width=600, height=500, )
b2_f0 = Frame(button2_frame, width=100, height=100, )
b2_f1 = Frame(button2_frame, width=100, height=100, )
b2_f2 = Frame(button2_frame, width=100, height=100, )

button3_frame = Frame(root, width=600, height=500, )
b3_f0 = Frame(button3_frame, width=100, height=100, )

button4_frame = Frame(root, width=600, height=500, )
b4_f0 = Frame(button4_frame, width=100, height=100, )
b4_f1 = Frame(button4_frame, width=100, height=100, )
button_op4_2 = Button(button4_frame, text= "Seleccionar persona", width= 18, command= lambda: button4_control2(GroupX))
# button will activate the next frame
b4_f2 = Frame(button4_frame, width=100, height=100, )
# b4_f2 = Frame(button4_frame, width=100, height=100, )
b4_f3 = Frame(button4_frame, width=100, height=100, )

button4_frame_Extra = Frame(root, width=600, height=500, )


button5_frame = Frame(root, width=600, height=500, )
b5_f1 = Frame(button5_frame, width=100, height=100, )
# general frame for instruction and button
b5g_f2 = Frame(button5_frame, width=100, height=100, highlightbackground="black", highlightthickness=2, pady=9, padx = 12)
b5_f2 = Frame(b5g_f2, width=100, height=100, )
button5_frame2 = Frame(b5g_f2, width=100, height=100, )
# general frame for instruction and button
b5g_f3 = Frame(button5_frame, width=100, height=100, highlightbackground="black", highlightthickness=2, pady=9, padx = 12)
b5_f3 = Frame(b5g_f3, width=100, height=100, )
button5_frame3 = Frame(b5g_f3, width=100, height=100, )
# general frame for instruction and button
b5g_f4 = Frame(button5_frame, width=100, height=100, highlightbackground="black", highlightthickness=2, pady=9, padx=12)
b5_f4 = Frame(b5g_f4, width=100, height=100, )
button5_frame4 = Frame(b5g_f4, width=600, height=500, )
b5g_f5 = Frame(button5_frame, width=100, height=100, highlightbackground="black", highlightthickness=2, pady=9, padx=12)
b5_f5 = Frame(b5g_f5, width=100, height=100, )
button5_frame5 = Frame(b5g_f5, width=600, height=500, )
b5g_f6 = Frame(button5_frame, width=100, height=100, highlightbackground="black", highlightthickness=2, pady=9, padx=12)
b5_f6 = Frame(b5g_f6, width=100, height=100, )
button5_frame6 = Frame(b5g_f6, width=600, height=500, )


button_op1 = Button(button_frame, text= "Guardar Accion", width= 18, command= lambda: button1_control(GroupX)).pack(side = LEFT, pady=20)
button_op2 = Button(button_frame, text= "New Person", width= 18, command= lambda: button2_control(GroupX)).pack(side = LEFT, pady=20)
button_op3 = Button(button_frame, text= "Guardar valor de hoy", width= 18, command= lambda: button3_control(GroupX)).pack(side = LEFT, pady=20)
button_op4 = Button(button_frame, text= "Vender Action", width= 18, command= lambda: button4_control(GroupX)).pack(side = LEFT, pady=20)
button_op5 = Button(button_frame, text= "Base de Control", width= 18, command= lambda: button5_control(GroupX)).pack(side = LEFT, pady=20)





button_frame.pack()


#button 1 labels and variables to use
b1_label0 = Label(b1_f0, text="Agrega una Accion\n", font=("Courier 22 bold"))
b1_label = Label(b1_f1, text="PERSON")
b1_variable0 = StringVar(root)
b1_variable0.set("") # default value
pp_l = [0]
b1_p_list = OptionMenu(b1_f1, b1_variable0, *pp_l)
b1_label2 = Label(b1_f2, text="Accion")
b1_entry2 = Entry(b1_f2, bd =5, width=50)
# b1_label2_5 = Label(b1_f2_5, text="NAME")
# b1_entry2_5 = Entry(b1_f2_5, bd =5, width=50)
b1_label3 = Label(b1_f3, text="Precio")
b1_entry3 = Entry(b1_f3, bd =5, width=50)
b1_label4 = Label(b1_f4, text="Cantidad")
b1_entry4 = Entry(b1_f4, bd =5, width=50)
b1_label5 = Label(b1_f5, text="Fecha")
b1_entry5 = DateEntry(b1_f5, selectmode="day", bd =5, width=50)
b1_button = Button(button1_frame, text= "Insertar", width= 25, height=3, command= lambda :Save_value(GroupX))


#button 2 labels and variables to use
b2_label0 = Label(b2_f0, text="Agrega una Perona", font=("Courier 22 bold"))
b2_label = Label(b2_f1, text="Nombre")
b2_entry = Entry(b2_f1, bd =5, width=50)
b2_label2 = Label(b2_f2, text="Acronimo")
b2_entry2 = Entry(b2_f2, bd =5, width=50)
b2_button = Button(button2_frame, text= "Entra una nueva Persona", width= 25, height=3, command= lambda :Add_person(GroupX, pp_l))

#button 3 labels and variables to use
b3_label0 = Label(b3_f0, text="Modifica tu cuenta", font=("Courier 22 bold"))
b3_button = Button(button3_frame, text= "Guarda el valor de tus acciones", width= 20, command= lambda: buttonF3(GroupX))

b3_button2 = Button(button3_frame, text= "Borra fecha de tus acciones", width= 20, command= lambda: buttonF3_2(GroupX))

# button 4 labels and variable to use
b4_button = Button(button4_frame, text= "Borra a una Accion", width= 25, height=3, command= lambda :delete_person(GroupX))
b4_label0 = Label(b4_f0, text="Vende una Accion", font=("Courier 22 bold"))
b4_label = Label(b4_f1, text="PERSON: ")
b4_variable0 = StringVar(root)
b4_variable0.set("") # default value
pp_D = [0]
b4_p_list = OptionMenu(b4_f1, b4_variable0, *pp_D)
b4_label2 = Label(b4_f2, text="ACCION: ")
b4_variable2 = StringVar(root)
b4_variable2.set("") # default value
pp_D2 = [0]
b4_p_list2 = OptionMenu(b4_f2, b4_variable2, *pp_D2)
b4_label3 = Label(b4_f3, text="Cantidad:")
b4_entry3 = Entry(b4_f3, bd =5, width=50)

b4_label =  Label(button4_frame_Extra, text="Acciones ha sido vendida")



#button 5 labels and variables to use
b5_label = Label(b5_f1, text="Estos botones son de control y aplicar accion\n", font=("Courier 22 bold"))
# b5_label2 = Label(b5_f2, text="1. Print on Terminal: imprime lista de Acciones en fisico")
b5_label3 = Label(b5_f3, text="2. Guardar en txt: una vez agregada una accion, este boton te la guarda en la memoria")
b5_label4 = Label(b5_f4, text="3. Guardar en Exel: este boton te crea tu documento excel")
b5_label5 = Label(b5_f5, text="4. Guardar en Txt y Exel")
b5_label6 = Label(b5_f6, text="5. Organizar valores")
button_F = Button(button5_frame2, text= "Desvela en Terminal", width= 20, command= lambda: buttonF(GroupX)).pack(side = LEFT, pady=20)
button_F2 = Button(button5_frame3, text= "Guardar en txt", width= 20, command= lambda: buttonF2(GroupX)).pack(side = LEFT, pady=20)
button_F3 = Button(button5_frame4, text= "Guardar on Exel", width= 20, command= lambda: buttonFE(GroupX)).pack(side = LEFT, pady=20)
button_F4 = Button(button5_frame5, text= "Modificar documentos", width= 20, command= lambda: buttonFE2(GroupX)).pack(side = LEFT, pady=20)
button_F5 = Button(button5_frame6, text= "Orginazar alfabeticamente", width= 20, command= lambda: buttonFE3(GroupX)).pack(side = LEFT, pady=20)



root.mainloop()


