import pdftables_api
from scanner import *

#Starting Directories
dest_dir = "/Users/wincheng/Desktop/VSCoding/FinanceAutomation"

#convert the file_name into CSV
def convert_to_CSV(file_name):
    c = pdftables_api.Client('zu9hzrgc0b3u')
    c.csv(file_name, file_name) 
#replace c.xlsx with c.csv to convert to CSV


#============================================================
for key, values in hash.items():
    for value in values:
        
        Copy_Files(str(key), str(value), dest_dir)
        print()

files_in_dir = Scan_Files(dest_dir)

#for pdf_files in files_in_dir:
   #convert_to_CSV(pdf_files)

#Hashmap Structure:
#key: source_dir, value: file_name