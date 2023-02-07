# import yfinance as yf
# import xlsxwriter
from datetime import date
from python_stage5 import Person, Stocks, Group
# import pandas as pdb
import os




time_date = date.today()
print(date.today())



# f = open("stocks.txt", "r")
f = open(os.path.join('Exel_Python_control', "stocks3.txt"), "r")

f2 = f.readlines()
print(f2)
y3 = []

Groupx = Group()
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
            print("HISTORYXX")
            Groupx.Group_add_history_person( y2[1], y2[2], y2[3], run_length-1)
            # print(y2)
        else:
            print(y2[0])
            tt = y2[0]
            # gg = yf.Ticker(tt)
            print(tt)
            
            gg_info = 100
            # gg.info["regularMarketPrice"]
            print(y2[0], ": $", gg_info)
            
            Groupx.Group_add_stock_person(y2[0], gg_info, 1, str(time_date), run_length-1)
            y3.append(y2)
            print("STOCK")

    
    # y2[1] = str(int(y2[1])+1) 
    # y3.append(y2)
    #print(x.strip())
f.close()

print(y3)
Groupx.Group_print_group()

# for x in y3:
    # print(x[0])
    # gg = yf.Ticker(x[0])
    # yf.pdr_override()
    # gg_info = gg.info["regularMarketPrice"]
    # start = str(time_date)
    # gg_info = pdb.get_data_yahoo(symbols=["regularMarketPrice"], start = start, end=start)
    # print(x[0])
    # print(x[0], ": $", gg_info)
    #print(x.strip())
    
    
    


#add on Excel
workbook = xlsxwriter.Workbook('hello.xlsx')
content = [1,2,3,4,5]
person =0
row=1
while person < Groupx.Group_get_num_persons():
    worksheet = workbook.add_worksheet(Groupx.get_persons_acronym(person))
    stockX =0
    row =1
    while stockX < Groupx.Group_get_num_persons_stocks(person):
        column =0
        worksheet.write(row,column, Groupx.get_persons_stock_date(person, stockX) )
                
        column +=1
        # gg = yf.Ticker(item[0])
        # gg_info = gg.info["regularMarketPrice"]
        gg_info = Groupx.get_persons_stock_price(person, stockX)
        worksheet.write(row,column, Groupx.get_persons_stock_name(person, stockX))
        worksheet.write(row,column+1, gg_info)
            
            
        var2 = "=("+str(gg_info)+"*"+ "0.07)"+"+"+str(gg_info)
        print("\t", var2)
        worksheet.write(row,column+2, var2)
        column+=1
            
        var2 = "=("+str(gg_info)+"*"+ "0.10)"+"+"+str(gg_info)
        print("\t", var2)
        worksheet.write(row,column+2, var2)
        column+=1
            
        var2 = "=("+str(gg_info)+"*"+ "0.15)"+"+"+str(gg_info)
        print("\t", var2)
        worksheet.write(row,column+2, var2)
        column+=1
            
        var2 = "=("+str(gg_info)+"*"+ "0.20)"+"+"+str(gg_info)
        print("\t", var2)
        worksheet.write(row,column+2, var2)
        column+=1
            
        print("Add stuff")
        row+=1
        stockX+=1
    person+=1
    
    
    
    
    
    
# worksheet = workbook.add_worksheet('Foglio2')
# # worksheet.define_name("Hello")

# row = 1 #ROW IS REPRESENTED WITH LETTERS
# column = 0 #COLUMNS IS REPRESENTED WITH NUMBERS
# content = [1,2,3,4,5,6,7,8,10,11,12,13,14]



# for x in content:
#     print("Add stuff")
#     worksheet.write(row,column, x)
#     row+=1
    

# for item in y3:
    # column =0
    # worksheet.write(row,column, str(date.today()) )
    
    # column +=1
    # gg = yf.Ticker(item[0])
    # gg_info = gg.info["regularMarketPrice"]
    # worksheet.write(row,column, item[0])
    # worksheet.write(row,column+1, gg_info)
    
    
    # var2 = "=("+str(gg_info)+"*"+ "0.07)"+"+"+str(gg_info)
    # print("\t", var2)
    # worksheet.write(row,column+2, var2)
    # column+=1
    
    # var2 = "=("+str(gg_info)+"*"+ "0.10)"+"+"+str(gg_info)
    # print("\t", var2)
    # worksheet.write(row,column+2, var2)
    # column+=1
    
    # var2 = "=("+str(gg_info)+"*"+ "0.15)"+"+"+str(gg_info)
    # print("\t", var2)
    # worksheet.write(row,column+2, var2)
    # column+=1
    
    # var2 = "=("+str(gg_info)+"*"+ "0.20)"+"+"+str(gg_info)
    # print("\t", var2)
    # worksheet.write(row,column+2, var2)
    # column+=1
    
    # print("Add stuff")
    # row+=1
    
# i0=0
# while i0 < 10:
#     print("HHH")
    
workbook.close()
