# Project Assets Repository

**Note**: This is not a personal project repository. 

This repository hosts the assets for my projects, such as images, resumes, and documents that I can use in multiple places.

## rename.py

The `rename.py` script is included in this repository. It performs the following functions:

- **Filename Renaming**: The script renames files based on their creation date, assigning a numeric filename format.
- **Duplicate Handling**: It ensures that the same file will not be renamed twice. This means the URL of an asset will remain consistent even if the script is executed multiple times on the same file.

This structure allows for organized management of project assets without the risk of breaking links or references.

## Usage

To run the `rename.py` script:

1. Ensure you have Python installed on your machine.
2. Navigate to the directory containing the assets.
3. Execute the script by running the following command in your terminal:

   ```bash
   python rename.py
