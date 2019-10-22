#! python3
# Merge all .pdf files in the current directory

import os, sys
from PyPDF2 import PdfFileReader, PdfFileMerger
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Get output filename from arguments
if len(sys.argv) <= 1:
    print('Missing Argument : pdfmerge.py [OutputFile.pdf]')
    exit(1)
if sys.argv[1][-4:] != '.pdf':
    print('Output file extension must be .pdf')
    exit(1)

OutputFile = sys.argv[1]

# Remove Merged file if exists
if os.path.exists(OutputFile):
    os.remove(OutputFile)

# Get all the .pdf files in current directory
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key = str.casefold)
pdfMerger = PdfFileMerger()

# Loop through all the pdf files
for filename in pdfFiles:
    pdfMerger.append(filename, import_bookmarks=False,bookmark=str(filename))

pdfMerger.write(OutputFile)

# Read newly created PDF to extract bookmarks
pdffile = PdfFileReader(OutputFile)
outlines = pdffile.outlines

# # Create Text File for fun
# f = open('bookmarks.txt',"w+")
# for x in outlines:
#     f.write('{:.<60} {:d}'.format(x.get("/Title"),x.get("/Page")+2)+'\n')
# f.close()

# Create PDF File
style = ParagraphStyle(
        name='Normal',
        fontName='Courier',
        fontSize=10,
        )
story = []

pdf_name = 'bookmarks.pdf'
doc = SimpleDocTemplate(
    pdf_name,
    pagesize=letter,
    bottomMargin=.4 * inch,
    topMargin=.6 * inch,
    rightMargin=.8 * inch,
    leftMargin=.8 * inch
    )

text_content = ""

for x in outlines:
    text_content += '{:.<70} {:d}'.format(x.get("/Title"),x.get("/Page")+2)
    text_content += '<br/>'
                    

P = Paragraph(text_content, style)
story.append(P)

doc.build(
    story,
)

# Merge TOC and Merged PDF
pdfMerger = PdfFileMerger()
pdfMerger.merge(0,'bookmarks.pdf',import_bookmarks=False)
pdfMerger.append(PdfFileReader(OutputFile))
pdfMerger.write(OutputFile)
pdfMerger.close()

# Remove bookmarks.pdf file if exists
if os.path.exists('bookmarks.pdf'):
    os.remove('bookmarks.pdf')

# Open PDF file
os.startfile(OutputFile)