import os
from PyPDF2 import PdfFileReader, PdfFileWriter

path = r"/Users/staniya/Downloads/book1-exercises-master/_old/Course-materials-Python3/Chapter 12/practice_files"

input_file_name = os.path.join(path, "Pride and Prejudice.pdf")
input_file = PdfFileReader(open(input_file_name, "rb"))

print(input_file.getDocumentInfo())

print(input_file.getPage(0).extractText())

output_file_name = os.path.join(path, "Pride and Prejudice.txt")
output_file = open(output_file_name, "w")

title = input_file.getDocumentInfo().title #get file title
total_pages = input_file.getNumPages() #get total page count

output_file.write(title +"\n")
output_file.write("Number of pages:{}\n\n".format(total_pages))

for page_num in range(0, total_pages):
    text = input_file.getPage(page_num).extractText()
    text = text.replace(" ", "\n")
    output_file.write(text)

output_file.close()

output_PDF=PdfFilwWriter()
for page_num in range(1, 4):
    output_PDF.addPage(input_file.getPage(page_num))

output_file_name2 = os.path.join(path, "portion.pdf")
output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()





