import pdftables_api
from scanner import *

dest_dir = "/Users/wincheng/Desktop/VSCoding/FinanceAutomation"

def convert_to_CSV(file_name):
    c = pdftables_api.Client('zu9hzrgc0b3u')
    c.csv(file_name, file_name) 
#replace c.xlsx with c.csv to convert to CSV
#replace c.xlsx with c.xml to convert to XML
#replace c.xlsx with c.html to convert to HTML

for key, values in hash.items():
    for value in values:
        #print(str(key) + ":" + str(value))
        Copy_Files(str(key), str(value), dest_dir)

#Hashmap Structure:
#key: source_dir, value: file_name