import pdftables_api
from scanner import *

dest_dir = "/Users/wincheng/Desktop/VSCoding/FinanceAutomation"

def convert_to_CSV(file_name):
    c = pdftables_api.Client('zu9hzrgc0b3u')
    c.csv(file_name, file_name) 
#replace c.xlsx with c.csv to convert to CSV
#replace c.xlsx with c.xml to convert to XML
#replace c.xlsx with c.html to convert to HTML

for item in h.map:
    if item is not None:
        print (item[0][0], "and", item[0][1][0])

            #Copy_Files(str(item[0][0]), str(item[0][1][0]), dest_dir)

#Hashmap Structure:
#key: source_dir, value: file_name