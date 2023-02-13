from fpdf import FPDF
import pandas as pd
##commit: Initial commit Sec24
pdf=FPDF(orientation='P',unit='mm',format='A4')
# print(type(pdf))

def create_page():
    pdf.add_page()  
    pdf.set_font(family='Times',style='B',size=12) ## set font for codes below!!!
    # pdf.cell(w=0,h=12,txt='Hello there!',align='L',ln=1,border=1) ## cell w=0 to expand!!!
    pdf.cell(w=0,h=12,txt='Hello there!',align='L',ln=1)
    pdf.set_font(family='Times',size=10)
    pdf.cell(w=0,h=12,txt='Hi there!',align='L',ln=1,border=0)

df=pd.read_csv('topics.csv')
for index,row in df.iterrows():
    # print(index,row)
    # print(index,row['Topic'])
    pdf.add_page()  
    pdf.set_font(family='Times',style='B',size=24)
    pdf.set_text_color(100,100,100)
    # pdf.set_text_color(254,0,0)
    pdf.cell(w=0,h=12,txt=row['Topic'],align='L',ln=1)
    pdf.line(10,22,200,22)

pdf.output('out.pdf')