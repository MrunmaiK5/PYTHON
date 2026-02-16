import os
def main():
    DirectoryName = input("Enter the name of the directory : ")

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("Folder name : ",FolderName)
        
        for subf in SubFolderName:
            print("Subfolder name : ",subf)

        for fname in FileName:
            print("File name : ",fname)

if __name__ == "__main__":
    main()