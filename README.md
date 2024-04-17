# PDF Merger

This Python script monitors an input folder for PDF files. When two or more PDF files are found, it merges them into a single PDF file and saves it to the output folder. 

## Requirements

- Python 3.x
- PyPDF2 library


## Create virtual environment
1. create venv
```
python -m venv myvenv
```

2. activate the venv for python 3.10.11
```
myvenv\bin\activate
```
3. to deactivate 
```
deactivate
```

4. you can use the extension - Python Environment Manager. 
```
https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-environment-manager
```
## Installation

1. Clone or download this repository to your local machine.
2. Install the required dependencies using pip:

```
pip install PyPDF2
```

## Usage

1. Place your PDF files in the input folder.
2. Run the `main.py` script:

```
python main.py
```

3. The script will continuously monitor the input folder for PDF files. When two or more PDF files are found, it will merge them into a single PDF file and save it to the output folder.

## Folder Structure

- `input_folder`: Place your PDF files here.
- `merged_pdf`: Merged PDF files will be saved here.


