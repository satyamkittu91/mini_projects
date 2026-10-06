from PIL import Image
from pillow_heif import register_heif_opener
from pathlib import Path
import json

register_heif_opener()
with open('C:\\Programming\\Mini_Projects\\mini_projects\\Image_convertor\\config.json') as config_file:
    config = json.load(config_file)

class Image:
    def __init__(self, input_file_or_path, output_file_or_path):
        self.file = Path(input_file_or_path)
        self.output_path = Path(output_file_or_path)

    def check_format(self):
        return config.get(self.file.suffix.lower())

    def convert_to_tiff(self):
        if self.file.is_file():
            with Image.open(self.file) as img:
                exif_data = img.info.get('exif')
                img.save(self.output_path, format='TIFF', compression = "tiff_lzw", exif = exif_data)

    def convert_to_jpeg(self, lossless=False):
        with Image.open(self.file) as img:
            exif_data = img.info.get('exif')
            if lossless:
                img.save(self.output_path, format='JPEG', quality=100, exif = exif_data)
            else:
                img.save(self.output_path, format='JPEG', quality=85)

    def convert_to_png(self):
        with Image.open(self.file) as img:
            exif_data = img.info.get('exif')
            img.save(self.output_path, format='PNG', exif = exif_data)

    def convert_to_heic(self):
        with Image.open(self.file) as img:
            exif_data = img.info.get('exif')
            img.save(self.output_path, format='HEIC', quality=100, exif = exif_data)