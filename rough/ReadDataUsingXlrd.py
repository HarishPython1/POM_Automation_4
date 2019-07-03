import xlrd


#print("col count ",col_count)

# for i in range(row_count):# count val is 2 but index starts from zero
#     val = ws.cell_value(i, 0)
#     print(val)

# for i in range(col_count):# count val is 2 but index starts from zero
#     val = ws.cell_value(1, i)
#     print(val)

# for i in range(row_count):
#     for j in range(col_count):
#         val = ws.cell_value(i, j)
#         print(val)

# for i in range(row_count):
#     for j in range(col_count):
#         if (ws.cell_value(i, j)=='Password'):
#             val = ws.cell_value(i+1,j)
#     break
#
# print(val)

def get_val(Sheet_Name,input_val):
    wb = xlrd.open_workbook("C:/Users/BTM-Faculty/PycharmProjects/POM_Automation_4/data/datadriven.xlsx")
    ws = wb.sheet_by_name(Sheet_Name)
    row_count = ws.nrows
    col_count = ws.ncols
    for i in range(row_count):
        for j in range(col_count):
            if (ws.cell_value(i, j) == input_val):
                val = ws.cell_value(i + 1, j)
        break
    return val

returned_val = get_val("Login","UserName")
print(returned_val)

returned_val = get_val("Login","Password")
print(returned_val)


