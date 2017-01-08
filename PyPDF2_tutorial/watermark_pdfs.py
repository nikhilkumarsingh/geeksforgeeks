# importing the required modules
import PyPDF2

def add_watermark(wmFile, pageObj):
    # opening watermark pdf file
    wmFileObj = open(wmFile, 'rb')
    # creating pdf reader object of watermark pdf file
    pdfReader = PyPDF2.PdfFileReader(wmFileObj) 
    # merging watermark pdf's first page with passed page object.
    pageObj.mergePage(pdfReader.getPage(0))
    # closing the watermark pdf file object
    wmFileObj.close()
    # returning watermarked page object
    return pageObj

def main():
    # watermark pdf file name
    mywatermark = 'watermark.pdf'
    # original pdf file name
    origFileName = 'example.pdf'
    # new pdf file name
    newFileName = 'watermarked_example.pdf'
    
    # creating pdf File object of original pdf
    pdfFileObj = open(origFileName, 'rb')
    # creating a pdf Reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # creating a pdf writer object for new pdf
    pdfWriter = PyPDF2.PdfFileWriter()
    # adding watermark to each page
    for page in range(pdfReader.numPages):
        # creating watermarked page object
        wmpageObj = add_watermark(mywatermark, pdfReader.getPage(page))
        # adding watermarked page object to pdf writer
        pdfWriter.addPage(wmpageObj)

    # new pdf file object
    newFile = open(newFileName, 'wb')
    
    # writing watermarked pages to new file
    pdfWriter.write(newFile)

    # closing the original pdf file object
    pdfFileObj.close()
    # closing the new pdf file object
    newFile.close()

if __name__ == "__main__":
    # calling the main function
    main()
    
