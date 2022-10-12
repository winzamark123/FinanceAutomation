import gspread
from oauth2client.service_account import ServiceAccountCredentials
from scanner import *
from convert_pdf import *
from gspread_formatting import *

#Header Lists
bank_header_list = ["Transaction Date", "Description", "Amount", "Running Bal"]


def Connect_to_GSpread():
    #Connecting to Google Sheets
    #------------------------------------------
    # defining the scope of the application
    scope_app =['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'] 

    #credentials to the account
    cred = ServiceAccountCredentials.from_json_keyfile_name('win_finance_credentials.json',scope_app) 

    # authorize the clientsheet 
    client = gspread.authorize(cred)
    #------------------------------------------

    # Open the spreadsheet
    sh = client.open("Personal Finance")
    ws = sh.worksheet('Sheet1') 
    val = ws.acell('B2').value
    
    return sh
    #print(val)

#Creates a new worksheet with each Month
def Format_CSV(cur_Month, cur_Year):
    sh = Connect_to_GSpread()
    worksheet = sh.worksheet(cur_Month + cur_Year)

#=======================================================
#Fomatting Col / Row Sizes
    set_column_width(worksheet, 'A', 130)
    set_column_width(worksheet, 'B', 700)
#=======================================================
#Setting up the Text Format 
    # worksheet.format("A1:D1", {
    #     "bold" : True

    # })

    fmt = CellFormat(
        #Bright Orange 255, 172, 28
        backgroundColor=color(1, 0.67, 0.11),
        textFormat=TextFormat(bold = True)
    )

    format_cell_range(worksheet, "A1:D1", fmt)

#Updating the information stored in PD into Gspread
def Update_PD_Worksheet(cur_Month, cur_Year):
    sh = Connect_to_GSpread()
    worksheet = sh.add_worksheet(cur_Month + cur_Year, rows = 50, cols = 50)
    
#=======================================================
#Setting up the Information Template
    df = Return_CSV(csv_dest_dir, "stmt.csv")
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    

Print_CSV(csv_dest_dir, "stmt.csv")

Update_PD_Worksheet("Sep", "2022")
Format_CSV("Sep", "2022")
#CSV_Edit(csv_dest_dir, "stmt.csv", bank_header_list)