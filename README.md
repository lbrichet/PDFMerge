# PDFMerge

Really simple PDF merger in Python.
Merge all pdf files in a directory and create one big pdf file with a Table of Content with file names as first page.

**Usage:**
* Executable :
  * [Download Linux Binary](https://github.com/tibuski/PDFMerge/blob/master/pdfmerge.bin)
  * Run 
    ```sh
    ./pdfmerge.bin "OutputFile.pdf" ["Paperless Tag Between Quotes"]
    ```


* Python :
  ```sh
  git clone https://github.com/tibuski/PDFMerge
  cd PDFMerge
  python3 -m venv .
  source bin/activate
  python3 -m pip install -r requirments.txt
  python3 ./pdfmerge.py "OutputFile.pdf" ["Paperless Tag Between Quotes"]
  ```
