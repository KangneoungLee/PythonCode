import re
import win32com.client as win32
import os

file_name = 'BA_F15_V5.1.par'
excel_file_name = '\TP_name_change_list__to상엽씨.xlsx'
sheet_name = 'S16toU8'

f = open(file_name)
txt = f.read()
f.close()

excel = win32.gencache.EnsureDispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Open(os.getcwd()+excel_file_name)
ws = wb.Worksheets(sheet_name)

ws.Activate()

for i in range(2, ws.UsedRange.Rows.Count+1):
    before = ws.Cells(i, 1).GetValue()
    after = ws.Cells(i, 2).GetValue()

    p = re.compile(before + ' \[.*\]')
    if 'group' in dir(p.search(txt)):
        find_str = p.search(txt).group()
        if after.split('_')[0][0] == 'U':
            suffix = ' [' + after.split('_')[0].replace('U','UINT(') + ')' + ']'
        elif after.split('_')[0][0] == 'S':
            suffix = ' [' + after.split('_')[0].replace('S', 'INT(') + ')' + ']'
        txt = re.sub(before + ' \[.*\]', after + suffix, txt)
    else:
        print(before)

f = open('test.txt', 'w')
f.write(txt)
f.close()