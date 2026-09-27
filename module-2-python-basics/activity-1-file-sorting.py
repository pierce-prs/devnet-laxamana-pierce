"""
Module 2 — Activity: File Sorting with os and shutil
Student: Laxamana, Pierce Darby A.
Date: September 27, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I have built a script that automatically cleans up a messy directory by sorting 
files into subfolders based on their file extensions!! where in The script scans the 
target folder, identifies the extension of each file (like .pdf, .py, or .pkt), 
creates a new folder named after that extension if it doesn't already exist, 
and moves the file inside.

============================================
KEY VOCABULARY
============================================
- os module: A built-in Python library that lets the script interact with the 
  operating system, allowing it to read folder contents, check file paths, and 
  create new directories.
- shutil module: A library used for high-level file operations, specifically 
  handling the actual moving or copying of files from one location to another.
- file path: The exact address of a file or folder on the computer 
- directory: Another word for a folder where files are stored.
- os.path.join(): A method that safely combines folder names and file names into 
  a full path, automatically using the correct slashes for Windows or Mac/Linux.

============================================
YOUR SCRIPT
============================================
"""

import os
import shutil

def sort_files_by_extension(folder_path):
    if not os.path.exists(folder_path):
        print(f"Error: The directory '{folder_path}' was not found.")
        return

    print(f"Scanning directory: {folder_path}\n")

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            file_name, file_extension = os.path.splitext(filename)
            
            if not file_extension:
                continue
                
            folder_name = file_extension[1:].lower()
            
            destination_folder = os.path.join(folder_path, folder_name)
            
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
                print(f"Created new folder: {folder_name}/")
                
            destination_path = os.path.join(destination_folder, filename)
            
            shutil.move(file_path, destination_path)
            print(f"Moved: {filename} -> {folder_name}/")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
A common mistake here is forgetting to include `if os.path.isfile(file_path):`. 
If you don't check whether the item is actually a file, the `os.listdir` loop 
will also grab the directories it just created. The script will then try to split 
a folder name as if it were a file, find no extension, and potentially crash or 
mess up the folder structure. 

Another mistake is using backslashes `\` in Windows file paths without putting 
an `r` (raw string) before the quote. Without it, Python 
might interpret `\U` or `\n` as escape characters, breaking the path.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional
"""
