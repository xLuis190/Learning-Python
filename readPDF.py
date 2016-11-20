import PyPDF2

pdFile = open('android_tutorial.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdFile)
pageObj = pdfReader.getPage(20)
print(pageObj.extractText())
