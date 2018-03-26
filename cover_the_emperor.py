import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import copy

path = r"/Users/staniya/Downloads/book1-exercises-master/_old/Course-materials-Python3/Chapter 12/practice_files"

input_file_name = os.path.join(path, "The Emperor.pdf")
input_file = PdfFileReader(open(input_file_name, "rb"))
output_PDF = PdfFileWriter()
cover_page_name = os.path.join(path, "Emperor cover sheet.pdf")
cover_page = PdfFileReader(open(cover_page_name, "rb"))

for page_num in range(0, cover_page.getNumPages()):
    pages = cover_page.getPage(page_num)
    output_PDF.addPage(pages)

for page_num in range(0, input_file.getNumPages()):
    pages = input_file.getPage(page_num)
    output_PDF.addPage(pages)
    
output_file_name = os.path.join(path, "The Covered Emperor.pdf")
output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()
                           
