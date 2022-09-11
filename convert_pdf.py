import pdftables_api
import shutil 
import os 

source_dir = "/Users/wincheng/Desktop/VSCoding/FinanceAutomation"


def Scan_Files(source_dir):
    # Scan the directory and get an iterator of os.DirEntry objects
    # corresponding to entries in it using os.scandir() method
    obj = os.scandir(source_dir)
    
    # List all files and directories in the specified source_dir
    with os.scandir(source_dir) as itr:
#starting the loop running through all files contained within the directory 
        for entry in itr :
            file_name = entry.name

            if file_name.endswith(".pdf"):
                convert_to_CSV(file_name)


def convert_to_CSV(file_name):
    c = pdftables_api.Client('zu9hzrgc0b3u')
    c.csv(file_name, file_name) 

Scan_Files(source_dir)
#replace c.xlsx with c.csv to convert to CSV
#replace c.xlsx with c.xml to convert to XML
#replace c.xlsx with c.html to convert to HTML