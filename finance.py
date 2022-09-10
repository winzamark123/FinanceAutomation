import shutil
import os 

#Starting Directories
main_source_dir = "/Users/wincheng/Desktop/Finance_INFO/"
tuition_dir = "/Users/wincheng/Desktop/Finance_INFO/Tuition"
rent_dir= "/Users/wincheng/Desktop/Finance_INFO/Rent"
bank_statement_dir = "/Users/wincheng/Desktop/Finance_INFO/Bank Statement"

#Destination Directory (This Folder)
dest_dir = "/Users/wincheng/Desktop/VSCoding/FinanceAutomation/"

def Copy_Files(source_dir, file_name, dest_dir):
    #/home/Doc/Sample.txt
    # --> /home/Doc/Sample(copy).txt

    #Current file path
    cur_path = source_dir + "/" + file_name

    #final path of the file edit
    final_path = dest_dir + file_name + "(copied_by_python).pdf"

    print(cur_path, final_path)

    shutil.copyfile(cur_path, final_path)


def Scan_Files(source_dir):
    # Scan the directory and get an iterator of os.DirEntry objects
    # corresponding to entries in it using os.scandir() method
    obj = os.scandir(source_dir)
    
    # List all files and directories in the specified source_dir
    with os.scandir(source_dir) as itr:
#starting the loop running through all files contained within the directory 
        for entry in itr :
            file_name = entry.name
            
            print(file_name)

            Copy_Files(source_dir, file_name, dest_dir)


Scan_Files(rent_dir)