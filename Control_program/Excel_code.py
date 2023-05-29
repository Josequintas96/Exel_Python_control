import xlsxwriter
from datetime import date
from Group import Person, Stocks, Group
# import pandas as pdb
import os
from read_file import control_Group


def date_conf(iP):
    ix = iP.split("-")
    ill = ix[2] + "/" + ix[1]+ "/" + ix[0]
    return ill


def Exel_production(GroupX):
#add on Excel
    script_data = os.path.dirname(__file__)
    workbook = xlsxwriter.Workbook(os.path.join(script_data, 'Tabla_de_Acciones.xlsx'))  #1.=. DOCUMENT IS CREATED
    person =0
    row=1
    print("Length of Group Person: ", GroupX.Group_get_num_persons_stocks(person) )
    
    #2.=. DIVIDE THE WORK FOR EACH PERSON
    while person < GroupX.Group_get_num_persons():
        
        #////////////////////////////////////////////////////////////////////////////////////////////////////#
        #////////////////////////////////////////////////////////////////////////////////////////////////////#
        #//////////////////        BASIC CELL FORMATS                   /////////////////////////////////////#
        #////////////////////////////////////////////////////////////////////////////////////////////////////#
        
        
        cell_border_full = workbook.add_format({'border': 2, 'center_across': True, 'valign': 'vcenter', 'text_wrap': True, 'font_name':'Arial' })
        # cell_border_full.set_border(style=2)
        
        cell_border_full_brown = workbook.add_format({'border': 2, 'color': 'brown', 'center_across': True, 'valign': 'vcenter', 'text_wrap': True, 'font_name':'Arial'  })
        simple_cell = workbook.add_format({'center_across': True, 'valign': 'vcenter', 'text_wrap': True,  'font_name':'Arial' })
        simple_cell_b = workbook.add_format({'center_across': True, 'valign': 'vcenter', 'text_wrap': True, 'bold': True, 'font_name':'Arial' })
        
        
        
        cell_color_b = workbook.add_format({"color": 'blue', 'center_across': True, 'valign': 'vcenter' })
        # cell_color_b.set_color('blue')
        
        
        set_chart_sheet_name = GroupX.Group_get_persons_acronym(person)
        worksheet = workbook.add_worksheet(GroupX.Group_get_persons_acronym(person)) #3.=. CREATE TAB FOR CURRENT PERSON
        # 

        row =2 #ORIGINAL START OF PROJECT ON ROW 2
        column =2 #ORIGINAL START OF PROJECT ON COLUMN 2
            
        pp_l = GroupX.Group_get_person_history_stocks(person) #return all stocks in person using the history track, there is no repetition OF STOCK
        # print("\t", pp_l)
        o0 = 0
        
        # while o0 < GroupX.Group_get_person_history_length(person):
        
        #4.=. RUN EACH STOCK 
        i1 = 0
        while i1 < len(pp_l):
            column =2
            # print("\t\tSTOCK: ", pp_l[i1])
            total_qu =0
            total_pri =0
        
            chart_price = [] #list to store begin and end for list of prices
            
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////#
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////#

    #//////   THIS SECTION IS FOR THE TITLE AND BASIC INFO OF THE STOCK (NAME, ACRONNYM, HISTORY TIMES BOUGHT)  ///#

    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////#
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////#
                #original color 'font_color':"#123456"
            cell_stock_title = workbook.add_format({'bg_color': '#A9FBF9' , 'text_wrap': True, 'font_color':"#123456", 'font_name':'Arial', 'bold': True,
                                                    'font_size': 10 , 'border': 2, 'center_across': True, 'valign': 'vcenter' })
            
            pp_S = GroupX.Group_get_person_stock_per_name(person, pp_l[i1]) #repeated stocks on person in order of list name, quatity, cost, date, full_name
            valor_stock = 0 #stock cost multiply by number of them
            
            worksheet.set_column(column, column+2, 20) #adjust width of cell
            # worksheet.set_column(column+4, column+8, 30) #adjust width of cell
            
            chart_price.append(row) #mark the first row where title is set up
            worksheet.write(row,column, pp_S[0][4], cell_stock_title)
            worksheet.write(row,column+1, pp_l[i1], cell_stock_title)
            row+=1
            
            #////////////////////////////////////////////////////////////////////////////////////////////////////#
            #//////////////////        HISTORY OF BOUGHT STOCKS             /////////////////////////////////////#
            #////////////////////////////////////////////////////////////////////////////////////////////////////#
            for iP in pp_S:
                worksheet.write(row,column-1, str(iP[1]) + " stocks" , simple_cell) #quantity
                total_qu += int(iP[1])
                
                
                worksheet.write(row ,column, date_conf(iP[3]) , simple_cell) # date    
                worksheet.write(row ,column+1, round(iP[2],2), cell_border_full_brown ) #cost
                total_pri += iP[2]*iP[1]
                valor_stock += iP[1]*iP[2] #cost multiply by stock = total cost of sell
                row+=1
            worksheet.write(row,column-1, str(total_qu) + " stocks" , cell_color_b)
            
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
            worksheet.write(row,column, "$", simple_cell_b )
            worksheet.write(row,column+1, "7%", simple_cell_b )
            worksheet.write(row,column+2, "11%" , simple_cell_b)
            worksheet.write(row,column+3, "15%" , simple_cell_b )
            worksheet.write(row,column+4, "20%" , simple_cell_b )
            #this section is to print the history track with algorithm
            hh_l = GroupX.Group_get_person_history_track(person, i1)
            i2 =0
            row +=1
            chart_price.append(row) #mark the first row when list start
            
            run_0 =0
            stock_p = [] #occurence thta stock must be inserted as title
            x=0
            while x < len(pp_S):
                stock_p.append(False)
                x+=1
            worksheet.set_column(1, 1, 10) #adjust width of cell for dates
            #################### DATE ##################################
            while i2 < len(hh_l):
                column =1
                worksheet.write(row,column, date_conf(hh_l[i2][0]), simple_cell ) 
                # worksheet.write(row,column, pp_l[i1] )      
                value_cost = float(hh_l[i2][1])  
                worksheet.write(row,column+1, round(value_cost,2), simple_cell ) 
                
                
                var2 = "=("+str(hh_l[i2][1])+"*"+ "0.07)"+"+"+str(hh_l[i2][1])
                #print("\t", var2)
                var7 = float(hh_l[i2][1])*0.07+float(hh_l[i2][1])
                worksheet.write(row,column+2, round(var7, 2), cell_border_full)
                column+=1
                    
                var2 = "=("+str(hh_l[i2][1])+"*"+ "0.11)"+"+"+str(hh_l[i2][1])
                var7 = float(hh_l[i2][1])*0.11+float(hh_l[i2][1])
                #print("\t", var2)
                worksheet.write(row,column+2, round(var7,2) , cell_border_full)
                column+=1
                    
                var2 = "=("+str(hh_l[i2][1])+"*"+ "0.15)"+"+"+str(hh_l[i2][1])
                var7 = float(hh_l[i2][1])*0.15+float(hh_l[i2][1])
                #print("\t", var2)
                worksheet.write(row,column+2, round(var7,2), cell_border_full)
                column+=1
                    
                var2 = "=("+str(hh_l[i2][1])+"*"+ "0.20)"+"+"+str(hh_l[i2][1])
                var7 = float(hh_l[i2][1])*0.2+float(hh_l[i2][1])
                #print("\t", var2)
                worksheet.write(row,column+2, round(var7,2), cell_border_full)
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
                            worksheet.write(row-1,column+2, "Junior "+str(x+1) , cell_gray)
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
            chart_price.append(row-1) #mark the last row when list end    
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
                worksheet.write(row_n+runT,column+6, "Junior "+str(xx+1) , cell_gray)
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
            
            
            if total < 0:
                # cell_format.set_font_color('red')
                worksheet.write(row_n+runT+7,column+6, "Perdida Total" ,cell_table_down_cornerL )
                cell_table_down_cornerR = workbook.add_format({'center_across': True, 'font_color': 'red', 'right': 2, 'bottom': 2 })
                worksheet.write(row_n+runT+7,column+7, round(total,2) , cell_table_down_cornerR)
            else:
                # cell_format.set_font_color('blue')
                worksheet.write(row_n+runT+7,column+6, "Ganancia Total" ,cell_table_down_cornerL )
                cell_table_down_cornerR = workbook.add_format({'center_across': True, 'font_color': 'blue', 'right': 2, 'bottom': 2 })
                worksheet.write(row_n+runT+7,column+7, round(total,2) , cell_table_down_cornerR)      
            
            
            
                
            if row_n+runT+7 > row:
                row = row_n+runT+7
            
            cell_separator = workbook.add_format({'bg_color': '#43302E'})
            worksheet.merge_range(row+2,0,row+3,column+12, "", cell_separator ) 
            
            i1+=1
            row +=6
        
        
            #///////////////////////////////////////////////////////////////////////////////////////////////
            #///////////////////////////////////////////////////////////////////////////////////////////////        
            #     THIS SECTION IS TO MAKE A CHART WITH INFO
            #///////////////////////////////////////////////////////////////////////////////////////////////        
            #///////////////////////////////////////////////////////////////////////////////////////////////        
            print("SUPER")
                        
            chart = workbook.add_chart({'type': 'line'}) #initialize the chart
            set_up_chart = chart_price[0]
            starting_row = chart_price[1]
            length_of_row = chart_price[2]
            # print("\t\t kkkkkkkkkkklll Set up chart: ", set_up_chart)
            # print("\t\t kkkkkkkkkkklll Starting row: ", starting_row)
            # print("\t\t kkkkkkkkkkklll length of row: ", length_of_row)
                        
                    # Add a series to the chart.
            chart.add_series({
                                'name': [set_chart_sheet_name, set_up_chart, 3],
                                'values': [set_chart_sheet_name, starting_row, 2, length_of_row, 2]
                                })

            # chart.add_series({'values': '=Sheet1!$C$11:$C$15'})

                        # Insert the chart into the worksheet.
            worksheet.insert_chart(set_up_chart+i1, column+10, chart)
        
            chart_price.clear()
        

        
    
    #///////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////        

    #     THIS SECTION IS FOR THE SEPARATION BETWEEN STOCK RESULTS 

    #///////////////////////////////////////////////////////////////////////////////////////////////        
    #///////////////////////////////////////////////////////////////////////////////////////////////         
            
        o0+=1
        row+=3    
        cell_separator = workbook.add_format({'bg_color': '#43302E'})
        worksheet.merge_range(row+2,0,row+3,column+12, "", cell_separator ) 
        
    
            
    #///////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////        

    #     THIS SECTION IS FOR THE TOTAL STOCK RESULTS 

    #///////////////////////////////////////////////////////////////////////////////////////////////        
    #///////////////////////////////////////////////////////////////////////////////////////////////        
        
        i9 = 0
        #run for each stock
        cartera_value = 0
        promedio_list = []
        valor_stock = 0
        valor_stock_list = []
        total_qu_list = []
        total_qu = 0
        while i9 < len(pp_l):
            pp_S = GroupX.Group_get_person_stock_per_name(person, pp_l[i9]) #repeated stocks on person in order of list name, quatity, cost, date
            #Calculate promedio and total quantity
            for iP in pp_S:
                print("IP:   ", iP)
                total_qu += iP[1]
                print("\t IP Quantity:  ", iP[1])
                print("\t Total Quantity:  ", total_qu)
                # total_pri += iP[2]
                valor_stock += iP[1]*iP[2] #cost multiply by stock = total cost of sell
                # print("   kkkkkkkl : ", iP[0], "  ", iP[1], "  ", iP[2])
            total_qu_list.append(total_qu)
            valor_stock_list.append(valor_stock)
            promedio_list.append(valor_stock/total_qu)
            cartera_value+=valor_stock
            total_qu =0
            # total_pri =0
            valor_stock =0
            
            i9+=1
        
        # cell_Final_table_title = 
        row+=6
        
        columnT =2
        cell_stock_title = workbook.add_format({'center_across': True, 'bold': True, 'font_color': '#123456', 'font_size': 12 })
        cell_stock_result = workbook.add_format({'center_across': True, 'bold': True, 'font_color': 'black', 'font_size': 12 })
        worksheet.write(row,columnT+2, "Nro. Acciones" , cell_stock_title)
        worksheet.write(row,columnT+3, "Costo/Promedio", cell_stock_title )
        worksheet.write(row,columnT+4, "Total" , cell_stock_title)
        worksheet.write(row,columnT+5, "% Cartera", cell_stock_title )
        
        
        cell_stock_name = workbook.add_format({'center_across': True, 'bg_color': '#A9FBF9' , 'text_wrap': True, 
                                               'border': 2, 'font_color': '#123456', 'font_size': 16 })
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



