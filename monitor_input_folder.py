# monitor_input_folder.py

import os
import time
from merge_pdfs import merge_pdfs


def sort_filenames(files):
    # Try sorting numerically, fallback to lexicographical sorting
    try:
        sorted_files = sorted(files, key=lambda x: int(x.split(".")[0]))
        print("Sorted filenames numerically.")
    except ValueError:
        sorted_files = sorted(files)
        print("Sorted filenames lexicographically.")
    return sorted_files

def monitor_input_folder(input_folder, output_folder):
    while True:
        files = [file for file in os.listdir(input_folder) if file.endswith(".pdf")]
        if len(files) >= 2:
            sorted_files = sort_filenames(files)
            merged_file_path = merge_pdfs([os.path.join(input_folder, file) for file in sorted_files], output_folder)
            print(f"Merged {len(files)} PDF files into {merged_file_path}")
            for file in sorted_files:
                os.remove(os.path.join(input_folder, file))
        time.sleep(5)