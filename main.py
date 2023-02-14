from fpdf import FPDF
import pandas as pd
##commit: Exercise: Add page lines Sec24
pdf=FPDF(orientation='P',unit='mm',format='A4')
pdf.set_auto_page_break(auto=False,margin=0)
# print(type(pdf))

df=pd.read_csv('topics.csv')
for index,row in df.iterrows():
    # print(index,row)
    # print(index,row['Topic'])
    pdf.add_page()  
    # set header
    pdf.set_font(family='Times',style='B',size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=row['Topic'],align='L',ln=1)
    # pdf.line(10,22,200,22)
    # lines 10mm apart
    for y in range(22,290,10):
        pdf.line(10,y,200,y)
    # set footer
    pdf.ln(265)
    pdf.set_font(family='Times',style='I',size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=0,txt=row['Topic'],align='R')
     # addpages
    for i in range(row['Pages']-1):
        pdf.add_page()
        # lines 10mm apart
        for y in range(22,290,10):
            pdf.line(10,y,200,y)
        # set footer
        pdf.ln(277)
        pdf.set_font(family='Times',style='I',size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=0,txt=row['Topic'],align='R')

pdf.output('tmp/out.pdf')