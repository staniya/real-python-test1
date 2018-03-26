from easygui import *
from PyPDF2 import PdfFileReader, PdfFileWriter
from numpy.core.defchararray import isdigit

input_file_name = fileopenbox("Please choose a file", "Select File", "*.pdf")
if input_file_name is None:
    exit()

beginning_page = int(enterbox("Choose beginning page", "Page Start", ""))
ending_page = int(enterbox("Choose ending page", "Page End", ""))
#
# check_digit = isdigit(beginning_page)
# check_digit2 = isdigit(ending_page)
#
# if check_digit or check_digit2 == False:
#     print("false")

input_file = PdfFileReader(open(input_file_name, "rb"))
output_PDF = PdfFileWriter()

while beginning_page < 0 or ending_page > input_file.getNumPages() or \
        beginning_page == ending_page or beginning_page > ending_page:
    message = msgbox("To continue press OK", "You entered an invalid beginning page or ending page", "OK")
    if message == "OK":
        beginning_page = int(enterbox("Choose beginning page", "Page Start", ""))
        ending_page = int(enterbox("Choose ending page", "Page End", ""))
    else:
        exit()

output_file_name = filesavebox("", "Save the rotated PDF as...", "*.pdf")

for page_num in range(beginning_page, ending_page):
    page = input_file.getPage(page_num)
    output_PDF.addPage(page)

output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()




