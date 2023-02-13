from fpdf import FPDF

pdf=FPDF(orientation='P',unit='mm',format='A4')
# print(type(pdf))

pdf.add_page()

pdf.set_font(family='Times',style='B',size=12) ## set font for codes below!!!
pdf.cell(w=0,h=12,txt='Hello there!',align='L',ln=1,border=1) ## cell w=0 to expand!!!
pdf.cell(w=20,h=12,txt='Hello there!',align='L',ln=1,border=1)
pdf.cell(w=10,h=12,txt='Hello there!',align='L',ln=0,border=1) ## line break!!!
pdf.cell(w=10,h=12,txt='Hello there!',align='L',ln=1,border=0)
pdf.cell(w=0,h=24,txt='Hello there!',align='L',ln=1,border=1) ## height keep same as font!!
pdf.cell(w=0,h=12,txt='Hi there!',align='R',ln=1,border=1)

pdf.set_font(family='Times',style='B',size=10)
pdf.cell(w=0,h=12,txt='Hi there!',align='L',ln=1,border=1)

pdf.output('out.pdf')