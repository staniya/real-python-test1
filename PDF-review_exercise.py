import os
from PyPDF2 import PdfFileReader, PdfFileWriter

path = r"/Users/staniya/Downloads/book1-exercises-master/_old/Course-materials-Python3/Chapter 12/practice_files"

input_file_name = os.path.join(path, "The Whistling Gypsy.pdf")
input_file = PdfFileReader(open(input_file_name, "rb"))

print("The title is: ", input_file.getDocumentInfo().title)
print("The author is: ", input_file.getDocumentInfo().author)
print("The total number of pages in the file is: ", input_file.getNumPages())

output_file_name = os.path.join(path, "The Whistling Gypsy.txt")
output_file = open(output_file_name, "wb")
total_pages = input_file.getNumPages()

for content in range(0, total_pages):
    text = input_file.getPage(content).extractText()
    text = text.replace(" ", "\n")
    text = text.encode("utf-8") #I need to change it to this format
    output_file.write(text)
    
output_file.close()

print(output_file)

output_PDF = PdfFileWriter()
for content in range(1, total_pages):
    text = output_PDF.addPage(input_file.getPage(content))

output_file_name2 = os.path.join(path, "The Whistling Gypsy 2.pdf")#Output
output_file2 = open(output_file_name2, "wb")
output_PDF.write(output_file2)
output_file2.close()
