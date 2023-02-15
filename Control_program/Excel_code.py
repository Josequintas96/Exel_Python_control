import xlsxwriter
from datetime import date
from Group import Person, Stocks, Group
# import pandas as pdb
import os
from read_file import control_Group





# GroupX = Group()
# control_Group(GroupX)

# GroupX.Group_print_group()


def Exel_production(GroupX):
#add on Excel

    # workbook = xlsxwriter.Workbook('hello.xlsx')
    script_data = os.path.dirname(__file__)
    workbook = xlsxwriter.Workbook(os.path.join(script_data, 'Tabla_de_Acciones.xlsx'))
    content = [1,2,3,4,5]
    person =0
    row=1
    print("Length of Group Person: ", GroupX.Group_get_num_persons_stocks(person) )
    while person < GroupX.Group_get_num_persons():
        
        cell_border_full = workbook.add_format({'border': 2, 'center_across': True, 'valign': 'vcenter' })
        # cell_border_full.set_border(style=2)
        
        cell_border_full_brown = workbook.add_format({'border': 2, 'color': 'brown', 'center_across': True, 'valign': 'vcenter' })
        cell_simple = workbook.add_format({'center_across': True, 'valign': 'vcenter' })
        
        
        
        cell_color_b = workbook.add_format({"color": 'blue', 'center_across': True, 'valign': 'vcenter' })
        # cell_color_b.set_color('blue')
        
        
        worksheet = workbook.add_worksheet(GroupX.Group_get_persons_acronym(person))
        # 

        stockX =0
        row =2
        print("\tLength of Person Stocks: ", GroupX.Group_get_person_history_length(stockX) )
        # while stockX < GroupX.Group_get_num_persons_stocks(person):
            
        pp_l = GroupX.Group_get_person_history_stocks(person) #return all stocks in person using the history track, no repetition
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
            cell_stock_title = workbook.add_format({'bg_color': '#82CAFF' , 'text_wrap': True, 'font_color':"#123456", 'font_size': 16 , 'border': 2, 'center_across': True, 'valign': 'vcenter'  })
            # cell_stock_title.set_font_color("#123456")
            # cell_stock_title.set_font_size(16)
            
            pp_S = GroupX.Group_get_person_stock_per_name(person, pp_l[i1]) #repeated stocks on person in order of list name, quatity, cost, date, full_name
            valor_stock = 0 #stock cost multiply by number of them
            
            worksheet.set_column(column, column, 20) #adjust width of cell
            worksheet.write(row,column, pp_S[0][4], cell_stock_title)
            worksheet.write(row,column+1, pp_l[i1], cell_stock_title)
            row+=1
            
            for iP in pp_S:
                worksheet.write(row,column-1, str(iP[1]) + " stocks" , cell_simple) #quantity
                total_qu += int(iP[1])
                worksheet.write(row ,column, iP[3] , cell_simple) # date    
                worksheet.write(row ,column+1, round(iP[2],2), cell_border_full_brown ) #cost
                total_pri += iP[2]
                valor_stock += iP[1]*iP[2] #cost multiply by stock = total cost of sell
                row+=1
            worksheet.write(row,column-1, str(total_qu) + " stocks" , cell_color_b)
            
            dateX = date.today()
            worksheet.write(row ,column, str(dateX) , cell_simple)
            worksheet.write(row ,column+1, round(total_pri,2) , cell_border_full_brown)
            row+=2
            worksheet.write(row ,column+2, "Promedio", cell_border_full_brown )
            promedio = valor_stock/total_qu
            worksheet.write(row ,column+3, round(promedio,2), cell_border_full_brown )
            
            
            row+=2
            row_n = row -5
            
            
            # print("This are all the repeated stocks:  ", pp_S)
            
            
    #///////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////        

    #       THIS SECTION IS FOR THE HISTORY OF THE STOCK FOR EACH TIME BOUGHT

    #///////////////////////////////////////////////////////////////////////////////////////////////        
    #///////////////////////////////////////////////////////////////////////////////////////////////        

            
            # title for history table
            worksheet.write(row,column, "$", cell_simple )
            worksheet.write(row,column+1, "7%", cell_simple )
            worksheet.write(row,column+2, "11%" , cell_simple)
            worksheet.write(row,column+3, "15%" , cell_simple )
            worksheet.write(row,column+4, "20%" , cell_simple )
            #this section is to print the history track with algorithm
            hh_l = GroupX.Group_get_person_history_track(person, i1)
            i2 =0
            row +=1
            run_0 =0
            stock_p = [] #occurence thta stock must be inserted as title
            x=0
            while x < len(pp_S):
                stock_p.append(False)
                x+=1
            worksheet.set_column(1, 1, 10) #adjust width of cell for dates
            while i2 < len(hh_l):
                column =1
                worksheet.write(row,column, hh_l[i2][0], cell_simple ) 
                # worksheet.write(row,column, pp_l[i1] )        
                worksheet.write(row,column+1, hh_l[i2][1], cell_simple ) 
                
                
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
                last_cost = [] ##strore the fianl value of each purchase
                
                
                #This section is to control board of total change per Stock bought
                x=0
                # if len(last_cost) > 0:    
                for i3 in pp_S:
                    print("TOT")
                    stockT = i3[3].split("-")
                    HS_T = hh_l[i2][0].split("-")
                    # print("\tSTOCK DATE: ",stockT)
                    # print("\tHISTORY DATEL ", HS_T )
                    i4=0
                    # run_Value
                    run_v = False
                    print("\t\trun_0: ", run_0)
                    print("\t\tTOT ", len(hh_l)-1)
                    print("\t\tstockT: ", int(stockT[0]),  "  ", int(stockT[1]), "  ", int(stockT[2]))
                    print("\t\tHS_T: ", int(HS_T[0]),  "  ", int(HS_T[1]), "  ", int(HS_T[2]))
                    if int(stockT[0]) < int(HS_T[0]):
                        # print("\t\t This will occur  ", i3[3])
                        print("\t\tHappen run")
                        run_v =True
                    if run_v == False:
                        if int(stockT[0]) == int(HS_T[0]) and int(stockT[1]) < int(HS_T[1]):
                            print("\t\tHappen run")
                            run_v =True
                    if run_v == False:
                        if int(stockT[0]) <= int(HS_T[0]) and int(stockT[1]) <= int(HS_T[1]):
                            if stockT[2] <= HS_T[2]:
                                print("\t\tHappen run")
                                run_v =True
                    
                    if run_v:
                            
                        if stock_p[x] == False:
                            cell_gray = workbook.add_format({'bg_color': '#E8E4C9'})
                            worksheet.write(row-1,column+2, "Junior "+str(x) , cell_gray)
                            stock_p[x] = True
                        var3 = float(i3[2])
                        
                            
                        var2 = ((float(hh_l[i2][1])*100)/var3)-100
                            
                            
                        cell_format = workbook.add_format()
                        if var2 <0:
                            cell_format.set_font_color('red')
                        else:
                            cell_format.set_font_color('blue')
                        worksheet.write(row,column+2, round(var2, 2), cell_format)
                        column+=1
                            # print("Verifying last cost: ", run_0)
                        if run_0 == len(hh_l)-1:
                            print("\tappend happen")
                            last_cost.append(var2)
                        x+=1
                # else:
                #     column+=3
                run_0+=1
                i2+=1
                row+=1
                
            runT=0
            
            
            
    #///////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////        

    #       THIS SECTION IS FOR THE RESULT FOR EACH TIME STOCK WAS BOUGHT

    #///////////////////////////////////////////////////////////////////////////////////////////////        
    #///////////////////////////////////////////////////////////////////////////////////////////////    
            if len(hh_l) <= 0:
                column+=3
            print("\t\tLastCost: ", last_cost)
            print("\t\tPP_S: ", pp_S)
    
            cell_format_r = workbook.add_format({'color': 'red', 'center_across': True,})
            cell_format_b = workbook.add_format({'color': 'blue', 'center_across': True,})
            cell_format_rL = workbook.add_format({'color': 'red', 'top': 2, 'bottom': 2, 'center_across': True,})
            cell_format_bL = workbook.add_format({'color': 'blue', 'top': 2, 'bottom': 2, 'center_across': True,})
            cell_format_p = workbook.add_format({'color': 'purple', 'top': 2, 'bottom': 2, 'left': 2, 'center_across': True,})
            cell_format_pL = workbook.add_format({'color': 'purple', 'top': 2, 'bottom': 2, 'right':2, 'center_across': True,})
            
            total_of_each_stock = 0
            xx=0
            for i5 in pp_S:
                cell_cream = workbook.add_format({'bg_color': '#FFFFCC', 'align': 'center', 'center_across': True,})
                cell_gray = workbook.add_format({'bg_color': '#E8E4C9', 'center_across': True,})
                merge_row = row_n+runT
                merge_column = column+3
                worksheet.merge_range(merge_row,merge_column,merge_row,merge_column+2, "Se compro en: " + i5[3], cell_cream ) 
                
                total_p = i5[1]*i5[2]
                worksheet.write(row_n+runT,column+6, "Junior "+str(xx) , cell_gray)
                worksheet.write(row_n+runT,column+7, round(total_p,2) , cell_gray)
                worksheet.write(row_n+runT+2,column+3, "Utilidad" , cell_format_p) 
                
                var3 = float(i5[2])
                ind = int(runT/4)
                print("runT: ", runT)
                print("HHHH: ", ind)
                # if len(last_cost) > 0:
                var2 = 0
                if len(last_cost) >0:   
                    print("\t\t\tHHH: ", last_cost[ind])
                    var2 = (var3*i5[1])*(last_cost[ind]/100)
                # print("(", var3, "*", i5[1], ")*(", last_cost[ind], "/100)" )
                if var2 < 0:
                    # cell_format.set_font_color('red')
                    worksheet.write(row_n+runT+2,column+4, round(var2, 2) , cell_format_rL)
                else:
                    # cell_format.set_font_color('blue')
                    worksheet.write(row_n+runT+2,column+4, round(var2, 2) , cell_format_bL)
                
                if len(last_cost) > 0:  
                    if last_cost[ind] < 0:
                        # cell_format.set_font_color('red')
                        worksheet.write(row_n+runT+2,column+5, round(last_cost[ind],2) , cell_format_rL)
                    else:
                        # cell_format.set_font_color('blue')
                        worksheet.write(row_n+runT+2,column+5, round(last_cost[ind],2 ), cell_format_bL)
                    

                worksheet.write(row_n+runT+2,column+6, "% util" , cell_format_pL) 
                total_of_each_stock += var2
                runT+=4
                xx+=1
            
    #///////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////        

    #     THIS SECTION IS FOR THE TOTAL RERSULT OF THE STOCK IN GENERAL

    #///////////////////////////////////////////////////////////////////////////////////////////////        
    #///////////////////////////////////////////////////////////////////////////////////////////////        

            worksheet.write(row_n+runT+2,column+5, "Total" , cell_format_p)
            total = total_of_each_stock
            if total < 0:
                # cell_format.set_font_color('red')
                cell_border_full_cream = workbook.add_format({'bg_color': '#FFFFCC', 'center_across': True,})
                cell_border_full_cream.set_border(style=2)
                cell_border_full_cream.set_font_color('red')
                cell_border_full_cream.set_font_size(13)
                worksheet.write(row_n+runT+2,column+6, round(total, 2) , cell_border_full_cream)
            else:
                # cell_format.set_font_color('blue')
                cell_border_full_cream = workbook.add_format({'bg_color': '#FFFFCC', 'text_wrap': True , 'center_across': True,})
                cell_border_full_cream.set_border(style=2)
                cell_border_full_cream.set_font_color('blue')
                cell_border_full_cream.set_font_size(13)
                worksheet.write(row_n+runT+2,column+6, round(total, 2) , cell_border_full_cream)
                
            
            cell_table_up_cornerL = workbook.add_format({'font_color': 'purple', 'left': 2, 'top': 2, 'text_wrap': True, 'center_across': True })
            cell_table_up_cornerR = workbook.add_format({'font_color': 'purple', 'right': 2, 'top': 2 , 'text_wrap': True, 'center_across': True})
            cell_table_right_size = workbook.add_format({'font_color': 'purple', 'right': 2 , 'text_wrap': True, 'center_across': True,})
            cell_table_left_size = workbook.add_format({'font_color': 'purple', 'left': 2 , 'text_wrap': True, 'center_across': True,})
            cell_table_down_cornerL = workbook.add_format({'font_color': 'purple', 'left': 2, 'bottom': 2, 'text_wrap': True , 'center_across': True,})
            
            
            
            worksheet.write(row_n+runT+5,column+6, "Valor" , cell_table_up_cornerL)
            worksheet.write(row_n+runT+5,column+7, round(valor_stock, 2)  , cell_table_up_cornerR)
            
            
            worksheet.write(row_n+runT+6,column+6, "" , cell_table_left_size)
            worksheet.write(row_n+runT+6,column+7, "" , cell_table_right_size)
            
            worksheet.write(row_n+runT+7,column+6, "Total perdida" ,cell_table_down_cornerL )
            if total < 0:
                # cell_format.set_font_color('red')
                cell_table_down_cornerR = workbook.add_format({'font_color': 'red', 'right': 2, 'bottom': 2 })
                worksheet.write(row_n+runT+7,column+7, round(total,2) , cell_table_down_cornerR)
            else:
                # cell_format.set_font_color('blue')
                cell_table_down_cornerR = workbook.add_format({'font_color': 'blue', 'right': 2, 'bottom': 2 })
                worksheet.write(row_n+runT+7,column+7, round(total,2) , cell_table_down_cornerR)      
            
            
            
                
            if row_n+runT+7 > row:
                row = row_n+runT+7
            
            cell_separator = workbook.add_format({'bg_color': '#43302E'})
            worksheet.merge_range(row+2,0,row+3,column+7, "", cell_separator ) 
            
            i1+=1
            row +=6
        
        o0+=1
        row+=3   
            
        cell_separator = workbook.add_format({'bg_color': '#43302E'})
        worksheet.merge_range(row+2,0,row+3,column+7, "", cell_separator ) 
            
    #///////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////        

    #     THIS SECTION IS FOR THE TOTAL STOCK RESULTS 

    #///////////////////////////////////////////////////////////////////////////////////////////////        
    #///////////////////////////////////////////////////////////////////////////////////////////////        
        
        i9 = 0
        #run for each stock
        cartera_value = 0
        promedio_list = []
        valor_stock_list = []
        total_qu_list = []
        while i9 < len(pp_l):
            pp_S = GroupX.Group_get_person_stock_per_name(person, pp_l[i9]) #repeated stocks on person in order of list name, quatity, cost, date
            #Calculate promedio and total quantity
            for iP in pp_S:
                total_qu += iP[1]
                total_pri += iP[2]
                valor_stock += iP[1]*iP[2] #cost multiply by stock = total cost of sell
            total_qu_list.append(total_qu)
            valor_stock_list.append(valor_stock)
            promedio_list.append(valor_stock/total_qu)
            cartera_value+=valor_stock
            
            i9+=1
        
        # cell_Final_table_title = 
        row+=6
        
        columnT =2
        cell_stock_title = workbook.add_format({'bold': True, 'font_color': '#123456', 'font_size': 12 })
        cell_stock_result = workbook.add_format({'bold': True, 'font_color': 'black', 'font_size': 12 })
        worksheet.write(row,columnT+2, "Nro. Acciones" , cell_stock_title)
        worksheet.write(row,columnT+3, "Costo", cell_stock_title )
        worksheet.write(row,columnT+4, "Total" , cell_stock_title)
        worksheet.write(row,columnT+5, "% Cartera", cell_stock_title )
        
        
        cell_stock_name = workbook.add_format({'bg_color': '#82CAFF' , 'text_wrap': True, 'border': 2, 'font_color': '#123456', 'font_size': 16 })
        cell_stock_details = workbook.add_format({'text_wrap': True, 'border': 2, 'center_across': True, 'valign': 'vcenter' })

            
        valor_stock = 0 #stock cost multiply by number of them
        i9 = 0
        row+=1
        total_perc=0
        pp_t = GroupX.Group_get_full_name_for_stock_list(person, pp_l)
        print("Full NAME: ", pp_t)
        # cell_Final_table_name
        while i9 < len(pp_l):
            worksheet.set_column(columnT, columnT, 20) #adjust width of cell
            worksheet.write(row,columnT, pp_t[i9], cell_stock_name )
            worksheet.write(row,columnT+1, pp_l[i9], cell_stock_details )
            worksheet.write(row,columnT+2, round(total_qu_list[i9],2), cell_stock_details )
            worksheet.write(row,columnT+3, round(promedio_list[i9],2), cell_stock_details )
            worksheet.write(row,columnT+4, round(valor_stock_list[i9],2), cell_stock_details )
            perc_cartera = (valor_stock_list[i9]/cartera_value)*100
            total_perc+=perc_cartera
            worksheet.write(row,columnT+5, round(perc_cartera,2), cell_stock_details )  
            row+=1      
            i9+=1
        worksheet.write(row,columnT+4, round(cartera_value,2), cell_stock_result )
        #  perc_cartera = (valor_stock_list[i9]/cartera_value)*100
        worksheet.write(row,columnT+5, round(total_perc,2) , cell_stock_result)  
        
            
        person+=1

        

        
    workbook.close()


    # print("FINISHED")
    # return True



