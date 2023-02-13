from fpdf import FPDF
import pandas as pd
##commit: Add more pages for each topic Sec24
pdf=FPDF(orientation='P',unit='mm',format='A4')
# print(type(pdf))

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
    
    for i in range(row['Pages']-1):
        pdf.add_page()

pdf.output('tmp/out.pdf')