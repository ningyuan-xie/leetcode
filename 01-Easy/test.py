import os
import re

folder = "./01-Easy"  # or the full path to your folder

for filename in os.listdir(folder):
    match = re.match(r"(\d+)-(.*)", filename)
    if match:
        old_number, rest = match.groups()
        new_number = old_number.zfill(5)
        new_filename = f"{new_number}-{rest}"
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_filename)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")
