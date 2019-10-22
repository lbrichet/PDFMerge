import os, sys,io
from PyPDF2 import PdfFileReader, PdfFileMerger
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

pdffile = PdfFileReader('testbookmark.pdf')
outlines = pdffile.outlines
table_of_content=""

# Create Text File
f = open("bookmark.txt","w+")
for x in outlines:
    f.write('{:.<90} {:d}'.format(x.get("/Title"),x.get("/Page"))+'\n')
f.close()

# Create PDF File
style = ParagraphStyle(
        name='Normal',
        fontName='Courier',
        fontSize=8,
        )
story = []

pdf_name = 'bookmark.pdf'
doc = SimpleDocTemplate(
    pdf_name,
    pagesize=letter,
    bottomMargin=.4 * inch,
    topMargin=.6 * inch,
    rightMargin=.8 * inch,
    leftMargin=.8 * inch
    )

with open("bookmark.txt", "r") as txt_file:
    text_content = txt_file.read()

P = Paragraph(text_content, style)
story.append(P)

doc.build(
    story,
)

# Merge TOC and Merged PDF
pdfMerger = PdfFileMerger()
pdfMerger.merge(0,'bookmark.pdf',import_bookmarks=False)
pdfMerger.append(PdfFileReader('testbookmark.pdf'))
pdfMerger.write('testbookmark.pdf')
pdfMerger.close()
