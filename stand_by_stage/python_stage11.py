import xlsxwriter

workbook = xlsxwriter.Workbook('chart_line.xlsx')
worksheet = workbook.add_worksheet()

# Add the worksheet data to be plotted.
data = [256.56, 268.06, 267.78, 266.73, 271.42, 280.12, 276.516, 276.38]

dataX = ["2023-02-06", "2023-02-07", "2023-02-08", "2023-02-09", "2023-02-13", "2023-03-23", "2023-03-27", "2023-03-28"]

dataP = [
    [256.56, "2023-02-06" ],
    [268.06, "2023-02-07" ],
    [267.78, "2023-02-08" ],
    [266.73, "2023-02-09"],
    [271.42, "2023-02-13"],
    [280.12, "2023-03-23"],
    [276.516, "2023-03-27"],
    [276.38, "2023-03-28"]    
    ]


# worksheet.write(0,3, "$" ) 
worksheet.write_column('B1', data)
worksheet.write_column('C1', dataX)

worksheet.write(9,3, 256.56 )
worksheet.write(10,3, 268.06 )
worksheet.write(11,3, 267.78 )
worksheet.write(12,3, 266.73 )
worksheet.write(13,3, 271.42 )

# Create a new chart object.
chart = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
chart.add_series({
                    # 'name': ['Sheet1', 0, 3],
                    # 'categories': ['Sheet1', 0, 1, 6, 0],
                    'values': ['Sheet1', 9, 3, 13, 3]
                    # 'values': '=Sheet1!$D$10:$D$12',
                })

#  'values': ['Sheet1', 9, 0, 6, 0]


# Insert the chart into the worksheet.
worksheet.insert_chart(0,6, chart)

workbook.close()



