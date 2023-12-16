import PyPDF2
import sys

inputs = sys.argv[1:]

PATH = './Complete_Python_Developer_in_2020-Zero-to-Mastery/pdf'
fileName = 'dummy.pdf'

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(inputs)

#with open(f'{PATH}/{fileName}', 'rb') as file: # 'rb' means read binary
#    reader = PyPDF2.PdfFileReader(file)
#    #print(reader.numPages)
#    #print(reader.getPage(0))
#    page : PyPDF2.PageObject = reader.getPage(0)
#    #print(page.rotateCounterClockwise(90))
#    page.rotateCounterClockwise(90)
#    writer = PyPDF2.PdfFileWriter()
#    writer.addPage(page)
#    with open(f'{PATH}/tilt.pdf', 'wb') as newFile:
#        writer.write(newFile)