# main.py

from monitor_input_folder import monitor_input_folder
from folder_utils import create_folder_if_not_exists, delete_folders
import os

if __name__ == "__main__":
    input_folder = "input_pdf"
    output_folder = "merged_pdf"
    
    # Delete both folders before starting the monitoring
    delete_folders(input_folder, output_folder)
    
    # Create input_pdf and merged_pdf folders if they don't exist
    create_folder_if_not_exists(input_folder)
    create_folder_if_not_exists(output_folder)

    # Create .gitkeep files in both folders
    with open(os.path.join(input_folder, ".gitkeep"), "w") as f:
        pass

    with open(os.path.join(output_folder, ".gitkeep"), "w") as f:
        pass
    
    # Start monitoring the input folder
    monitor_input_folder(input_folder, output_folder)