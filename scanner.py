import shutil
import os 
import csv
import pandas as pd

#Starting Directories
main_source_dir = "/Users/wincheng/Desktop/Finance_INFO/"
tuition_dir = "/Users/wincheng/Desktop/Finance_INFO/Tuition"
rent_dir= "/Users/wincheng/Desktop/Finance_INFO/Rent"
bank_statement_dir = "/Users/wincheng/Desktop/Finance_INFO/Bank_Statement"

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

#Creating empty CSV Files for each presented in CSV_Copied_dir
def Create_Empty_CSV(source_dir, file_name):
    dest_dir = CSV_Edited_dir = "/Users/wincheng/Desktop/VSCoding/FinanceAutomation/CSV_Edited"
    


#reading and editing Tuition type CSV_Files
def Tution_CSV_Edit(source_dir, file_name):
    #with open(source_dir + file_name, 'r') as file:
    #    csvreader = csv.reader(file)

    path_file = source_dir + "/" + file_name
    CSV_Edited_dir = "/Users/wincheng/Desktop/VSCoding/FinanceAutomation/CSV_Edited"

    #Need to create an empty CSV File for each CSV presented first 
    #with open(path_file, "r") as F1:
        #with open()

    

    #col_list = ["Printable Bill"]
    #print(df["Printable Bill"])

    #Specific to Reading Tuition Payments
    #The first row of the CSV Files determines the Columns and name of the Col_List
    #Therefore needs to Append the first row of each CSV File Read:
    #   (Col 1: Key or Labeled ("Purchases and Adjustments"))
    #   (Col 2: Date)
    #   (Col 3: Name or Purpose)
    #   (Col 4: The Amount $)

    header_list = {"Key", "Date", "Name/Purpose", "Amount"}
    

    df.to_csv(CSV_Edited_dir + "/NEW_" + file_name, header = header_list, index = False)
             

#============================================================
#Starting Hash
print("Using Scanner.py!")
print("")
hash = {}

#using Scan_Files runs through the main directory (Finance_INFO)
obj = os.scandir(main_source_dir)

with os.scandir(main_source_dir) as itr:

    for entry in itr :
        if entry.name.startswith("."):
            continue

        #dir includes: Tuition / Rent / Bank 
        dir_name = main_source_dir + entry.name

        #using hash to store every pdf files in each dir 
        #KEY: dir_name
        #VALUE: array of filenames
        hash[dir_name] = Scan_Files(dir_name, ".pdf")
         
    #print(hash)
