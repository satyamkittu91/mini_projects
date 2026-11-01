import os
from pathlib import Path
import mini_projects.Image_convertor.convertor as convertor
s2 = r"C:\\Project\\inputforimageconvertor\\output"
s1 = r"C:\\Project\\inputforimageconvertor"

s1 = Path(s1)
s2 = Path(s2)

s1 = (s1,)

convertor.Picture(s1, s2, 'jpeg').convert()