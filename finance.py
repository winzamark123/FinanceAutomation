import gspread
from oauth2client.service_account import ServiceAccountCredentials
from scanner import *
from convert_pdf import *

bank_header_list = ["Transaction Date", "Description", "Amount", "Running Bal"]
tuition_header_list = ["Key", "Date", "Name/Purpose", "Amount", "Extra"]
rent_header_list = ["Date", "Amount"]


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

Print_CSV(csv_dest_dir, "stmt.csv")
#CSV_Edit(csv_dest_dir, "stmt.csv", bank_header_list)