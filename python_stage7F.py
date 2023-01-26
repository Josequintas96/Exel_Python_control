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
    
    cell_border_full = workbook.add_format()
    cell_border_full.set_border(style=2)
    
    cell_border_full_brown = workbook.add_format()
    cell_border_full_brown.set_border(style=2)
    cell_border_full_brown.set_color("brown")
    
    cell_color_b = workbook.add_format()
    cell_color_b.set_color('blue')
    
    
    worksheet = workbook.add_worksheet(GroupX.Group_get_persons_acronym(person))
    stockX =0
    row =2
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
        total_qu =0
        total_pri =0
        
#///////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////        

#        THIS SECTION IS FOR THE TITLE AND BASIC INFO OF THE STOCK

#///////////////////////////////////////////////////////////////////////////////////////////////        
#///////////////////////////////////////////////////////////////////////////////////////////////        
        cell_stock_title = workbook.add_format({'bg_color': '#82CAFF'})
        cell_stock_title.set_font_color("#123456")
        cell_stock_title.set_font_size(16)
        
        worksheet.write(row,column+1, pp_l[i1], cell_stock_title)
        row+=1
        pp_S = GroupX.Group_get_person_stock_per_name(person, pp_l[i1]) #order of list name, quatity, cost, date
        for iP in pp_S:
            worksheet.write(row,column-1, str(iP[1]) + " stocks" ) #quantity
            total_qu += iP[1]
            worksheet.write(row ,column, iP[3] ) # date    
            worksheet.write(row ,column+1, iP[2], cell_border_full_brown ) #cost
            total_pri += iP[2]
            row+=1
        worksheet.write(row,column-1, str(total_qu) + " stocks" , cell_color_b)
        worksheet.write(row ,column, "Today" )
        worksheet.write(row ,column+1, total_pri , cell_border_full_brown)
        row+=2
        worksheet.write(row ,column+2, "Promedio" )
        promedio = 0
        worksheet.write(row ,column+3, promedio )
        
        
        row+=2
        row_n = row  
        
        
        print("This are all the repeated stocks:  ", pp_S)
        
        
#///////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////        

#       THIS SECTION IS FOR THE HISTORY OF THE STOCK FOR EACH TIME BOUGHT

#///////////////////////////////////////////////////////////////////////////////////////////////        
#///////////////////////////////////////////////////////////////////////////////////////////////        

        
        # title for history table
        worksheet.write(row,column, "$" )
        worksheet.write(row,column+1, "7%" )
        worksheet.write(row,column+2, "11%" )
        worksheet.write(row,column+3, "15%" )
        worksheet.write(row,column+4, "20%" )
        #this section is to print the history tack with algorithm
        hh_l = GroupX.Group_get_person_history_track(person, i1)
        i2 =0
        row +=1
        run_0 =0
        while i2 < len(hh_l):
            column =1
            worksheet.write(row,column, hh_l[i2][0] ) 
            # worksheet.write(row,column, pp_l[i1] )        
            worksheet.write(row,column+1, hh_l[i2][1] ) 
            
            
            var2 = "=("+str(hh_l[i2][1])+"*"+ "0.07)"+"+"+str(hh_l[i2][1])
            #print("\t", var2)
            worksheet.write(row,column+2, var2, cell_border_full)
            column+=1
                
            var2 = "=("+str(hh_l[i2][1])+"*"+ "0.10)"+"+"+str(hh_l[i2][1])
            #print("\t", var2)
            worksheet.write(row,column+2, var2, cell_border_full)
            column+=1
                
            var2 = "=("+str(hh_l[i2][1])+"*"+ "0.15)"+"+"+str(hh_l[i2][1])
            #print("\t", var2)
            worksheet.write(row,column+2, var2, cell_border_full)
            column+=1
                
            var2 = "=("+str(hh_l[i2][1])+"*"+ "0.20)"+"+"+str(hh_l[i2][1])
            #print("\t", var2)
            worksheet.write(row,column+2, var2, cell_border_full)
            column+=1
            last_cost = []
            
            
            #This section is to control board of total change per Stock bought
            
            for i3 in pp_S:
                
                stockT = i3[3].split("-")
                HS_T = hh_l[i2][0].split("-")
                # print("\tSTOCK DATE: ",stockT)
                # print("\tHISTORY DATEL ", HS_T )
                i4=0
                # run_Value
                run_v = False
                if stockT[0] < HS_T[0]:
                    # print("\t\t This will occur  ", i3[3])
                    run_v =True
                if run_v == False:
                    if stockT[0] == HS_T[0] and stockT[1] < HS_T[1]:
                        run_v =True
                if run_v == False:
                    if stockT[0] <= HS_T[0] and stockT[1] <= HS_T[1]:
                        if stockT[2] <= HS_T[2]:
                            run_v =True
                
                if run_v:
                    
                
                    var3 = float(i3[2])
                    
                    
                    var2 = ((float(hh_l[i2][1])*100)/var3)-100
                    
                    
                    cell_format = workbook.add_format()
                    if var2 <0:
                        cell_format.set_font_color('red')
                    else:
                        cell_format.set_font_color('blue')
                    worksheet.write(row,column+2, round(var2, 2), cell_format)
                    column+=1
                    print("Verifying last cost: ", run_0)
                    if run_0 == len(hh_l)-1:
                        last_cost.append(var2)
                    
            run_0+=1
            i2+=1
            row+=1
            
        runT=0
        
        
        
#///////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////        

#       THIS SECTION IS FOR THE RESULT FOR EACH TIME STOCK WAS BOUGHT

#///////////////////////////////////////////////////////////////////////////////////////////////        
#///////////////////////////////////////////////////////////////////////////////////////////////        
        cell_format_r = workbook.add_format()
        cell_format_r.set_font_color('red')
        cell_format_b = workbook.add_format()
        cell_format_b.set_font_color('blue')
        
        cell_format_rL = workbook.add_format()
        cell_format_rL.set_font_color('red')
        cell_format_rL.set_top(2)
        cell_format_rL.set_bottom(2)
        
        cell_format_bL = workbook.add_format()
        cell_format_bL.set_font_color('blue')
        cell_format_bL.set_top(2)
        cell_format_bL.set_bottom(2)
        
        
        cell_format_p = workbook.add_format()
        cell_format_p.set_font_color('purple')
        cell_format_p.set_top(2)
        cell_format_p.set_left(2)
        cell_format_p.set_bottom(2)
        
        cell_format_pL = workbook.add_format()
        cell_format_pL.set_font_color('purple')
        cell_format_pL.set_top(2)
        cell_format_pL.set_right(2)
        cell_format_pL.set_bottom(2)
        
        for i5 in pp_S:
            worksheet.write(row_n+runT,column+3, "Se compro en: " + i5[3] ) 
            worksheet.write(row_n+runT+2,column+3, "Utilidad" , cell_format_p) 
            
            var3 = float(i5[2])
            ind = int(runT/4)
            var2 = (var3*i5[1])*(last_cost[ind]/100)
            print("(", var3, "*", i5[1], ")*(", last_cost[ind], "/100)" )
            if var2 < 0:
                # cell_format.set_font_color('red')
                worksheet.write(row_n+runT+2,column+4, round(var2, 2) , cell_format_rL)
            else:
                # cell_format.set_font_color('blue')
                worksheet.write(row_n+runT+2,column+4, round(var2, 2) , cell_format_bL)
                
            if last_cost[ind] < 0:
                # cell_format.set_font_color('red')
                worksheet.write(row_n+runT+2,column+5, round(last_cost[ind],2) , cell_format_rL)
            else:
                # cell_format.set_font_color('blue')
                worksheet.write(row_n+runT+2,column+5, round(last_cost[ind],2 ), cell_format_bL)
                

            worksheet.write(row_n+runT+2,column+6, "% util" , cell_format_pL) 
                
            runT+=4
        
#///////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////        

#     THIS SECTION IS FOR THE TOTAL RERSULT OF THE STOCK IN GENERAL

#///////////////////////////////////////////////////////////////////////////////////////////////        
#///////////////////////////////////////////////////////////////////////////////////////////////        

        worksheet.write(row_n+runT+2,column+5, "Total" , cell_format_p)
        total = 0
        if total < 0:
            # cell_format.set_font_color('red')
            worksheet.write(row_n+runT+2,column+6, "Total" , cell_format_r)
        else:
            # cell_format.set_font_color('blue')
            worksheet.write(row_n+runT+2,column+6, "Total" , cell_format_b)
            
        
        worksheet.write(row_n+runT+5,column+6, "Valor" , cell_format_p)
        worksheet.write(row_n+runT+5,column+7, 0 , cell_format_p)
        
        worksheet.write(row_n+runT+6,column+6, "Today Date" , cell_format_p)
        
        worksheet.write(row_n+runT+7,column+6, "Total perdida" , cell_format_p)
        if total < 0:
            # cell_format.set_font_color('red')
            worksheet.write(row_n+runT+7,column+7, 0 , cell_format_r)
        else:
            # cell_format.set_font_color('blue')
            worksheet.write(row_n+runT+7,column+7, 0 , cell_format_b)      
        
        
        
            
        if row_n+runT > row:
            row = row_n+runT+2
        
        i1+=1
        row +=3
    
    o0+=1
    row+=3

        
            
        
        
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
