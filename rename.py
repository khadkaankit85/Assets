import os
import re
from datetime import datetime

# Path to the base folder
base_path = "/home/khadka_angkit/Computer Programming/GithubAssets/Assets"

# Supported image file extensions
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

# Regular expression to extract the date from the file name
date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')

# Function to sort files by the date in their names
def sort_files_by_date(files):
    def get_date_from_name(file_name):
        match = date_pattern.search(file_name)
        if match:
            # Parse the date string into a datetime object
            return datetime.strptime(match.group(), '%Y-%m-%d')
        return datetime.min  # Use a very old date if no date is found

    return sorted(files, key=get_date_from_name)

# Function to rename images in each folder, starting numbering from 1, only if the name is not already a number
def rename_images_if_not_number(base_directory):
    for root, _, files in os.walk(base_directory):
        # Filter files to only include supported image extensions
        image_files = [f for f in files if f.lower().endswith(image_extensions)]

        # Sort the image files by date
        sorted_files = sort_files_by_date(image_files)

        count = 1  # Reset the count for each folder
        for file_name in sorted_files:
            # Check if the file has a supported image extension
            name_without_extension = os.path.splitext(file_name)[0]

            # Rename the file only if the current name is not numeric
            if not name_without_extension.isnumeric():
                # Create the new file name with the sequential number
                new_name = f"{count}{os.path.splitext(file_name)[1]}"
                old_file_path = os.path.join(root, file_name)
                new_file_path = os.path.join(root, new_name)

                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} -> {new_file_path}")
                count += 1
            else:
                print(f"Skipped: {file_name} is already a number")

# Check if the base path exists
if os.path.exists(base_path):
    rename_images_if_not_number(base_path)
    print("Renaming process completed.")
else:
    print(f"Base directory not found: {base_path}")
