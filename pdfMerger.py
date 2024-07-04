import PyPDF2

# Okey so the first thing that we need to do is to open both the input and the watermark PDFs and create an wroter object for the output one.
inputPDF = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermarkPDF = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
outputPDF = PyPDF2.PdfWriter()

# Making sure that we select the right page that has the watermark
watermarkPage = watermarkPDF.pages[0]

for i in range(len(inputPDF.pages)):
    # Saare pages ko access karne ke liye:-
    page = inputPDF.pages[i]
    # accessed pages ko watermark wale page se MERGE karwa do:-
    page.merge_page(watermarkPage)
    # output PDF me ek ek kar ke saare pages ko add kar do:-
    outputPDF.add_page(page)
    
# Finally jitne bhi pages aaye h un sabko addedWtrMrkPDF.pdf me write karo:-
with open('addedWtrMrkPDF.pdf', 'wb') as file:
    outputPDF.write(file)