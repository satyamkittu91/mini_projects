from PIL import Image, UnidentifiedImageError
from pillow_heif import register_heif_opener
from pathlib import Path
import json
import os

register_heif_opener()
with open('C:\\Programming\\Mini_Projects\\mini_projects\\Image_convertor\\config.json') as config_file:
    config = json.load(config_file)

class Picture:

    def __init__(self, input_tuple : tuple[os.PathLike[str]], destination_folder : os.PathLike[str], conversion_to : str):
        self.input_tuple = input_tuple
        self.destination = destination_folder
        self.conversion = config["Formats"].get(str(conversion_to).lower().lstrip('.'))
        

        # checking if the conversion format is valid
        if self.conversion == None:
            raise ValueError(f"Unsupported conversion format: {conversion_to}")


    @staticmethod
    def check_format(file) -> str | None:
        path = Path(file)
        return config["Formats"].get(path.suffix.lower().lstrip('.'))

    @staticmethod
    def convert_image(i_name, o_name, format):
        options = {
            'JPEG': {'quality': 100},
            'TIFF': {'compression' : 'tiff_lzw'},
            'PNG' : {},
            'HEIC' : {'quality': 100}
        }

        save_options = options[format]

        try:
            with Image.open(i_name) as img:
                exif_data = img.info.get('exif')
                img.save(o_name, format=format, exif=exif_data, **save_options)
                print(f'{o_name} Saved!!')
                return

        except (UnidentifiedImageError, OSError, SyntaxError) as e:
            print(f"An error occured: {e}")
    '''
    @staticmethod
    def convert_image(i_name, o_name, format):

        if format == 'JPEG':
            with Image.open(i_name) as img:
                exif_data = img.info.get('exif')
                img.save(o_name, format=format, quality=100, exif=exif_data)
                print(f"{o_name} Saved!!")
                return

        elif format == 'TIFF':
            with Image.open(i_name) as img:
                exif_data = img.info.get('exif')
                img.save(o_name, format=format, compression='tiff_lzw', exif=exif_data)
                print(f"{o_name} Saved!!")

        elif format == 'PNG':
            with Image.open(i_name) as img:
                exif_data = img.info.get('exif')
                img.save(o_name, format=format, exif=exif_data)
                print(f"{o_name} Saved!!")

        elif format == 'HEIC':
            with Image.open(i_name) as img:
                exif_data = img.info.get('exif')
                img.save(o_name, format=format, quality = 100, exif=exif_data)
                print(f"{o_name} Saved!!")
    '''

    def convert(self):

        if isinstance(self.input_tuple, tuple):
            for f in self.input_tuple:
                f = Path(f)
                # if f.is_dir():
                #     for file in f.iterdir():
                #         if self.check_format(file) is not None:
                #             o_name = os.path.join(self.destination, file.name)
                #             o_name = Path(o_name).with_suffix(config["Conversion"].get(self.conversion))
                #             self.convert_image(file, o_name,  self.conversion)

                #         else:
                #             print(f"Invalid file: {file}")


                if f.is_file():
                    if self.check_format(file=f) is not None:
                        o_name = os.path.join(self.destination, f.name)
                        o_name = Path(o_name).with_suffix(config["Conversion"].get(self.conversion))
                        self.convert_image(f, o_name, self.conversion)

                    else:
                        print(f"Invalid File: {f}")

        if isinstance(self.input_tuple, Path):
            f = self.input_tuple
            if f.is_file():
                if self.check_format(file=f) is not None:
                    o_name = os.path.join(self.destination, f.name)
                    o_name = Path(o_name).with_suffix(config["Conversion"].get(self.conversion))
                    self.convert_image(f, o_name, self.conversion)

                else:
                    print(f"Invalid File: {f}")

            elif f.is_dir():
                for file in f.iterdir():
                    if self.check_format(file) is not None:
                        o_name = os.path.join(self.destination, file.name)
                        o_name = Path(o_name).with_suffix(config["Conversion"].get(self.conversion))
                        self.convert_image(file, o_name, self.conversion)

                    else:
                        print(f"Invalid File: {file}")
        if f.is_dir():
            for file in f.iterdir():
                if self.check_format(file) is not None:
                    o_name = os.path.join(self.destination, file.name)
                    o_name = Path(o_name).with_suffix(config["conversion"].get(self.converstion))
                    self.convert_image(file, o_name, self.conversion)

        return


    