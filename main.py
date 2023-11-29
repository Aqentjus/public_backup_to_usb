#aqentjus 2023
import os
import shutil
#import sys

def copy_folders(source_path, destination_path):
    try:
        # If the destination folder already exists, delete it to ensure a fresh copy
        if os.path.exists(destination_path):
            shutil.rmtree(destination_path)
        shutil.copytree(source_path, destination_path)
        print(f"Successfully copied {source_path} to {destination_path}")
    except Exception as e:
        print(f"Error copying {source_path}: {str(e)}")

def main():
    # Path to the text file containing folder paths
    file_path = 'folder_paths.txt'

    # Read folder paths from the text file
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()

    # Ensure that there is at least one line in the file
    if not lines:
        print("Error: Empty file")
        return

    # The first line is the USB drive path
    usb_drive_path = lines[0]

    # Check if the USB drive is accessible
    if not os.path.exists(usb_drive_path):
        print(f"Error: USB drive not found at {usb_drive_path}")
        return

    print(f"Destination USB drive path: {usb_drive_path}")

    # Loop through each remaining line in the file and copy the folders
    for folder_path in lines[1:]:
        source_path = folder_path
        destination_path = os.path.join(usb_drive_path, os.path.basename(folder_path))

        print(f"\nCopying {source_path} to {destination_path}")
        copy_folders(source_path, destination_path)

if __name__ == "__main__":
    main()
    #sys.exit()
