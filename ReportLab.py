import os
import csv
from reportlab.pdfgen import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reporlab.platypus import Table

xmargin = 3.2 * inch
ymargin = 6 * inch

my_path = "/Users/staniya/Downloads/book1-exercises-master/chp09/practice_files"

with open(os.path.join(my_path, "pastimes.csv"), "r") as my_input, open(os.path.join(my_path, "categorized pastimes.csv"), "w") as my_output:
    my_file_reader = csv.reader(my_input)
    my_file_writer = csv.writer(my_output)

    next(my_file_reader)
    my_file_writer.writerow(["Name", "Favorite Pastime", "Type of Pastime"])

    for row in my_file_reader:
        if row[1].find("fighting") != False:
            row.append("Combat")
        else:
            row.append("Other")

        my_file_writer.writerow(row)
        print(row)

with open(os.path.join(my_path, "categorized_pastimes.csv"), "r") as my_csv_input:
    data_reader = csv.reader(my_csv_input)
    c = canvas.Canvas("reportLab test.pdf", pagesize=letter)
    c.setFont('Helvetica', 12)
    t = Table(data_reader)
    t.setStyle([("TEXTCOLOR", colors.blue)])
    t.wrapOn(c, xmargin, ymargin)
    t.drawOn(c, xmargin, ymargin)
    c.save()
