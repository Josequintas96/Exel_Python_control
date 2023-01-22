import os
from datetime import date


class Group:
    PP = None
    
    def __init__(self):
        self.PP = []
    
    def Group_get_num_persons(self):
        return len(self.PP)
    
    def Group_get_num_persons_stocks(self, person_num):
        return self.PP[person_num].Person_num_stock()
    
    def Group_get_persons_name(self, person_num):
        return self.PP[person_num].Person_get_name()
    
    def Group_get_persons_acronym(self, person_num):
        return self.PP[person_num].Person_get_acronym()
    
    def Group_get_persons_stock_name(self, person_num, stock_num):
        return self.PP[person_num].Person_stock_name(stock_num)
    
    def Group_get_persons_stock_price(self, person_num, stock_num):
        return self.PP[person_num].Person_stock_price(stock_num)
    
    def Group_get_persons_stock_quantity(self, person_num, stock_num):
        return self.PP[person_num].Person_stock_quantity(stock_num)
    
    def Group_get_persons_stock_date(self, person_num, stock_num):
        return self.PP[person_num].Person_stock_date(stock_num)
    
    def Group_ret_list_persons(self):
        pp_l =[]
        for x in self.PP:
            pp_l.append(x.Person_get_name())
        return pp_l
    
    
    def Group_Create_New_Person(self):
        pp1 = Person()
        # if len(pp1.stocks) >0:
        #     pp1.clean()
        #     print("CLEAN HAPPEN")
        #     pp1 = Person()
        pp1.Person_insert_name()
        pp1.Person_insert_stock()
        pp1.Person_insert_stock()
        self.PP.append(pp1)
        print("Length of pp1: ", len(pp1.stocks))
        print("Length of PP: ", len(self.PP))
        
    def Group_insert_person(self, pp1):
        self.PP.append(pp1)
        
    def Group_create_person(self, name):
        pp2 = Person()
        pp2.Person_set_name(name)
        self.PP.append(pp2)
        return len(self.PP)
    
    def Group_add_person_acronym(self, acro, person_num):
        self.PP[person_num].Person_set_acronym(acro)
        
    def Group_insert_Stock(self, person_name, name, cost, quantity, date):
        i=0
        while i < len(self.PP):
            if person_name == self.PP[i].Person_get_name():
                try:
                    float(cost)
                except ValueError:
                    return False

                
                if quantity.isdigit() == False:
                    return False

                print("PERSON FOUND")
                self.Group_add_stock_person(name, cost, quantity, date, i)
                return True
            i+=1
        print("NOT FOUND")
        return False
    
    def Group_add_stock_person(self, name, cost, quantity, date, run_person):
        self.PP[run_person].Person_add_stock(name, cost, quantity, date)
        
    def Group_add_history_person(self, name, date, price, run_person):
        self.PP[run_person].Person_add_to_track(name, date, price)
    
    def Group_print_group(self):
        for x in self.PP:
            x.Person_print_stock()
        # print("\n")
            
    def Group_set_up_history(self):
        print("\t\tSet up history for all persons")
        for pers in self.PP:
            pers.Person_add_history_onStock()
            
    def Group_take_action(self):
        #using input to do actions
        choice = 0
        
        while int(choice) != 9:
            print("1. Save value on txt")
            print("2. Add history on Group")
            print("3. Print all info")
            print("9. RUN END")
            choice = input("What to do?  ")
        
            if int(choice) == 1:
                print("\tSAVE FILE was chosen")
                f = open(os.path.join('Exel_Python_control', "stocks3.txt"), "w")
                for x in self.PP:
                    f.write("Person: " + x.name+"\n")
                    f.write("Acronym: " + x.acronym+"\n")
                    for stockX in x.stocks:
                        strX = stockX.Stock_get_name() + " " + str(stockX.Stock_get_quantity()) + " " + str(stockX.Stock_get_price()) + " " + stockX.Stock_get_date() +"\n"
                        f.write(strX)   
                    for histX in x.history_track:
                        if len(histX.history)>0:
                            x0=0
                            while x0 < len(histX.history):
                                strX = "!ST: " + histX.HS_get_value_hist(x0)
                                print(strX)
                                f.write(strX) 
                                x0+=1
                        
            elif int(choice) ==2:
                print("\tHISTORY was chosen")
                self.Group_set_up_history()
                
            elif int(choice) ==3:
                print("\tPrint info")
                self.Group_print_group()
                
    def Group_command_action(self, choice):
        #using input to do actions
        
        # while choice != 9:
        #     print("1. Save value on txt")
        #     print("2. Add history on Group")
        #     print("3. Print all info")
        #     print("9. RUN END")
        #     choice = input("What to do?  ")
        
        if choice == 1:
            print("\tSAVE FILE was chosen")
            f = open(os.path.join('Exel_Python_control', "stocks3.txt"), "w")
            for x in self.PP:
                f.write("Person: " + x.name+"\n")
                f.write("Acronym: " + x.acronym+"\n")
                for stockX in x.stocks:
                    strX = stockX.Stock_get_name() + " " + str(stockX.Stock_get_quantity()) + " " + str(stockX.Stock_get_price()) + " " + stockX.Stock_get_date() +"\n"
                    f.write(strX)   
                for histX in x.history_track:
                    if len(histX.history)>0:
                        x0=0
                        while x0 < len(histX.history):
                            strX = "!ST: " + histX.HS_get_value_hist(x0)
                            print(strX)
                            f.write(strX) 
                            x0+=1
                        
        elif choice ==2:
            print("\tHISTORY was chosen")
            self.Group_set_up_history()
                
        elif choice ==3:
            print("\tPrint info")
            self.Group_print_group()

class Person:
    name=""
    acronym=""
    history_track = None
    
    def __init__(self, name):
        self.name = name
        self.stocks=[]
        self.history_track = []
        
    def __init__(self):
        self.stocks=[]
        self.history_track = []
    
    def Person_set_name(self, name):
        self.name = name
        
    def Person_insert_name_acronym(self, name, acronym):
        #give attribute to person
        self.name = name
        self.acronym = acronym
        
    def Person_insert_name(self):
        #give attribute to person with input user
        name = input("Insert name of person: ")
        self.name = name
        acronym = input("Insert acronym of person: ")
        self.acronym = acronym
        self.stocks=[]
        
    def Person_get_name(self):
        return self.name
    
    def Person_get_acronym(self):
        return self.acronym
    
    def Person_num_stock(self):
        return len(self.stocks)
    
    def Person_stock_name(self, stock_num):
        return self.stocks[stock_num].Stock_get_name()
    
    def Person_stock_price(self, stock_num):
        return self.stocks[stock_num].Stock_get_price()
    
    def Person_stock_quantity(self, stock_num):
        return self.stocks[stock_num].Stock_get_quantity()
    
    def Person_stock_date(self, stock_num):
        return self.stocks[stock_num].Stock_get_date()
        
    def Person_set_acronym(self, acro):
        self.acronym = acro
        
    def Person_add_history_onStock(self):
        #save on each history track
        for x in self.history_track:
            x.HS_add_history(10)
        
    def Person_insert_stock(self):
        #create Sotck directly on method inside
        x = Stocks()
        x.Stock_insert_stock()
        self.stocks.append(x)
        
    def Person_add_stock_to_history(self, stock):
        for x in self.history_track:
            if stock == x.name:
                print("Exist")
        return None
    
    def Person_add_stock(self, name, cost, quantity, date):
        #give person a stock by parameters
        stockX = Stocks(name, cost, quantity, date)
        self.stocks.append(stockX)
        if self.Person_is_on_track(name):
            print("\t\t new stock")
        else:
            print("\t\tRepeated stock")
    
    def Person_is_on_track(self, name):
        if len(self.history_track) == 0:
            sh1 = history_Stocks(name)
            self.history_track.append(sh1)
            return True
        else:
            for X in self.history_track:
                if X.name == name:
                    return False
            sh1 = history_Stocks(name)
            self.history_track.append(sh1)
            return True
        
    def Person_add_to_track(self, name, date, price):
        if self.Person_is_on_track(name):
            #IF DO NOT EXIST, THEN IT IS CREATED AND NOW ADD VALUE
            self.Person_find_and_add_on_track(name, date, price)
        else:
            self.Person_find_and_add_on_track(name, date, price)
            
    def Person_find_and_add_on_track(self, name, date, price):
        print("Find and add on track list")
        for x in self.history_track:
            if name == x.name:
                x.HS_add_history(price)
    
    
    def Person_print_stock(self):
        print(self.name , "(" , self.acronym, ")")
        for x in self.stocks:
            x.Stock_print_stock_value()
            print("\n")
        if len(self.history_track) >0:
            print("\tThese are the history")
            for x in self.history_track:
                lenx = x.HS_get_len()
                x0 =0
                while x0 < lenx:
                    strX = x.HS_get_value_hist(x0)
                    print("\t", strX)
                    x0+=1
            
            
    def Person_take_action(self):
        choice = input("What to do?  ")
        print("1. save value on txt")
        if int(choice) == 1:
            f = open(os.path.join('Exel_Python_control', "stocks3.txt"), "w")
            f.write("Person: " + self.name+"\n")
            f.write("Acronym: " + self.acronym+"\n")
            for stockX in self.stocks:
                strX = stockX.Stock_get_name() + " " + str(stockX.Stock_get_quantity()) + " " + str(stockX.Stock_get_price()) + " " + stockX.Stock_get_date() +"\n"
                f.write(strX)

class Stocks:
    name =""
    date = ""
    quantity = 0
    cost = 0
    
    def __init__(self, name,  cost, quantity, date):
        self.name = name
        self.date = date
        self.quantity = quantity
        self.cost = cost
    
    # def __init__(self):
    #     self.name = ""
    
        
    def Stock_get_name(self):
        return self.name
    
    def Stock_get_quantity(self):
        return self.quantity
    
    def Stock_get_price(self):
        return self.cost
    
    def Stock_get_date(self):
        return self.date
        
    def Stock_print_stock_value(self):
        print("\tThese are the Stocks")
        print("\tName: ", self.name )
        print("\tQuantity: ", self.quantity)
        print("\tDate bought: ", self.date)
        
    def Stock_insert_stock(self):
        self.name = input("Insert a stock: " )
        self.quantity = input("How many: " )
        self.price = input("Cost of each: " )
        self.date = input("Date brought: " )
        
class history_Stocks:
    name =""
    history = None
    
    def __init__(self, name):
        self.name = name
        self.history = []
    
    def HS_get_len(self):
        return len(self.history)
        
    def HS_add_history(self, value):
        dateX = date.today()
        hist0 = (str(dateX), value)
        self.history.append(hist0)
        
    def HS_get_value_hist(self, run_t):
        if len(self.history) == 0:
            strX = self.name + " No Stock History\n"
            return strX
        if run_t >= len(self.history):
            strX="p"
            return strX
        strX = self.name + " " + str(self.history[run_t][0]) + " " + str(self.history[run_t][1]) + "\n"
        return strX
    

# nameX = input("Insert a stock: " )
# quantityX = input("How many: " )
# priceX = input("Cost of each: " )
# dateX = input("Date brought: " )
# stockX = Stocks()
# stockX.Stock_insert_stock()
# stockX.print_stock_value()
# # stockX =  Stocks(nameX, quantityX, dateX, priceX)

# choice = input("What to do?")
# print("1. save value on txt")
# if int(choice) == 1:
#     f = open("\stocks2.txt", "w")
#     strX = stockX.Stock_get_name() + " " + str(stockX.Stock_get_quantity()) + " " + str(stockX.Stock_get_price()) + " " + stockX.Stock_get_date() +"\n"
#     f.write(strX)
    
# pp = Person()
# pp.Person_insert_name()
# pp.Stock_insert_stock()
# pp.Person_print_stock()


# gg = Group()
# pp1 = Person()
# pp1.Person_insert_name_acronym("Pablo", "PB")
# pp1.Person_add_stock("PSY", 10, 12, "12/09/2022")
# pp1.Person_add_stock("DISN", 1, 120, "12/01/2022")
# gg.Group_insert_person(pp1)

# pp2 = Person()
# pp2.Person_insert_name_acronym("Yetta", "YT")
# pp2.Person_add_stock("POT", 8, 40, "10/09/2020")
# pp2.Person_add_stock("SEN", 2, 35, "08/01/2019")
# gg.Group_insert_person(pp2)
# # gg.Group_Create_New_Person()
# # gg.Group_insert_person(pp)
# # gg.Group_Create_New_Person()
# gg.Group_print_group()
# gg.Group_take_action()

    
    
    



    


