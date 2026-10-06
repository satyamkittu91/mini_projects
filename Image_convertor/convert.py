from PIL import Image
from pillow_heif import register_heif_opener
from pathlib import Path

register_heif_opener()

def convert_heic_to_tiff(input_file_or_path, output_file_or_path, lossless = False):
    path = Path(input_file_or_path)
    if path.is_file():
        with Image.open(path) as img:
            img.save(output_file_or_path, format='TIFF', lossless=lossless)
            