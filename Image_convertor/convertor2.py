from PIL import Image
from pillow_heif import register_heif_opener
from pathlib import Path
import json
import os
import sys

register_heif_opener()
with open('config.json') as config_file:
    config = json.load(config_file)

def check_format(file) -> str | None:
    path = Path(file)
    return config["Formats"].get(path.suffix.lower())



class Picture:
    def __init__(self, input_path : tuple[os.PathLike[str], ...], output_path : os.PathLike[str], conversion_format : str, lossless : bool = False):
        self.f = input_path
        self.files = tuple(Path(p) for p in input_path) if isinstance(input_path, (tuple, list)) else Path(input_path)
        self.output_path = Path(output_path)
        self.conversion = config["Formats"].get(str(conversion_format).lower().lstrip("."))
        self.lossless = lossless
        if self.conversion == None:
            raise ValueError(f"Unsupported conversion format: {conversion_format}")

    
    def convert(self):
        #version 3
        
        
'''
        #version 2
        if isinstance(self.files, tuple):
            for file in self.files:
                Picture(file, self.output_path, self.conversion, self.lossless).convert()
            return


        if self.files.is_dir():
            for file in self.files.iterdir():
                if file.is_file() and check_format(file) is not None:
                    Picture(file, self.output_path, self.conversion, self.lossless)
            return

        if self.files.is_file():
            format_of_the_file = check_format(self.files)
            if format_of_the_file is None:
                return

            extension = config["Conversion"].get(self.conversion, "." + self.conversion.lower())
            output_name = self.output_path / (self.files.stem + extension)

            with Image.open(self.files) as img:
                exif_data = img.info.get('exif')
                if self.lossless and self.conversion == "JPEG":
                    img.save(output_name, format=self.conversion, quality =100, exif=exif_data)
                else:
                    img.save(output_name, format=self.conversion, exif=exif_data)

            return output_name

        return None
'''



'''
        #version 1
        if os.path.isdir(self.f):
            files = []
            for file in os.listdir(self.f):
                if check_format(file) in config["Conversion"]:
                    img = Picture(file, self.output_path, self.conversion, self.lossless)


        if isinstance(self.f, tuple):
            for file in self.f:
                img = Picture(file, self.output_path, self.conversion, self.lossless)

        if os.path.isfile(self.f):
            format_of_the_file = config["Formats"].get((self.f.suffix.lower()).replace('.', ''))
            if format_of_the_file is not None:
                output_name = os.path.join(self.output_path, self.f.name)
                with Image.open(self.f) as img:
                    exif_data = img.info.get('exif')
                    img.save(output_name, format=self.conversion)
'''