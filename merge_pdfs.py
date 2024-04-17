# merge_pdfs.py

import os
from PyPDF2 import PdfMerger

def merge_pdfs(files, output_folder):
    merger = PdfMerger()
    for file in files:
        merger.append(file)
    merged_file_path = os.path.join(output_folder, "merged_file.pdf")
    merger.write(merged_file_path)
    merger.close()
    return merged_file_path