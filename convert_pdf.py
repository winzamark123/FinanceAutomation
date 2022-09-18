import pdftables_api
from scanner import *

#Starting Directories
pdf_dest_dir = "/Users/wincheng/Desktop/VSCoding/FinanceAutomation/PDF_Copied"
csv_dest_dir = "/Users/wincheng/Desktop/VSCoding/FinanceAutomation/CSV_Copied"
cur_dir = "/Users/wincheng/Desktop/VSCoding/FinanceAutomation"

#convert the file_name into CSV
def convert_to_CSV(file_name):
    c = pdftables_api.Client('p6cuwg6w4n60')
    c.csv(file_name, file_name) 
#replace c.xlsx with c.csv to convert to CSV

#moving the files in source_dir with dest_dir 
def Move_Files(source_dir, file_name, dest_dir):
    
    files_exist = os.path.exists(dest_dir + "/" + file_name)

    #if the file is already in the folder 
    if files_exist:
        print("The file is already in the folder")
        return

    #updates the src_path with the folder's name + the file name
    src_path = source_dir + "/" + file_name

    shutil.move(src_path, dest_dir)


#============================================================
#copying pdf files from the main dir (Finance_INFO) into dest_dir (PDF_Copied) 
def copying_PDF_files():
    #an array of existing files
    Existing_PDF_Files = checking_existing_files()

    for key, values in hash.items():
        for value in values:
            #check if the name is the same 
            updated_value = value + "(copied_by_python).pdf"

            if updated_value in Existing_PDF_Files:
                print(updated_value + " Already Exists")
                continue
            
            #print("Copying" + str(value))
            Copy_Files(str(key), str(value), cur_dir)




            
            
    print("Finished Copying!")
    print()
  
#moving the converted CSV files into CSV_Copied dir 
def moving_CSV_files():
    CSV_Files = Scan_Files(cur_dir, ".csv")

    for csv_file in CSV_Files:
        Move_Files(cur_dir, csv_file, csv_dest_dir)

    print("Finished Moving CSV!")
    print()

#moving the remaining PDF files into PDF_Copied dir
def moving_PDF_files():
    PDF_Files = Scan_Files(cur_dir, ".pdf")

    for pdf_file in PDF_Files:
        Move_Files(cur_dir, pdf_file, pdf_dest_dir)

    print("Finished Moving PDF!")
    print()

#converting all pdf files in PDF_Copied to csv files
def convert_all_to_CSV():
    PDF_Files = Scan_Files(cur_dir, ".pdf")

    for pdf_file in PDF_Files:
        convert_to_CSV(pdf_file)

    print("Finished Converting!")
    print()

#returns an array of file names which exists in PDF_Copied dir
def checking_existing_files():
    Existing_PDF_Files = Scan_Files(pdf_dest_dir, ".pdf")

    return Existing_PDF_Files 


#=====================================
#STARTING THE PROGRAM!

copying_PDF_files()
convert_all_to_CSV()
moving_CSV_files()
moving_PDF_files()
