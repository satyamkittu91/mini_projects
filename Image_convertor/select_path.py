from tkinter import Tk, filedialog

class FileSelector:
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        self.root.attributes('-topmost', True)

    def select_files(self):
        file_paths = filedialog.askopenfilenames(title="Select Files", filetypes=[("Image Files", "*.heic *.jpg *.jpeg *.png *.tiff *.bmp *.gif *.webp")])
        return file_paths

    def select_folder(self):
        folder_path = filedialog.askdirectory(title="Select Folder with Images")
        return folder_path



'''
def destination_folder():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    destination_folder = filedialog.askdirectory(title="Select Destination Folder")
    root.destroy()
    return destination_folder


def select_files():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_paths = filedialog.askopenfilenames(title="Select Files", filetypes=[("Image Files", "*.heic *.jpg *.jpeg *.png *.tiff *.bmp *.gif *.webp")])
    root.destroy()
    return file_paths

def select_folder():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    folder_path = filedialog.askdirectory(title="Select Folder with Images")
    root.destroy()
    return folder_path
'''