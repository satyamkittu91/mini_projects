import convertor
import select_path
import os
from pathlib import Path
import handler
import json


while True:
    handler.print_instructions()
    choice = input("Enter your choice: ")


    if choice.lower() == "help":
        handler.print_instructions()

    if choice.lower() in ["exit", "e", "quit", "q"]:
        print("Exiting the program.")
        break

    if choice.lower() in ["file", "image", "photo", "picture", "pic"]:
        print("choose a file: ")
        file = select_path.FileSelector().select_files()
        if len(file) == 1:
            file = file[0]
        print("file selected: ", file)
        print("Choose a destination folder: ")
        destination = select_path.FileSelector().select_folder()
        print("destination folder selected: ", destination)

        print("select the format: ")
        format = input("Enter the format (tiff, jpeg, png, heic): ").lower()
        if format not in ["tiff", "jpeg", "png", "heic"]:
            print("Invalid format. Please choose from tiff, jpeg, png, or heic.")
            continue
        image = convertor.Picture(file, destination)
        if format == "tiff":
            image.convert_to_tiff()
        elif format == "jpeg":
            lossless = input("Do you want a lossless conversion? (y/n): ").lower() == "y"
            image.convert_to_jpeg(lossless=lossless)
        elif format == "png":
            image.convert_to_png()
        elif format == "heic":
            image.convert_to_heic()