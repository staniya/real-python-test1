import os
import copy
from PyPDF2 import PdfFileReader, PdfFileWriter

path = r"/Users/staniya/Downloads/book1-exercises-master/_old/Course-materials-Python3/Chapter 12/practice_files"

input_file_name = os.path.join(path, "Walrus.pdf")
input_file = PdfFileReader(open(input_file_name, "rb"))
input_file.decrypt("IamtheWalrus")
output_PDF = PdfFileWriter()

for content in range (0, input_file.getNumPages()):
    page_left = input_file.getPage(content)
    page_left.rotateCounterClockwise(90)

    page_right = copy.copy(page_left)
    upper_right = page_left.mediaBox.upperRight

    page_left.mediaBox.upperRight = (upper_right[0]/2, upper_right[1])
    output_PDF.addPage(page_left)
    
    page_right.mediaBox.upperLeft = (upper_right[0]/2, upper_right[1])
    output_PDF.addPage(page_right)
    
output_file_name = os.path.join(path, "New Walrus.pdf")
with open(output_file_name, "wb") as output_file:
    output_PDF.write(output_file)

