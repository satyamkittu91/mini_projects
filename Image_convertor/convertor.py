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
    def convert_image(i_name, o_name, image_format):
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

        if isinstance(self.input_tuple, (str, Path)):
            raw_values = [self.input_tuple]
        elif isinstance(self.input_tuple, (tuple, list, set)):
            raw_values = self.input_tuple
        else:
            return []

        files: list[Path] = []

        for item in raw_values:
            path = Path(item)
            if path.is_dir():
                files.extend(sorted(child for child in path.iterdir() if child.is_file()))
            elif path.is_file():
                files.append(path)

        return files

    def convert(self):
        for file in self._collect_files():
            if self.check_format(file) is None:
                print(f"Invalid File: {file}")
                continue

            output_path = Path(self.destination, file.name)
            output_path = output_path.with_suffix(config["Conversion"].get(self.conversion, ".png"))
            self.convert_image(file, output_path, self.conversion)

        return


    