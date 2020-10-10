import csv
import sys
csv.field_size_limit(sys.maxsize)
a='solar'     #String that you want to search
try:
    with open("googlebooks-eng-1M-2gram-20090715-75.csv") as f_obj:
        reader = csv.reader(f_obj, delimiter='\t')
        for line in reader:      #Iterates through the rows of your csv
            print("Line",line)          #line here refers to a row in the csv
            if a in line:      #If the string you want to search is in the row
                print("String found in first row of csv")
                # break
except Exception as e:
    print("Exception caught",e)