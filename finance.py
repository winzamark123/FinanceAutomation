import gspread
from oauth2client.service_account import ServiceAccountCredentials
from scanner import *
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
def Format_CSV(file_name):
    sh = Connect_to_GSpread()
    worksheet = sh.worksheet(file_name)

#=======================================================
#Fomatting Col / Row Sizes
    set_column_width(worksheet, 'A', 100)
    set_column_width(worksheet, 'B', 300)
    set_column_width(worksheet, 'C', 600)
    set_column_width(worksheet, 'D', 500)
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
def Update_PD_Worksheet(file_name):
    sh = Connect_to_GSpread()
    worksheet = sh.add_worksheet(file_name, rows = 50, cols = 50)
    
#=======================================================
#Setting up the Information Template
    df = Return_CSV(dest_dir, file_name)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    
def Title_Worksheet_List():
    title_list = []
    sh = Connect_to_GSpread()
    worksheet_list = sh.worksheets()

    for ws in worksheet_list:
        title_list.append(ws.title)

    return title_list

def Common_Sheet(worksheet_list, file_list):
    i = 0
    while i < len(worksheet_list):
        j = 0
        while j < len(file_list):
            if file_list[j] == worksheet_list[i]:
                file_list.remove(file_list[j])
            j = j + 1
        
        i = i + 1

    return file_list

var1 = Title_Worksheet_List()
print(file_list)
print(var1)
test = Common_Sheet(var1, file_list)
print(test)

#Print_CSV(dest_dir, file_list[0])

#Update_PD_Worksheet(file_list[0])
#Format_CSV(file_list[0])
#CSV_Edit(dest, "stmt.csv", bank_header_list)