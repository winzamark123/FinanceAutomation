import gspread
from oauth2client.service_account import ServiceAccountCredentials
from scanner import *
from convert_pdf import *

bank_header_list = ["Transaction Date", "Description", "Amount", "Running Bal"]
tuition_header_list = ["Key", "Date", "Name/Purpose", "Amount", "Extra"]
rent_header_list = ["Date", "Amount"]

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
    ss = client.open("Personal Finance")
    ws = ss.worksheet('Sheet1') 
    val = ws.acell('B2').value
    
    return ss
    #print(val)

#Creates a new worksheet with each Month
def New_Month(cur_Month, cur_Year):
    ss = Connect_to_GSpread()
    worksheet = ss.add_worksheet(title= cur_Month + "-" + cur_Year)
    
    #Changing the Text Type
    worksheet.format("A1: L32",{
        #Changing the Text
        "textFormat": {
            "fontFamily" : "Georgia",
            "fontSize" : 10,
        }
    })
    
    worksheet.format("A1", {
        
        #Changing the Background Color
        "backgroundColorStyle":{
            #168, 143, 50 Color Cream
            "red" : 168 / 255,
            "green" : 143 / 255,
            "blue" : 50 / 255
        },

        #Changing the Text
        "textFormat": {
            "bold" : True
        }
    })

    worksheet.format("A3:C3", {

    })


Print_CSV(csv_dest_dir, "stmt.csv")
#CSV_Edit(csv_dest_dir, "stmt.csv", bank_header_list)