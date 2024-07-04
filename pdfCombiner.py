import PyPDF2
import sys

pdfInput = sys.argv[1:]

def pdfCombiner(pdfList):
    merger = PyPDF2.PdfMerger()
    for pdf in pdfList:
        # print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')
    
# PDF combiner ko use karne ke liye python ./pdfCombiner.py file1, file2, file3....
pdfCombiner(pdfInput)



# Basics of PyPDF2

# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfReader(file)
#     page = reader.pages[0]
#     text = page.extract_text()
#     print(text)
# --------------------------------------
# reader = PdfReader("dummy.pdf")
# number_of_pages = len(reader.pages)
# page = reader.pages[0]
# text = page.extract_text()
