import mini_projects.Image_convertor.convertor as convertor
import select_path
import os
from pathlib import Path
import handler
import json

format_func = {"tiff": convertor.Picture.convert_to_tiff,
               "jpeg": convertor.Picture.convert_to_jpeg,}

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
        files = select_path.FileSelector().select_files()

        for file in files:
            print("file selected: ", file)
        print("Choose a destination folder: ")
        destination = select_path.FileSelector().select_folder()
        print("destination folder selected: ", destination)

        print("select the format: ")
        format = input("Enter the format (tiff, jpeg, png, heic): ").lower()
        if format not in ["tiff", "jpeg", "png", "heic"]:
            print("Invalid format. Please choose from tiff, jpeg, png, or heic.")
            continue
        func = format_func.get(format)
        if format == "jpeg":
            lossless = input("Do you want a lossless conversion? (y/n): ").lower() == "y"
        for file in files:
            image = convertor.Picture(file, destination)
            if format == "tiff":
                image.convert_to_tiff()
            elif format == "jpeg":
                image.convert_to_jpeg(lossless=lossless)
            elif format == "png":
                image.convert_to_png()
            elif format == "heic":
                image.convert_to_heic()

    if choice.lower() in ["folder", "directory", "dir"]:
        print("choose a directory: ")
        input_folder = select_path.FileSelector().select_folder()

        print("choose the destination folder: ")
        destination_folder = select_path.FileSelector().select_folder()
        files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
        print(*files)

        print("select the format: ")
        format = input("Enter the format (tiff, jpeg, png, heic): ").lower()
        if format not in ["tiff", "jpeg", "png", "heic"]:
            print("Invalid format. Please choose from tiff, jpeg, png, or heic.")
            continue

        if format == "jpeg":
            lossless = input("Do you want a lossless conversion? (y/n): ").lower() == "y"
        for file in files:
            image = convertor.Picture(file, output_file_or_path=destination_folder)
            print(f"Converting {file} to {image.name}.{format}...")
            
            if format == "tiff":
                image.convert_to_tiff()
            elif format == "jpeg":
                image.convert_to_jpeg(lossless=lossless)
            elif format == "png":
                image.convert_to_png()
            elif format == "heic":
                image.convert_to_heic()
            
