# folder_utils.py

import os
import shutil

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
       

def delete_folders(input_folder, output_folder):
    if os.path.exists(input_folder):
        shutil.rmtree(input_folder)
        print(f"cleaning input folder: {input_folder}")
    
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
        print(f"cleaning output folder: {output_folder}")