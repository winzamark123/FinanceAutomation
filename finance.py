import gspread
from oauth2client.service_account import ServiceAccountCredentials
from scanner import *
from convert_pdf import *

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

print(val)
print()

Tution_CSV_Edit(csv_dest_dir, "RyderPayment_Sep22.pdf(copied_by_python).pdf.csv")
#CSV_Reader(csv_dest_dir, "Tuition_Fall_Aug2022.pdf(copied_by_python).pdf.csv")