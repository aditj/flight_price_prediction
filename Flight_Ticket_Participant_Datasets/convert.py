import xlrd
import csv
def csv_from_excel(name):
    wb= xlrd.open_workbook(name+'.xlsx')
    sh=wb.sheet_by_name('Sheet1')
    your_csv_file = open(name+'.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()


    