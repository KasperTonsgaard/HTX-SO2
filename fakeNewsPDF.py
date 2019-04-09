import fakeNewsGenerator as fng
from fpdf import FPDF
import random

def GeneratePDF():
    pdf = FPDF('P', 'mm', (594, 3550))
    pdf.add_page()
    pdf.set_font("Arial", size=20, style="B")
    for x in range(0, 25):
        articles = fng.GenerateFakeArticles()
        for y in range (0, len(articles)):
            pdf.cell(200, 10, txt=str(articles[y][0]), ln=1, align="L")
    pdf.output("pdf/Fake News.pdf")
