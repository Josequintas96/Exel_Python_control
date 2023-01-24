# import yfinance as yf
import xlsxwriter
from datetime import date
from python_stage5 import Person, Stocks, Group
# import pandas as pdb
import os
from python_stage8 import control_Group





GroupX = Group()
control_Group(GroupX)

GroupX.Group_print_group()



#add on Excel
workbook = xlsxwriter.Workbook('hello.xlsx')
content = [1,2,3,4,5]
person =0
row=1
print("Length of Group Person: ", GroupX.Group_get_num_persons_stocks(person) )
while person < GroupX.Group_get_num_persons():
    worksheet = workbook.add_worksheet(GroupX.Group_get_persons_acronym(person))
    stockX =0
    row =1
    print("\tLength of Person Stocks: ", GroupX.Group_get_person_history_length(stockX) )
    # while stockX < GroupX.Group_get_num_persons_stocks(person):
        
    pp_l = GroupX.Group_get_person_history_stocks(person)
    print("\t", pp_l)
    o0 = 0
    column =2
    # while o0 < GroupX.Group_get_person_history_length(person):
    i1 = 0
    while i1 < len(pp_l):
        column =2
        print("\t\tSTOCK: ", pp_l[i1])
        worksheet.write(row,column, pp_l[i1] )
        #this section is to print the history tack with algorithm
        hh_l = GroupX.Group_get_person_history_track(person, i1)
        i2 =0
        row +=2
        while i2 < len(hh_l):
            column =2
            worksheet.write(row,column-1, hh_l[i2][0] )
            worksheet.write(row,column, pp_l[i1] )
            worksheet.write(row,column+1, hh_l[i2][1] )
            
            
            var2 = "=("+str(hh_l[i2][1])+"*"+ "0.07)"+"+"+str(hh_l[i2][1])
            print("\t", var2)
            worksheet.write(row,column+2, var2)
            column+=1
                
            var2 = "=("+str(hh_l[i2][1])+"*"+ "0.10)"+"+"+str(hh_l[i2][1])
            print("\t", var2)
            worksheet.write(row,column+2, var2)
            column+=1
                
            var2 = "=("+str(hh_l[i2][1])+"*"+ "0.15)"+"+"+str(hh_l[i2][1])
            print("\t", var2)
            worksheet.write(row,column+2, var2)
            column+=1
                
            var2 = "=("+str(hh_l[i2][1])+"*"+ "0.20)"+"+"+str(hh_l[i2][1])
            print("\t", var2)
            worksheet.write(row,column+2, var2)
            column+=1
            
            i2+=1
            row+=1
        i1+=1
        row +=3
    o0+=1
    row+=3

        
            
        
        
        # column =0
        # worksheet.write(row,column, GroupX.Group_get_persons_stock_date(person, stockX) )
                
        # column +=1
        # gg_info = GroupX.Group_get_persons_stock_price(person, stockX)
        # worksheet.write(row,column, GroupX.Group_get_persons_stock_name(person, stockX))
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
        # stockX+=1
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
    

    
workbook.close()


print("FINISHED")
