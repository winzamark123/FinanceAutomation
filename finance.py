from urllib import request
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from scanner import *
from gspread_formatting import *
from googleapiclient import discovery
from Google import *

#Header Lists
bank_header_list = ["Transaction Date", "Description", "Amount", "Running Bal"]

#defining the scope of the application
scope_app = ["https://www.googleapis.com/auth/spreadsheets"] 

#credentials to the account
cred = ServiceAccountCredentials.from_json_keyfile_name("win_finance_credentials.json",scope_app) 

#secret JSON File
secret_file = "win_OAuth.json"

#spreadsheet_id
spreadsheet_id = "1Ok7bCIplJnvrLn8ltPFJrG9YxOpbeTvQzVrXoEsWPI4"

# authorize the clientsheet 
client = gspread.authorize(cred)

def Connect_to_GSpread():
    #Connecting to Google Sheets
    #------------------------------------------
    # defining the scope of the application
    scope_app =["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"] 

    #credentials to the account
    cred = ServiceAccountCredentials.from_json_keyfile_name("win_finance_credentials.json",scope_app) 

    # authorize the clientsheet 
    client = gspread.authorize(cred)
    #------------------------------------------

    # Open the spreadsheet
    sh = client.open("Personal Finance")
    ws = sh.worksheet("Sheet1") 
    val = ws.acell("B2").value
    
    return sh


#Creates a new worksheet with each Month
def Format_Gspread(file_name):
    sh = Connect_to_GSpread()
    worksheet = sh.worksheet(file_name)

#=======================================================
#Fomatting Col / Row Sizes
    set_column_width(worksheet, "A", 100)
    set_column_width(worksheet, "B", 200)
    set_column_width(worksheet, "C", 400)
    set_column_width(worksheet, "D", 300)
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

    format_cell_range(worksheet, "A1:E1", fmt)

#Updating the information stored in PD into Gspread
def Update_PD_Worksheet(file_name):
    sh = Connect_to_GSpread()
    worksheet = sh.add_worksheet(file_name, rows = 50, cols = 50)
    
#Setting up the Information Template
    df = Return_CSV(dest_dir, file_name)
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

#Gets the title of each worksheet from GSpread 
def Title_Worksheet_List():
    title_list = []
    sh = Connect_to_GSpread()
    worksheet_list = sh.worksheets()

    for ws in worksheet_list:
        title_list.append(ws.title)

    return title_list

#Checks the Common Sheets between CSV and GSpread and remove it 
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

#Creates a pie chart based on spending type
def Pie_Chart(file_name, row_num):
    sourceSheet_id = "1113555184"
    sheet_ID = "1676022265"
    API_NAME = "sheets"
    API_VERS = "v4"
    service = Create_Service(secret_file, API_NAME, API_VERS, scope_app)

    request_body = {
      "requests" : [
        {
          "addChart":{
            "chart":{
              "spec":{
                "title" : "Spending Types",
                "pieChart": {
                  "legendPosition" : "BOTTOM_LEGEND",
                  "threeDimensional" : True,
                  "domain" : {
                    "sourceRange" : {
                      "sources" : [
                        {
                          "sheetId": sourceSheet_id,
                          "startRowIndex" : 0,
                          "endRowIndex" : 7,
                          "startColumnIndex" : 0,
                          "endColumnIndex" : 1
                        }
                      ]
                    }
                  },
                  "series" : {
                    "sourceRange" : {
                      "sources" : [
                        {
                        "sheetId" : sourceSheet_id,
                        "startRowIndex" : 0,
                        "endRowIndex" : 7,
                        "startColumnIndex" : 4,
                        "endColumnIndex" : 5
                        }
                      ]
                    }
                  },
                }
              },
              "position" : {
                "overlayPosition": {
                  "anchorCell": {
                    "sheetId": sheet_ID,
                    "rowIndex": 2,
                    "columnIndex": 2
                  },
                  "offsetXPixels": 50,
                  "offsetYPixels": 50
                }
              }
            }
          }
        }
      ]
    }
    request = service.spreadsheets().batchUpdate(
      spreadsheetId = spreadsheet_id,
      body = request_body
    )
    response = request.execute()

    print("Print Chart Successfully!")





#=======================================================
raw_worksheet = Title_Worksheet_List()
print(file_list)
print(raw_worksheet)
final_list = Common_Sheet(raw_worksheet, file_list)
print(final_list)

i = 0

#Pie_Chart(file_list, 53)

#Start Updating All the CSV Files onto GSpread
# while i < len(final_list):
#     Update_PD_Worksheet(final_list[i])
#     Format_Gspread(final_list[i])
#     i = i + 1 


