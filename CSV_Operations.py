from typing import Type
from scanner import *
from gspread_formatting import *


source_dir = "/Users/wincheng/Desktop/Finance_INFO/Bank_Statement/"

#Calculate the total Amount of Transaction
def Calculate_Sum(file_name):
    df = Remove_Payment(file_name)
    sum = 0

    Amount_Col = df["Amount"] 

    for amount in Amount_Col:
        sum = sum + amount
    
    print(sum)
    return sum

#Determine the Type of Transaction 
def Type_of_Transac(file_name):
     #Types Include:
        # - UCD : UC Davis
        # - AMZN: Amazon : Shopping
        # - DD:Door Dash : Food
        # - LA Creperie : Food
        # - WALMART : Walmart : Food


    Groceries = 0
    Groceries_Amount = 0

    Fast_Food = 0
    Fast_Food_Amount = 0
    
    School = 0
    School_Fees = 0

    Online_Orders = 0
    Online_Orders_Amount = 0

    Others = 0
    Others_Amount = 0


    df = Remove_Payment(file_name)


    #Checking Each Category and Adding it to the Type
    #===================================================================
    x = 0

    #Iterate over all the rows on CSV
    for x, row in df.iterrows():

        #if Category starts with DoorDash / DD = Fast_Food is added
        if df.loc[x, "Payee"].startswith("DOORDASH") or df.loc[x, "Payee"].startswith("DD"):
            Fast_Food = Fast_Food + 1
            Fast_Food_Amount = Fast_Food_Amount + df.loc[x, "Amount"]
            continue

        #Fast Food
        if df.loc[x, "Payee"].startswith("RAISING") or df.loc[x, "Payee"].startswith("IN N OUT") or df.loc[x, "Payee"].startswith("BASKIN") or df.loc[x, "Payee"].startswith("SHELL"):
            Fast_Food = Fast_Food + 1
            Fast_Food_Amount = Fast_Food_Amount + df.loc[x, "Amount"]
            continue

        #Walmart and Savemart
        if df.loc[x, "Payee"].startswith("WALMART") or df.loc[x, "Payee"].startswith("SAVEMART"):
            Groceries = Groceries + 1
            Groceries_Amount = Groceries_Amount + df.loc[x, "Amount"]
            continue

        #Online Orders
        if df.loc[x, "Payee"].startswith("AMAZON") or df.loc[x, "Payee"].startswith("AMZN") or df.loc[x, "Payee"].startswith("eBay"):
            Online_Orders = Online_Orders + 1
            Online_Orders_Amount = Online_Orders_Amount + df.loc[x, "Amount"]
            continue

        #School
        if df.loc[x, "Payee"].startswith("CHEGG") or df.loc[x, "Payee"].startswith("UCD"):
            School = School + 1
            School_Fees = School_Fees + df.loc[x, "Amount"]
            continue

       

        #Others 
        Others = Others + 1
        Others_Amount = Others_Amount + df.loc[x, "Amount"]
    
    print("Groceries:", Groceries)
    print("Groceries Amount", Groceries_Amount)

    print("Fast Food:", Fast_Food)
    print("Fast Food Amount:", Fast_Food_Amount)

    print("Online Orders", Online_Orders)
    print("Online Orders Amount:", Online_Orders_Amount)

    print("School", School)
    print("School Fees:", School_Fees)

    print("Others", Others)
    print("Others Amount:", Others_Amount)

    Array_Amount = [Groceries_Amount, Fast_Food_Amount, Online_Orders_Amount, School_Fees, Others_Amount]
    
    return Array_Amount

#Removing the Rows where Payment is done
def Remove_Payment(file_name):
    df = Return_CSV(source_dir, file_name)
    
    for x, row in df.iterrows():
        if df.loc[x, "Amount"] > 0:
            df.drop(x, inplace=True)
    
    return df

#Updates the Last Row of CSV with the Values of Types of Payment
def Update_Last_Row_CSV(file_name):
    df = Remove_Payment(file_name)
    Array_Amount = Type_of_Transac(file_name)

    df.loc[-1, ["Posted Date", "Reference Number","Payee", "Address", "Amount"]] \
        = ["Total Groceries:" + str(Array_Amount[0]), "Total Fast Food:" + str(Array_Amount[1]) \
            ,"Total Online Orders:" + str(Array_Amount[2]), "Total School Fees:" + str(Array_Amount[3]), "Total Others:" + str(Array_Amount[4])]
    
    pd.set_option("display.max_columns",6)
    
    return df

def Perc_Type_Spent(file_list):
    perc = 0

#================================================================

# Remove_Payment(file_list)
# Calculate_Sum(file_list)
# Type_of_Transac(file_list)
#Update_Last_Row_CSV(file_list)