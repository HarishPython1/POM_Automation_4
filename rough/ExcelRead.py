# import xlrd
# wb = xlrd.open_workbook("C:/Users/BTM-Faculty/PycharmProjects/POM_Automation_6/rough/data.xlsx")
# ws = wb.sheet_by_name("Sheet1")
# val1 = ws.cell_value(1,1)
# #print(val1)
#
# active_row_count = ws.nrows
# #print(active_row_count)
#
# active_col_count = ws.ncols
#print(active_col_count)

# for i in range(active_row_count):#2,starts from 0, ends with -1
#     print(ws.cell_value(i,0))


#to read first row data
# for i in range(active_col_count):
#     print(ws.cell_value(0,i))


# To read entire data
# for i in range(active_row_count):
#     for j in range(active_col_count):
#         print(ws.cell_value(i,j))

#to fetch values depending on column input
# for i in range(active_row_count):
#     for j in range(active_col_count):
#         if ws.cell_value(i,j)=="UN":
#             print(ws.cell_value(i+1,j))
#     break


#path
#"C:/Users/BTM-Faculty/PycharmProjects/POM_Automation_6/rough/data.xlsx"
#"Sheet1"
#"UN"

#Generic method to read data
def read_val(path,sheet_name,col_name):
    import xlrd
    wb = xlrd.open_workbook(path)
    ws = wb.sheet_by_name(sheet_name)
    active_row_count = ws.nrows
    active_col_count = ws.ncols
    for i in range(active_row_count):
        for j in range(active_col_count):
            if ws.cell_value(i,j)==col_name:
                return  ws.cell_value(i+1,j)
        break
val = read_val("C:/Users/BTM-Faculty/PycharmProjects/POM_Automation_6/rough/data.xlsx",
               "Sheet1","PWD")
print(val)




