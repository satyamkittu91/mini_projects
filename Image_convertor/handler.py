import convertor
from tkinter import Tk, filedialog
import os

def destination_folder():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    destination_folder = filedialog.askdirectory(title="Select Destination Folder")
    root.destroy()
    return destination_folder


def select_file():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_paths = filedialog.askopenfilenames(title="Select Files", filetypes=[("Image Files", "*.heic *.jpg *.jpeg *.png *.tiff *.bmp *.gif *.webp")])
    root.destroy()
    return file_paths

