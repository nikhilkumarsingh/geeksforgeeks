# importing the required modules
import PyPDF2

def PDFrotate(origFileName, newFileName, rotation):
    # creating a pdf File object of original pdf
    pdfFileObj = open(origFileName, 'rb')
    # creating a pdf Reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # creating a pdf writer object for new pdf
    pdfWriter = PyPDF2.PdfFileWriter()
    # rotating each page
    for page in range(pdfReader.numPages):
        # creating rotated page object
        pageObj = pdfReader.getPage(page)
        pageObj.rotateClockwise(rotation)
        # adding rotated page object to pdf writer
        pdfWriter.addPage(pageObj)

    # new pdf file object
    newFile = open(newFileName, 'wb')
    
    # writing rotated pages to new file
    pdfWriter.write(newFile)

    # closing the original pdf file object
    pdfFileObj.close()
    # closing the new pdf file object
    newFile.close()
    

def main():
    # original pdf file name
    origFileName = 'example.pdf'
    # new pdf file name
    newFileName = 'rotated_example.pdf'
    # rotation angle
    rotation = 270
    
    # calling the PDFrotate function
    PDFrotate(origFileName, newFileName, rotation)
    
    

if __name__ == "__main__":
    # calling the main function
    main()
    
