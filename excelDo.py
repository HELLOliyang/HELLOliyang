import xlrd
def read_data(excelFile):
    #打开excel
    data = xlrd.open_workbook(excelFile)
    #定位表单
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))
        # rowNum = table.row_values(rowNum)
    return dataFile
if __name__ == '__main__':
    excelFile = 'loginTest.xlsx'
    a = read_data(excelFile = excelFile)
    for i in a:
     print(a)

