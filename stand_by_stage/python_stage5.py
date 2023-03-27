import os
from datetime import date
import yfinance as yf



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
        
    def Group_person_exist(self, name, acro):
        for x in self.PP:
            if x.name == name or x.acronym == acro:
                return False
        return True
        
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
                self.Group_add_stock_person(name, float(cost), int(quantity), date, i)
                return True
            i+=1
        print("NOT FOUND")
        return False
    
    def Group_add_stock_person(self, name, cost, quantity, date, run_person):
        self.PP[run_person].Person_add_stock(name, cost, quantity, date)
        
    def Group_add_full_stock_person(self, name, cost, quantity, date, full_name, run_person):
        self.PP[run_person].Person_add_full_stock(name, cost, quantity, date, full_name)
        
    def Group_add_history_person(self, name, date, price, run_person):
        self.PP[run_person].Person_add_to_track(name, date, price)
    
    def Group_get_person_history_stocks(self, run_person):
        #return all stocks in person using the history track, no repetition
        if run_person < 0:
            return None
        if run_person > len(self.PP):
            return None
        return self.PP[run_person].Person_stock_list_in_history()
    
    def Group_get_full_name_for_stock_list(self, run_person , stock_list):
        #return all stocks in person using the history track, no repetition
        if  run_person > len(self.PP):
            return None
        return self.PP[run_person].Person_get_full_name_for_stock_list(stock_list)
    
    def Group_get_person_history_length(self, run_person):
        #return the number of each person stock history track => how many different stocks has the person (no repetition)
        return self.PP[run_person].Person_stock_history_length()
    
    def Group_get_person_history_track(self, run_person, run_history):
        #return track of all histoies stored in each history values
        return self.PP[run_person].Person_history_track_L(run_history)
    
    def Group_print_group(self):
        for x in self.PP:
            x.Person_print_stock()
        # print("\n")
            
    def Group_set_up_history(self):
        # print("\t\tSet up history for all persons")
        for pers in self.PP:
            pers.Person_add_history_onStock()
            
    def Group_back_up_history(self):
        # print("\t\Back up history for all persons")
        for pers in self.PP:
            pers.Person_back_up_history_onStock()
            

    def Group_get_person_stock_per_name(self, run_person, stock_name):
        #return list with all stocks price and date with specific name
        return self.PP[run_person].Person_get_all_stock_per_name(stock_name)
    
    
    def Group_get_peron_run_person(self, person_name):
        i0=0
        while i0<len(self.PP):
            if self.PP[i0].name == person_name:
                return i0
            i0+=1
        return None
            
    def Group_stock_verification(self, name):
        gg_info = yf.Ticker(name)
        info = gg_info.info
        if info == None:
            # print(f"Cannot get info, it probably does not exist")
            return False
        else:
            return True
    
    def Group_delete_stock(self, person_name, stock_name, quantity):
        # print("Delete Stock of Person  => ", person_name)
        # print("Delete Stock  => ", stock_name)
        # print("Delete Stock  => ", int(quantity))
         
        run_person = self.Group_get_peron_run_person(person_name)
        self.PP[run_person].Person_delete_Stock(stock_name, int(quantity))
        
    def Group_Sort_Person(self):
        print("Sort stocks in each Persons in Group")
        for x in self.PP:
            x.Person_Sort_Stocks()
    
            
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
            # print("\tSAVE FILE was chosen")
            #you are writing all your info in a txt file
            f = open(os.path.join('Exel_Python_control', "stocks3.txt"), "w")
            for x in self.PP:
                f.write("Person: " + x.name+"\n")
                f.write("Acronym: " + x.acronym+"\n")
                for stockX in x.stocks:
                    strX = stockX.Stock_get_name() + " " + str(stockX.Stock_get_quantity()) + " " + str(stockX.Stock_get_price()) + " " + stockX.Stock_get_date() + " " + stockX.Stock_get_txt_full_name() +"\n"
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
            # print("\tHISTORY was chosen")
            self.Group_set_up_history()
                
        elif choice ==3:
            # print("\tPrint info")
            self.Group_print_group()
            
        elif choice ==4:
            # print("\tHISTORY was mean to be rewrite")
            self.Group_back_up_history()
        elif choice ==5:
            self.Group_Sort_Person()
            
        

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
            print("\t\t NAME: ", x.name)
            gg = yf.Ticker(x.name)
            gg.history(period="max")
            # gg_info = gg.info["regularMarketPrice"]
            gg_info = gg.history_metadata["regularMarketPrice"]
            
            print( x, " VALUE IS ", gg_info  )
            dateX = date.today()
            x.HS_add_history(dateX, gg_info)
            
    def Person_back_up_history_onStock(self):
        for x in self.history_track:
            x.HS_erase_history()
        
        
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
        stockX.Stock_set_Yahoo_full_name()
        self.stocks.append(stockX)
        if self.Person_is_on_track(name):
            print("\t\t new stock")
        else:
            print("\t\tRepeated stock")
            
    def Person_add_full_stock(self, name, cost, quantity, date, full_name):
        #give person a stock by parameters
        stockX = Stocks(name, cost, quantity, date)
        stockX.Stock_set_full_name(full_name)
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
        
    def Person_delete_track(self, name):
        if len(self.history_track) == 0:
            return False
        i0 =0
        while i0< len(self.history_track):
            print("HS__")
            if self.history_track[i0].name == name:
                del self.history_track[i0]
                print("This track should have been erase")
                break
            i0+=1
        
        return True
        
    def Person_stock_exist(self, stock_name):
        i0 =0
        while i0 < len(self.stocks):
            if self.stocks[i0].name == stock_name:
                return True
            i0+=1
        return False
    
    def Person_Sort_Stocks(self):
        # print("\tSort stcoks in Person")
        # i_for = 0
        # while i_for < len(self.stocks)-1:
        #     if self.stocks[i_for+1].name < self.stocks[i_for]:
        #         i_back = i_for+1
                
            
        #     i_for +=1
        self.stocks.sort(key=lambda x: x.name, reverse=False)
        self.history_track.sort(key=lambda x: x.name, reverse=False)
        
        
        
    def Person_add_to_track(self, name, date, price):
        if self.Person_is_on_track(name):
            #IF DO NOT EXIST, THEN IT IS CREATED AND NOW ADD VALUE
            self.Person_find_and_add_on_track(name, date, price)
        else:
            self.Person_find_and_add_on_track(name, date, price)
            
    def Person_stock_list_in_history(self):
        #return a list with all possible stocks considering list, no repetiton
        HS_stockL= []
        if len(self.history_track) > 0:
            # print("VVVVV")
            HS_stockL.append(self.history_track[0].name)
            if len(self.history_track) > 1:
                # print("VVVVVVVVV")
                i=1
                while i < len(self.history_track):
                    HS_stockL.append(self.history_track[i].name)
                    i+=1
        return HS_stockL
    
    def Person_get_full_name_for_stock_list(self, stock_list):
        HS_stock_name = []
        i0 =0
        while i0 < len(stock_list):
            i1=0
            while i1 < len(self.stocks):
                if self.stocks[i1].name == stock_list[i0]:
                    HS_stock_name.append(self.stocks[i1].full_name)
                    i1 = len(self.stocks)
                i1+=1
            i0+=1
        return HS_stock_name
    
    def Person_history_track_L(self, run_history):
        #return history of certain value
        return self.history_track[run_history].HS_get_history_list()
    
    def Person_get_all_stock_per_name(self, stock_name):
        #retrun list of all stock value and date with same name
        pp_S = []
        
        for x in self.stocks:
            if x.name == stock_name:
                cart = []
                cart.append(x.name)
                cart.append(x.quantity)
                cart.append(x.cost)
                cart.append(x.date)
                cart.append(x.full_name)
                
                pp_S.append(cart)
        return pp_S
                
                
    
    def Person_stock_history_length(self):
        return len(self.history_track)
            
    def Person_find_and_add_on_track(self, name, date, price):
        print("Find and add on track list")
        for x in self.history_track:
            if name == x.name:
                x.HS_add_history(date, price)
                
    def Person_delete_Stock(self, name_stock, stock_quantity):
        i0 = 0
        while i0 < len(self.stocks):
            if self.stocks[i0].name == name_stock:
                stock_quantity = self.stocks[i0].Stock_reduce_quantity(stock_quantity)
                    
                if self.stocks[i0].quantity <= 0:
                    print("To erase the stock: ", len(self.stocks))
                    del self.stocks[i0]
                    print("To erase the stock: ", len(self.stocks))
                    i0-=1
                    
                if stock_quantity <0:
                    stock_quantity = -stock_quantity
                elif stock_quantity >=0:
                    i0 = len(self.stocks)
                    break;
            i0+=1
            
        if self.Person_stock_exist(name_stock) == False:
            print("We are erasing the Stock")
            self.Person_delete_track(name_stock)
        
        
    
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
    full_name = ""
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
    
    def Stock_reduce_quantity(self, quantity):
        self.quantity -= quantity
        return self.quantity
    
    def Stock_get_quantity(self):
        return self.quantity
    
    def Stock_get_price(self):
        return self.cost
    
    def Stock_get_date(self):
        return self.date
    
    def Stock_get_full_name(self):
        return self.full_name
    
    def Stock_get_txt_full_name(self):
        n = self.full_name.split()
        full_n = n[0]
        if len(n) > 1:
            i0=1
            while i0 < len(n):
                full_n = full_n + "_" + n[i0]
                i0+=1
        print("\t\tSSS: ", full_n)
        return full_n
        
    def Stock_print_stock_value(self):
        print("\tThese are the Stocks")
        print("\tName: ", self.name )
        print("\tFull name: ", self.full_name)
        print("\tQuantity: ", self.quantity)
        print("\tDate bought: ", self.date)
        
    def Stock_set_Yahoo_full_name(self):
        gg = yf.Ticker(self.name)
        gg_name = gg.info['longName']
        self.full_name = gg_name 
        
    def Stock_set_full_name(self, name):
        self.full_name = name 
        
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
        
    def HS_add_history(self, dateX, value):
        # dateX = date.today()
        dateX = dateX
        hist0 = (str(dateX), value)
        self.history.append(hist0)
        
    def HS_erase_history(self):
        self.history.pop()
        
    def HS_get_value_hist(self, run_t):
        if len(self.history) == 0:
            strX = self.name + " No Stock History\n"
            return strX
        if run_t >= len(self.history):
            strX="p"
            return strX
        strX = self.name + " " + str(self.history[run_t][0]) + " " + str(self.history[run_t][1]) + "\n"
        return strX
    
    def HS_get_history_list(self):
        return self.history
    
