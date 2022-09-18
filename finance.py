import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

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
sheet = client.open("Personal Finance")

val = sheet.acell('B1').value
print(val)