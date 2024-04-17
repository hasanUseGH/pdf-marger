import os
import time
from merge_pdfs import merge_pdfs

def monitor_input_folder(input_folder, output_folder):
    while True:
        files = [file for file in os.listdir(input_folder) if file.endswith(".pdf")]
        if len(files) >= 2:
            sorted_files = sorted(files, key=lambda x: int(x.split(".")[0])) if all(file.split(".")[0].isdigit() for file in files) else files
            if sorted_files != files:
                print("\n Sorted filenames numerically:\n ")
                for file_name in sorted_files:
                    print(file_name)
                print('\n')
            else:
                print("\n File names are not numerical. Proceeding with the original order.\n ")

            merged_file_path = merge_pdfs([os.path.join(input_folder, file) for file in sorted_files], output_folder)
            print(f"Merged {len(files)} PDF files into {merged_file_path}")

            for file in sorted_files:
                os.remove(os.path.join(input_folder, file))
        time.sleep(5)