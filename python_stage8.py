from datetime import date
from python_stage5 import Group
import os

def control_Group(Groupx):

    time_date = date.today()
    print(date.today())

    # f = open("stocks.txt", "r")
    f = open(os.path.join('Exel_Python_control', "stocks3.txt"), "r")

    f2 = f.readlines()
    print(f2)
    y3 = []

    run_length = 0
    for x in f2:
        print(x)
        y1 = x.strip()
        print(y1)
        y2 = y1.split()
        print(y2[0])
        if y2[0] == "Person:":
            run_length+=1
            Groupx.Group_create_person(y2[1])
            print("Super")
        else:
            if y2[0] == "Acronym:":
                Groupx.Group_add_person_acronym(y2[1], run_length-1)
                print("Super Acronym")
                
            elif y2[0] == "!ST:":
                print("HISTORYXX: ", y2[2])
                Groupx.Group_add_history_person( y2[1], y2[2], y2[3], run_length-1)
                # print(y2)
            else:
                print(y2[0])
                tt = y2[0]
                # gg = yf.Ticker(tt)
                print(tt)
                
                gg_price = float(y2[2])
                # gg.info["regularMarketPrice"]
                print(y2[0], ": $", gg_price)
                
                gg_quantity = int(y2[1])
                
                Groupx.Group_add_stock_person(y2[0], gg_price, gg_quantity, str(y2[3]), run_length-1)
                y3.append(y2)
                print("STOCK")

        
        # y2[1] = str(int(y2[1])+1) 
        # y3.append(y2)
        #print(x.strip())
    f.close()


# Groupx = Group()

# control_Group(Groupx)

# pp_ll = Groupx.Group_ret_list_persons()

# print(pp_ll)

# Groupx.Group_take_action()

