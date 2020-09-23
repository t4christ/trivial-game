import xlrd
import csv
import json
# import pandas as pd
def Excel2CSV(ExcelFile, SheetName, CSVFile):

     workbook = xlrd.open_workbook(ExcelFile)
     worksheet = workbook.sheet_by_name(SheetName)
     csvfile = open(CSVFile, 'w')
     wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

     for rownum in range(worksheet.nrows):
         wr.writerow(worksheet.row_values(rownum))

     csvfile.close()


# def CSV2Json(CSVFile):
    
    # df = pd.read_csv(CSVFile)
    # any operations on dataframe df
    # df.to_json('question.json')
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
    Excel2CSV('new_answer.xlsx','Sheet1','answer.csv')
    # CSV2Json('question.csv')



# def correct_answer_list():
#     correct_answers_list = {"easy_ans": EasyAnswer, "medium_ans":MediumAnswer, "hard_ans":HardAnswer, "akwa_ans":AkwaIbomAnswer,
#     "xmas_ans":HardAnswer, "levone_ans":LevelOneAnswer, "levtwo_ans":LevelTwoAnswer, "levthree_ans":LevelThreeAnswer, "levfour_ans":LevelFourAnswer,
#     "levfive_ans":LevelFiveAnswer, "jacct_ans": JAccountAnswer, "jgeo_ans": JGeoAnswer, "jbio_ans": JBioAnswer,
#     "jphy_ans": JPhysicsAnswer, "jchem_ans": JChemistryAnswer, "jcomm_ans": JCommerceAnswer, "jict_ans": JIctAnswer,
#     "jcrk_ans": JCrkAnswer, "jlit_ans": JLiteratureAnswer, "jeco_ans": JEconomicsAnswer, "jgov_ans": JGovAnswer,
#     "jeng_ans": JEngAnswer, "jmath_ans": JMathAnswer 
#     }
#     return correct_answers_list

# 'JAccount':JAccountAnswer,'JGeo':JGeoAnswer,'JBio':JBioAnswer,'JPhysics':JPhysicsAnswer,'JChemistry':JChemistryAnswer,
# 'JCommerce':JCommerceAnswer,'JIct':JIctAnswer,'JCrk':JCrkAnswer,'JLiterature':JLiteratureAnswer,'JEconomics':JEconomicsAnswer,
# 'JGov':JGovAnswer

def double(n):
       return n*2