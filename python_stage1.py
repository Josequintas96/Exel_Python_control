#import xlsxwriter module
import xlsxwriter

#Workbook() takes one, non-optional, argument
#which is the filename that we want to create.
workbook = xlsxwriter.Workbook('hello.xlsx')

# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()

# Use the worksheet object to write
# data via the write() method.
#worksheet.write('A1', 'Hello..')
#worksheet.write('B1', 'Geeks')
#worksheet.write('C1', 'For')
#worksheet.write('D1', 'Geeks')

row = 1
column = 0
content = [1,2,3,4,5,6,7,8,10,11,12,13,14]

for item in content:
	worksheet.write(row,column, item)
	row+=1


# Finally, close the Excel file
# via the close() method.
workbook.close()
