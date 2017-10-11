import openpyxl

wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')
sheet['A1'] = 'A2'
print(sheet['A1'].value)
wb.save('test.xlsx')