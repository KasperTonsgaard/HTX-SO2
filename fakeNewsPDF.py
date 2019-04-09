import fakeNewsGenerator as fng
from fpdf import FPDF
import random

def GeneratePDF():
    pdf = FPDF('P', 'mm', (594, 8250))
    pdf.add_page()
    pdf.set_font("Arial", size=20, style="B")
    for x in range(0, 25):
        for y in range (0, 12):
            pdf.cell(200, 10, txt=str((fng.GenerateFakeArticles(y, 0))), ln=1, align="L")
    pdf.output("pdf/Fake News.pdf")