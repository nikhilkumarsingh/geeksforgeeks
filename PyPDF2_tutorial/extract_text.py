# importing required modules
import PyPDF2

# creating a pdf File object
pdfFileObj = open('example.pdf', 'rb')

# creating a pdf Reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()
