import pdftables_api
from scanner import *

#Starting Directories
pdf_dest_dir = "/Users/wincheng/Desktop/VSCoding/FinanceAutomation/PDF_Copied"
csv_dest_dir = "/Users/wincheng/Desktop/VSCoding/FinanceAutomation/CSV_Copied"

#convert the file_name into CSV
def convert_to_CSV(file_name):
    c = pdftables_api.Client('zu9hzrgc0b3u')
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
    for key, values in hash.items():
        for value in values:
            
            Copy_Files(str(key), str(value), pdf_dest_dir)
            
    print("Finished Copying!")
    print()
  
#moving the converted CSV files into CSV_Copied dir 
def moving_CSV_files():
    CSV_Files = Scan_Files(pdf_dest_dir, ".csv")

    for csv_file in CSV_Files:
        Move_Files(pdf_dest_dir, csv_file, csv_dest_dir)

    print("Finished Moving!")
    print()


#converting all pdf files in PDF_Copied to csv files
def convert_all_to_CSV():
    PDF_Files = Scan_Files(pdf_dest_dir, ".pdf")

    for pdf_file in PDF_Files:
        convert_to_CSV(pdf_file)

    print("Finished Converting!")
    print()

print("Starting the Program!")
print("")

copying_PDF_files
convert_all_to_CSV
moving_CSV_files
