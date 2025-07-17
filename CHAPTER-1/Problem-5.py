import os  # Importing the os module to interact with the operating system

# Define the full path of the directory whose contents you want to list
directory_path = r'C:\Users\Admin\OneDrive\Desktop\New folder'  # Use raw string (r"...") to avoid issues with backslashes

# Use try-except block to handle possible errors like file not found or permission denied
try:
    # Get the list of all files and folders in the specified directory
    contents = os.listdir(directory_path)
    
    # Print the directory path
    print(f"\nContents of directory '{directory_path}':")
    
    # Loop through the list and print each item
    for item in contents:
        print(item)

# If the directory is not found, this block will handle the error
except FileNotFoundError:
    print(f"\nError: The directory '{directory_path}' does not exist.")

# If the program does not have permission to access the directory, this block will handle it
except PermissionError:
    print(f"\nError: Permission denied to access '{directory_path}'.")
