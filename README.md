# ht-papers

## Install
pip install -e .
pip install -r requirements.txt

## Usage

First search for PDFs on google scholar. These are saved to ```src/data/pdfs.txt```.
```
python src/save_google_scholar_pdf_links.py
```

Then download these and parse the text from the PDFs.
```
python src/download_and_parse_pdf.py
```