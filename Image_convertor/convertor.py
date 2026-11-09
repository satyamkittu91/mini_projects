from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from PIL import Image, UnidentifiedImageError
from pillow_heif import register_heif_opener

register_heif_opener()

CONFIG_PATH = Path(__file__).resolve().with_name("config.json")

if not CONFIG_PATH.exists():
    raise FileNotFoundError(f"Configuration file not found: {CONFIG_PATH}")

with CONFIG_PATH.open("r", encoding="utf-8") as config_file:
    config = json.load(config_file)


class Picture:
    def __init__(self, input_tuple, destination_folder, conversion_to: str):
        self.input_tuple = input_tuple
        self.destination = Path(destination_folder).expanduser()
        self.destination.mkdir(parents=True, exist_ok=True)

        supported_formats = config.get("Formats", {})
        normalized_target = str(conversion_to).strip().lower().lstrip(".")
        self.conversion = supported_formats.get(normalized_target)

        if self.conversion is None:
            raise ValueError(f"Unsupported conversion format: {conversion_to}")

    @staticmethod
    def check_format(file) -> str | None:
        path = Path(file)
        return config.get("Formats", {}).get(path.suffix.lower().lstrip("."))

    @staticmethod
    def convert_image(image_tuple : dict) -> Path | None:
        i_name = image_tuple["in"]
        o_name = image_tuple["out"]
        image_format = image_tuple["format"]
        options = {
            "JPEG": {"quality": 100},
            "TIFF": {"compression": "tiff_lzw"},
            "PNG": {},
            "HEIC": {"quality": 100},
            "BMP": {},
            "GIF": {},
            "WEBP": {},
        }

        format_name = str(image_format).upper()
        save_options = options.get(format_name)

        if save_options is None:
            print(f"Unsupported format: {image_format}")
            return None

        output_path = Path(o_name)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with Image.open(i_name) as img:
                exif_data = img.info.get("exif")
                save_kwargs = {"format": format_name}

                if exif_data:
                    save_kwargs["exif"] = exif_data

                save_kwargs.update(save_options)
                img.save(output_path, **save_kwargs)
                print(f"{output_path} Saved!!")
                return output_path

        except (UnidentifiedImageError, OSError, SyntaxError, ValueError) as exc:
            print(f"An error occured: {exc}")
            return None

    def _collect_files(self) -> list[Path]:
        raw_values: Iterable[str | Path]
        files: list[tuple[Path, Path, str]] = []

        if isinstance(self.input_tuple, (str, Path)):
            path = Path(self.input_tuple)
            if path.is_dir(): # Extra check
                path_list = (sorted(child for child in path.iterdir() if child.is_file()))
                for item in path_list:
                    item = Path(item)
                    if self.check_format(item) is not None:
                        output_path = Path(self.destination, item.name)
                        output_path = output_path.with_suffix(config["Conversion"].get(self.conversion))
                        files.append({"in": item, "out": output_path, "format": self.conversion})
                    else:
                        print(f'Invalid File! {item}')

        elif isinstance(self.input_tuple, (tuple, list, set)):
            for item in self.input_tuple:
                item = Path(item)
                if item.is_file(): # Extra check
                    if self.check_format(item) is not None:
                        output_path = Path(self.destination, item.name).with_suffix(config["Conversion"].get(self.conversion))
                        files.append({"in": item, "out": output_path, "format": self.conversion})
                    else:
                        print(f'Invalid File! {item}')
        else:
            return []

        return files

    def convert(self):
        for file in self._collect_files():
            self.convert_image(file)
        return
    