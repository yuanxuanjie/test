# import xlrd
# file = xlrd.open_workbook("F:\wenjian.xls")
# fl = file.sheet_by_index(0)
# fl = file.sheet_by_name(shell1)
# print(fl.cell_value(0,3))

import xlwt
file = xlwt.Workbook()
bb = file.add_sheet('shell0')
f = input('data:')
bb.write(0,0,f)
file.save("F:\wj.xls")