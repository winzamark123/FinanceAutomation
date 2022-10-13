import shutil
import os 
import csv
from time import strftime
import pandas as pd
import datetime
import pathlib

#Starting Directories
bank_dir = "/Users/wincheng/Desktop/Finance_INFO/Bank_Statement/"

#Destination Directory (This Folder)
dest_dir = "/Users/wincheng/Desktop/VSCoding/FinanceAutomation/"

#copies the file within the directory to another dir
def Copy_Files(source_dir, file_name, dest_dir):
    #/home/Doc/Sample.txt
    # --> /home/Doc/Sample(copy).txt

    #Current file path
    cur_path = source_dir + "/" + file_name

    #final path of the file edit
    final_path = dest_dir + "/" + file_name + "(copied_by_python).pdf"

    #print(cur_path, final_path)

    try:
        shutil.copyfile(cur_path, final_path)
                
    except shutil.SameFileError:
        print(file_name + "is already in the folder")
        return

#scanning the files within the dir and RETURNS an Array based on file type
def Scan_Files(source_dir, file_type):

    names_array = []

    # Scan the directory and get an iterator of os.DirEntry objects
    # corresponding to entries in it using os.scandir() method
    obj = os.scandir(source_dir)
    
    # List all files and directories in the specified source_dir
    with os.scandir(source_dir) as itr:
#starting the loop running through all files contained within the directory 
        for entry in itr :
            file_name = entry.name

            if file_name.endswith(file_type):
                #print(file_name)
                
                names_array.append(file_name)
                #Copy_Files(source_dir, file_name, dest_dir)

    #returns an array of file names
    return names_array

#printing the CSV file onto terminal 
def Print_CSV(source_dir, file_name):
    path = source_dir + "/" + file_name
    pd.set_option("display.max_columns",4)
    #reads csv
    df = pd.read_csv(path)
    

    print(df)

#returning the CSV file 
def Return_CSV(source_dir, file_name):
    path = source_dir + "/" + file_name
    pd.set_option("display.max_columns",4)
    #reads csv
    df = pd.read_csv(path)
    df = df.fillna("")
    
    return df

#Edits CSV depending on header_type
#CURRENTLY SPECIFIC TO BANKSTMT
def CSV_Edit(source_dir, file_name, header_list):
    #Each type of files will contain different amount / ways of header_type
    path = source_dir + "/" + file_name

    #reads csv
    df = pd.read_csv(path, skiprows = 5)

    #edits csv, inputting the header
    df.to_csv(path, header=header_list, index=False)

#Get the date of each files in the file list 
def Get_Date(source_dir, file_list):

   

    i = 0
    sizeofList = len(file_list)

    f_name = [None] * sizeofList
    new_time = [None] * sizeofList

    while i < sizeofList:
        f_name[i] = pathlib.Path(source_dir + file_list[i])

        # get modification time
        m_timestamp = f_name[i].stat().st_mtime

        m_time = datetime.datetime.fromtimestamp(m_timestamp)
        
        new_time[i] = m_time.strftime("%m/%d/%Y")

        print("Time file was modified: " + new_time[i])
        i = i + 1
    
    return new_time

#Move the File into FinanceAutomation Dir
def Move_Files(source_dir, file_list, file_date, dest_dir):
    
    i = 0
    while i < len(file_date):

        files_exist = os.path.exists(dest_dir + file_list[i])

        #if the file is already in the folder 
        if files_exist:
            print("The file is already in the folder")
            return

        #updates the src_path with the folder's name + the file name
        src_path = source_dir + file_date[i]

        shutil.move(src_path, dest_dir)


#============================================================
#Starting Hash
print("Using Scanner.py!")
print("")


file_list = Scan_Files(bank_dir, ".csv")
print(file_list)

file_date = Get_Date(bank_dir, file_list)

print(file_date)

#Move_Files(bank_dir, file_list, file_date, dest_dir)


#using Scan_Files runs through the main directory (Finance_INFO)
# obj = os.scandir(bank_statement_dir)

# with os.scandir(bank_statement_dir) as itr:

#     for entry in itr :
#         if entry.name.startswith("."):
#             continue
        
#         #dir includes: Tuition / Rent / Bank 
#         new_file_name = Get_Date(bank_statement_dir, entry) 

         
    #print(hash)
