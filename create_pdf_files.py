from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Table

xmargin = 3.2 * inch
ymargin = 6 * inch

  
c = canvas.Canvas("hello.pdf")
#c.drawString(100, 100, "Hello World")
c.drawString(250, 500, "Hello World") #text is now closer to being centered
c.save()

c2 = canvas.Canvas("hello_again.pdf", pagesize=letter)
c2.setLineWidth(1)
c2.drawString(xmargin, ymargin, "Hello World from Report Lab!")
c2.save()

xmargin = 3.2 * inch
ymargin = 6 * inch

c3 = canvas.Canvas("tps_report.pdf", pagesize=letter)
c3.setFont('Helvetica', 12)

data = [['#1', '#2', '#3', '#4', '#5'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34'],
        ['20', '21', '22', '23', '24'],
        ['20', '21', '22', '23', '24'],
        ['20', '21', '22', '23', '24'],
        ['20', '21', '22', '23', '24']]

t = Table(data)
t.setStyle([('TEXTCOLOR', (0,0), (4,0), colors.red)])
t.wrapOn(c3, xmargin, ymargin)
t.drawOn(c3, xmargin, ymargin)
c3.save() 
