from convertor import Picture
import os
from pathlib import Path
import select_path
import handler


while True:
    handler.print_instructions()
    choice = input("Enter your choice: ")

    if choice.lower() in ['help', 'h', 'instructions']:
        handler.print_instructions()

    if choice.lower() in ['exit', 'e', 'quit', 'q']:
        print("Exiting the program.")
        break



    print("choose destination: ")
    folder = select_path.FileSelector().select_folder()

    conversion_format = input("Convert to:  ")

    if choice.lower() in ('file', 'image', 'photo', 'picture', 'pic'):
        print('choose your files: ')
        files = select_path.FileSelector().select_files()

        Picture(files, folder, conversion_format).convert()

    elif choice.lower() in ['folder', 'directory', 'dir', 'fold']:
        print("choose a folder: ")
        input_folder = select_path.FileSelector().select_folder()

        Picture(input_folder, folder, conversion_format).convert()