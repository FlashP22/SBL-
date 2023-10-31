import os

def list_files_in_current_directory():
    current_directory = os.getcwd()
    files = os.listdir(current_directory)

    print(f"Files in the current directory ({current_directory}):")
    for file in files:
        if os.path.isfile(file):
            print(file)

if __name__ == "__main__":
    list_files_in_current_directory()
