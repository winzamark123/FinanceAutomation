import shutil
import os 

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
