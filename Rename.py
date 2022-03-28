#Rename multiple files in a folder
 
# importing os module
import os
 
# Function to rename multiple files
def main():
   
    folder = r"xyz" #Enter dictory path
    folder.replace("\\","//") #To avoid escape sequence error
    folder.replace("/","//")
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"File_Name{str(count)}.format"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)
         
# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()
print("Rename successful")   