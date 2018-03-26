import os
import copy
from PyPDF2 import PdfFileReader, PdfFileWriter

path = r"/Users/staniya/Downloads/book1-exercises-master/_old/Course-materials-Python3/Chapter 12/practice_files"

input_file_name = os.path.join(path, "ugly.pdf")
input_file = PdfFileReader(open(input_file_name, "rb"))

output_PDF = PdfFileWriter()

for page_num in range(0, input_file.getNumPages()):
    page = input_file.getPage(page_num)
    if page_num % 2 == 0:
        page.rotateClockwise(90)
    output_PDF.addPage(page)

output_file_name = os.path.join(path, "The Conformed Duckling.pdf")
output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()

from PyPDF2 import PdfFileReader

path = r"/Users/staniya/Downloads/book1-exercises-master/_old/Course-materials-Python3/Chapter 12/practice_files"

input_file_name = os.path.join(path, "half and half.pdf")
input_file = PdfFileReader(open(input_file_name, "rb"))
output_PDF = PdfFileWriter()

page = input_file.getPage(0)
print(page.mediaBox)

for page_num in range(0, input_file.getNumPages()):
    page_left = input_file.getPage(page_num)
    page_right = copy.copy(page_left)
    upper_right = page_left.mediaBox.upperRight #get originial page corner
    #crop and add left-side page
    page_left.mediaBox.upperRight = (upper_right[0]/2, upper_right[1])
    output_PDF.addPage(page_left)
    #crop and add right-side page
    page_right.mediaBox.upperLeft = (upper_right[0]/2, upper_right[1])
    output_PDF.addPage(page_right)

output_file_name = os.path.join(path, "The Little Mermaid.pdf")
output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()


input_file_name = os.path.join(path, "The Emperor.pdf")
input_file = PdfFileReader(open(input_file_name, "rb"))
output_PDF = PdfFileWriter()

watermark_file_name = os.path.join(path, "top secret.pdf")
watermark_file = PdfFileReader(open(watermark_file_name, "rb"))

for page_num in range(0, input_file.getNumPages()):
    page = input_file.getPage(page_num)
    page.mergePage(watermark_file.getPage(0)) #add watermark image
    output_PDF.addPage(page)

output_PDF.encrypt("good2Bkind") #add password to the PDF file
output_file_name = os.path.join(path, "New Suit.pdf")
output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()



