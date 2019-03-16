# WAP to accept a folder name from user and create zip file out of contents of it.
import shutil

def main():
    inputDirPath = input("Please enter directory name: ")
    shutil.make_archive("outputZip", "zip", inputDirPath)
    print("Archived!")

if __name__ == "__main__":
    main()