from finance import *
from scanner import *
from gspread_formatting import *

source_dir = "/Users/wincheng/Desktop/Finance_INFO/Bank_Statement/"

def Calculate_Sum(file_list):
    data = Return_CSV(source_dir, file_list[0])
    sum = 0

    Amount_Col = data["Amount"] 

    for amount in Amount_Col:
        sum = sum + amount
    
    print(sum)

def Type_of_Transac(file_list):
    data = Return_CSV(source_dir, file_list[0])
    
    Data_Type = {}


    Type_Col = data["Payee"]

    #Types Include:
        # - UCD : UC Davis
        # - AMZN: Amazon : Shopping
        # - DD:Door Dash : Food
        # - LA Creperie : Food
        # - WALMART : Walmart : Food

    #for type in Type_Col:
def Type_Spent(file_list):
    type_spent = 0

def Perc_Type_Spent(file_list):
    perc = 0




Calculate_Sum(file_list)