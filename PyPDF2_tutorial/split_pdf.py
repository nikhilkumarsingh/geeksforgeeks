# importing the required modules
import PyPDF2

def PDFsplit(pdf, splits):
    # creating input pdf file object
    pdfFileObj = open(pdf, 'rb')
    # creating pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    # starting index of first slice
    start = 0
    # starting index of last slice
    end = splits[0]
    
    
    for i in range(len(splits)+1):
        # creating pdf writer object for (i+1)th split
        pdfWriter = PyPDF2.PdfFileWriter()
        
        # output pdf file name
        outputpdf = pdf.split('.pdf')[0] + str(i) + '.pdf'
        
        # adding pages to pdf writer object
        for page in range(start,end):
            pdfWriter.addPage(pdfReader.getPage(page))
        
        # writing split pdf pages to pdf file
        with open(outputpdf, "wb") as f:
            pdfWriter.write(f)

        # interchanging page split start position for next split
        start = end
        try:
            # setting split end positon for next split
            end = splits[i+1]
        except IndexError:
            # setting split end position for last split
            end = pdfReader.numPages
        
    # closing the input pdf file object
    pdfFileObj.close()
            
def main():
    # pdf file to split
    pdf = 'example.pdf'
    # split page positions
    splits = [2,4]
    # calling PDFsplit function to split pdf
    PDFsplit(pdf, splits)

if __name__ == "__main__":
    # calling the main function
    main()
