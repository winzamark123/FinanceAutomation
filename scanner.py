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

def Scan_Files(source_dir):

    names_array = []

    # Scan the directory and get an iterator of os.DirEntry objects
    # corresponding to entries in it using os.scandir() method
    obj = os.scandir(source_dir)
    
    # List all files and directories in the specified source_dir
    with os.scandir(source_dir) as itr:
#starting the loop running through all files contained within the directory 
        for entry in itr :
            file_name = entry.name

            if file_name.endswith(".pdf"):
                #print(file_name)
                
                names_array.append(file_name)
                #Copy_Files(source_dir, file_name, dest_dir)
    
    return names_array

class HashMap:
    #initialize hashmap size 
    def __init__(self):
            self.size = 64
            self.map = [None] * self.size
    
    #getting the hash index 
    def _get_hash(self, key):
            hash = 0
            for char in str(key):
                    hash += ord(char)
            return hash % self.size
    
    #adding a key + value to the hashmap
    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
                self.map[key_hash] = list([key_value])
                return True
        else:
                for pair in self.map[key_hash]:
                        if pair[0] == key:
                                pair[1] = value
                                return True
                self.map[key_hash].append(key_value)
                return True
    
    #getting the value using the key
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
                for pair in self.map[key_hash]:
                        if pair[0] == key:
                                return pair[1]
        return None
    
    #deleting the value using the key
    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
                return False
        for i in range (0, len(self.map[key_hash])):
                if self.map[key_hash][i][0] == key:
                        self.map[key_hash].pop(i)
                        return True
        return False

    #printing the entire hash list
    def print(self):   
        for item in self.map:
                if item is not None:
                        print(str(item))

   
#============================================================
#Starting Hash
hash = {}

#using Scan_Files runs through the main directory
obj = os.scandir(main_source_dir)

with os.scandir(main_source_dir) as itr:

    for entry in itr :
        if entry.name.startswith("."):
            continue

        dir_name = main_source_dir + entry.name

        hash[dir_name] = Scan_Files(dir_name)
         
    #print(hash)


#while itr running, use Scan_Files again to go into specific directory 
#add each files into the hash map
#go through all the hashmaps and copy the files into Finance Automation dir using key and value