import os
from pathlib import Path
s2 = r"C:\\Project\\inputforimageconvertor\\output"
s1 = r"C:\\Project\\inputforimageconvertor\\IMG_1922.HEIC"

s1 = Path(s1)
s2 = Path(s2)

s3 = os.path.join(s2, s1.stem)
print(s3 + ".jpeg")