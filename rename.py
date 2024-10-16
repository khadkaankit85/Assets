import os

# Path to the base folder
base_path = "/home/khadka_angkit/Computer Programming/GithubAssets/Assets"

# Supported image file extensions
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

# Function to rename images in each folder, starting numbering from 1, only if the name is not already a number
def rename_images_if_not_number(base_directory):
    for root, _, files in os.walk(base_directory):
        count = 1  # Reset the count for each folder
        for file_name in files:
            # Check if the file has a supported image extension
            if file_name.lower().endswith(image_extensions):
                # Extract the file name without extension
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
