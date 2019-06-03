import xlrd
import csv
import json
import pandas as pd
def Excel2CSV(ExcelFile, SheetName, CSVFile):

     workbook = xlrd.open_workbook(ExcelFile)
     worksheet = workbook.sheet_by_name(SheetName)
     csvfile = open(CSVFile, 'w')
     wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

     for rownum in range(worksheet.nrows):
         wr.writerow(worksheet.row_values(rownum))

     csvfile.close()


def CSV2Json(CSVFile):
    
    df = pd.read_csv(CSVFile)
    # any operations on dataframe df
    df.to_json('question.json')
    # data_list = list()  
    # with open(CSVFile, 'r') as f:
    #     reader = csv.reader(f, delimiter=';')
        
    #     for row in reader:
    #         data_list.append(row)
    # data = [dict(zip(data_list[0],row)) for row in data_list]
    # data.pop(0)
    # s = json.dumps(data)
    # print (s)

if __name__ == "__main__":
    Excel2CSV('new_answer.xls','Sheet1','answer.csv')
    CSV2Json('answer.csv')




