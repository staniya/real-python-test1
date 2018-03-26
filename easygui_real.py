from PyPDF2 import PdfFileReader, PdfFileWriter
from easygui import *

# let the user choose and input file

input_file_name = fileopenbox("", "Select a PDF to rotate...", "*.pdf")
if input_file_name is None:  # exit on "Cancel"
    exit()

# let the user choose an amount of rotation
rotate_choices = [90, 180, 270]
message = "Rotate the PDF clockwise by how many degrees?"
degrees = choicebox(message, "Choose rotation...", rotate_choices)

# let the user choose an output file
output_file_name = filesavebox(" ", "Save the rotated PDF as...", "*.pdf")
while input_file_name == output_file_name:  # cannot use same file as innput
    msgbox("Cannot overwrite original file!", "Please choose another file...")
    output_file_name = filesavebox("", "Save the rotated PDF as...", "*.pdf")

if output_file_name is None:
    exit()  # exit on "Cancel"

#read in file, perform rotation and save out new file
input_file = PdfFileReader(open(input_file_name, "rb"))
output_PDF = PdfFileWriter()

for page_num in range(0, input_file.getNumPages()):
    page = input_file.getPage(page_num)
    page = page.rotateClockwise(int(degrees))
    output_PDF.addPage(page)

output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()
