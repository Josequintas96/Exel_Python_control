import os
from datetime import date


class Group:
    PP = None
    
    def __init__(self):
        self.PP = []
    
    def get_num_persons(self):
        return len(self.PP)
    
    def get_num_persons_stocks(self, person_num):
        return self.PP[person_num].num_stock()
    
    def get_persons_name(self, person_num):
        return self.PP[person_num].get_name()
    
    def get_persons_acronym(self, person_num):
        return self.PP[person_num].get_acronym()
    
    def get_persons_stock_name(self, person_num, stock_num):
        return self.PP[person_num].stock_name(stock_num)
    
    def get_persons_stock_price(self, person_num, stock_num):
        return self.PP[person_num].stock_price(stock_num)
    
    def get_persons_stock_quantity(self, person_num, stock_num):
        return self.PP[person_num].stock_quantity(stock_num)
    
    def get_persons_stock_date(self, person_num, stock_num):
        return self.PP[person_num].stock_date(stock_num)
    
    
    
    def insert_person_New(self):
        pp1 = Person()
        # if len(pp1.stocks) >0:
        #     pp1.clean()
        #     print("CLEAN HAPPEN")
        #     pp1 = Person()
        pp1.name_insert()
        pp1.insert_stock()
        pp1.insert_stock()
        self.PP.append(pp1)
        print("Length of pp1: ", len(pp1.stocks))
        print("Length of PP: ", len(self.PP))
        
    def insert_person(self, pp1):
        self.PP.append(pp1)
        
    def create_person(self, name):
        pp2 = Person()
        pp2.set_name(name)
        self.PP.append(pp2)
    
    def add_person_acronym(self, acro, person_num):
        self.PP[person_num].set_acronym(acro) 
    
    def add_stock_person(self, name, cost, quantity, date, run_person):
        self.PP[run_person].add_stock(name, cost, quantity, date)
        
    def add_history_person(self, name, date, price, run_person):
        self.PP[run_person].add_track(name, date, price)
    
    def print_group(self):
        for x in self.PP:
            x.print_stock()
        # print("\n")
            
    def set_up_history(self):
        print("\t\tSet up history for all persons")
        for pers in self.PP:
            pers.add_history_onStock()
            
    def take_action(self):
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
                        strX = stockX.get_name() + " " + str(stockX.get_quantity()) + " " + str(stockX.get_price()) + " " + stockX.get_date() +"\n"
                        f.write(strX)   
                    for histX in x.history_track:
                        if len(histX.history)>0:
                            x0=0
                            while x0 < len(histX.history):
                                strX = "!ST: " + histX.get_value_hist(x0)
                                print(strX)
                                f.write(strX) 
                                x0+=1
                        
            elif int(choice) ==2:
                print("\tHISTORY was chosen")
                self.set_up_history()
                
            elif int(choice) ==3:
                print("\tPrint info")
                self.print_group()

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
    
    def set_name(self, name):
        self.name = name
        
    def name_insert_PP(self, name, acronym):
        #give attribute to person
        self.name = name
        self.acronym = acronym
        
    def name_insert(self):
        #give attribute to person with input user
        name = input("Insert name of person: ")
        self.name = name
        acronym = input("Insert acronym of person: ")
        self.acronym = acronym
        self.stocks=[]
        
    def get_name(self):
        return self.name
    
    def get_acronym(self):
        return self.acronym
    
    def num_stock(self):
        return len(self.stocks)
    
    def stock_name(self, stock_num):
        return self.stocks[stock_num].get_name()
    
    def stock_price(self, stock_num):
        return self.stocks[stock_num].get_price()
    
    def stock_quantity(self, stock_num):
        return self.stocks[stock_num].get_quantity()
    
    def stock_date(self, stock_num):
        return self.stocks[stock_num].get_date()
        
    def set_acronym(self, acro):
        self.acronym = acro
        
    def add_history_onStock(self):
        #save on each history track
        for x in self.history_track:
            x.add_history(10)
        
    def insert_stock(self):
        #create Sotck directly on method inside
        x = Stocks()
        x.insert_stock()
        self.stocks.append(x)
        
    def add_stock_to_history(self, stock):
        for x in self.history_track:
            if stock == x.name:
                print("Exist")
        return None
    
    def add_stock(self, name, cost, quantity, date):
        #give person a stock by parameters
        stockX = Stocks(name, cost, quantity, date)
        self.stocks.append(stockX)
        if self.is_on_track(name):
            print("\t\t new stock")
        else:
            print("\t\tRepeated stock")
    
    def is_on_track(self, name):
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
        
    def add_track(self, name, date, price):
        if self.is_on_track(name):
            #IF DO NOT EXIST, THEN IT IS CREATED AND NOW ADD VALUE
            self.find_and_add_on_track(name, date, price)
        else:
            self.find_and_add_on_track(name, date, price)
            
    def find_and_add_on_track(self, name, date, price):
        print("Find and add on track list")
        for x in self.history_track:
            if name == x.name:
                x.add_history(price)
    
    
    def print_stock(self):
        print(self.name , "(" , self.acronym, ")")
        for x in self.stocks:
            x.stock()
            print("\n")
        if len(self.history_track) >0:
            print("\tThese are the history")
            for x in self.history_track:
                lenx = x.get_len()
                x0 =0
                while x0 < lenx:
                    strX = x.get_value_hist(x0)
                    print("\t", strX)
                    x0+=1
            
            
    def take_action(self):
        choice = input("What to do?  ")
        print("1. save value on txt")
        if int(choice) == 1:
            f = open(os.path.join('Exel_Python_control', "stocks3.txt"), "w")
            f.write("Person: " + self.name+"\n")
            f.write("Acronym: " + self.acronym+"\n")
            for stockX in self.stocks:
                strX = stockX.get_name() + " " + str(stockX.get_quantity()) + " " + str(stockX.get_price()) + " " + stockX.get_date() +"\n"
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
    
        
    def get_name(self):
        return self.name
    
    def get_quantity(self):
        return self.quantity
    
    def get_price(self):
        return self.cost
    
    def get_date(self):
        return self.date
        
    def stock(self):
        print("\tThese are the Stocks")
        print("\tName: ", self.name )
        print("\tQuantity: ", self.quantity)
        print("\tDate bought: ", self.date)
        
    def insert_stock(self):
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
    
    def get_len(self):
        return len(self.history)
        
    def add_history(self, value):
        dateX = date.today()
        hist0 = (str(dateX), value)
        self.history.append(hist0)
        
    def get_value_hist(self, run_t):
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
# stockX.insert_stock()
# stockX.stock()
# # stockX =  Stocks(nameX, quantityX, dateX, priceX)

# choice = input("What to do?")
# print("1. save value on txt")
# if int(choice) == 1:
#     f = open("\stocks2.txt", "w")
#     strX = stockX.get_name() + " " + str(stockX.get_quantity()) + " " + str(stockX.get_price()) + " " + stockX.get_date() +"\n"
#     f.write(strX)
    
# pp = Person()
# pp.name_insert()
# pp.insert_stock()
# pp.print_stock()


gg = Group()
pp1 = Person()
pp1.name_insert_PP("Pablo", "PB")
pp1.add_stock("PSY", 10, 12, "12/09/2022")
pp1.add_stock("DISN", 1, 120, "12/01/2022")
gg.insert_person(pp1)

pp2 = Person()
pp2.name_insert_PP("Yetta", "YT")
pp2.add_stock("POT", 8, 40, "10/09/2020")
pp2.add_stock("SEN", 2, 35, "08/01/2019")
gg.insert_person(pp2)
# gg.insert_person_New()
# gg.insert_person(pp)
# gg.insert_person_New()
gg.print_group()
gg.take_action()

    
    
    



    


