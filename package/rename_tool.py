"""This script renames files in the specified directory."""

import os
import re


def rename_files():
    """Helper function to rename files in the specified directory."""

    folder = "./01-Easy"  # adjust as needed

    for filename in os.listdir(folder):
        match = re.match(r"(\d+)-(.*)", filename)

        if match:
            old_number, rest = match.groups()
            new_number = old_number.zfill(5)  # Pad with zeros to make it 5 digits
            new_filename = f"{new_number}-{rest}"

            # Only rename if the filename actually changes
            if filename != new_filename:
                old_path = os.path.join(folder, filename)
                new_path = os.path.join(folder, new_filename)
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")


if __name__ == "__main__":
    rename_files()
    print("All files have been renamed.")
