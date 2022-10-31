from typing import Type
from finance import *
from scanner import *
from gspread_formatting import *

source_dir = "/Users/wincheng/Desktop/Finance_INFO/Bank_Statement/"

#Calculate the total Amount of Transaction
def Calculate_Sum(file_list):
    df = Return_CSV(source_dir, file_list[0])
    sum = 0

    Amount_Col = df["Amount"] 

    for amount in Amount_Col:
        sum = sum + amount
    
    print(sum)

#Determine the Type of Transaction 
def Type_of_Transac(file_list):
     #Types Include:
        # - UCD : UC Davis
        # - AMZN: Amazon : Shopping
        # - DD:Door Dash : Food
        # - LA Creperie : Food
        # - WALMART : Walmart : Food

    Food = 0
    School = 0
    Online_Orders = 0
    Others = 0


    df = Return_CSV(source_dir, file_list[0])


    Type_Col = df[["Payee"]]
    Type_Col = Type_Col.astype(str)
    #print(Type_Col.values)

    #Checking Each Category and Adding it to the Type
    #===================================================================
    
    #Foods
    x = 0
    row = len(df)

    for x in range(len(df)):
        if list(map(lambda x: x.startswith("DOORDASH") or x.startswith("DD"), df["Payee"])):
            Food = Food + 1
        if list(map(lambda x: x.startswith("WALMART"), df["Payee"])):
            Food = Food + 1

        if list(map(lambda x: x.startswith("UCD"), df["Payee"])):
            School = School + 1

        if list(map(lambda x: x.startswith("AMZN"), df["Payee"])):
            Online_Orders = Online_Orders + 1
    

    print("Food:")
    print(Food)

    #Printing DF to Check 
    pd.set_option("display.max_columns",6)
    print(df)


    #df['student_id_starts_with_TCS'] = list(
    #map(lambda x: x.startswith('TCS'), df['Student_id'])) 

def Type_Spent(file_list):
    type_spent = 0

def Perc_Type_Spent(file_list):
    perc = 0




Calculate_Sum(file_list)
Type_of_Transac(file_list)