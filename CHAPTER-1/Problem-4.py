import os

# Use the correct full path here
directory_path = r'C:\Users\Admin\OneDrive\Desktop\PYTHON\CHAPTER-1'

try:
    contents = os.listdir(directory_path)
    print(f"\nContents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"\nError: The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"\nError: Permission denied to access '{directory_path}'.")
