import os
import PyPDF2
import warnings

# will not give warning while printing pfd page
warnings.simplefilter('ignore')

pdf_path = './YashEdu/python ch 4-17/Project/New folder'  # . means current path
dir = os.listdir(pdf_path)  # scan files in path
src_files = []
for file in dir:
    if file[-3:] == 'pdf':
        src_files.append(file)

print(f'files are {src_files}')

pdfWriter = PyPDF2.PdfFileWriter()

for file in src_files:
    pdfFile = open(pdf_path+'\\' + file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdf_num = (input(
        f'Entere page Number  as comma separeted from {file} between 0 and {pdfReader.numPages - 1}  ')).split(',')
    # numPages give total no.of pages  , split will separete numbers and will create list

    for pageNum in range(pdfReader.numPages):
        # as pdf1_num is list contained values as string therfr we convert pageNum into string
        if str(pageNum) in pdf_num:
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
            # print(pageObj.extractText())

pdfOutputFile = open(pdf_path+'\\'+'combined.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfFile.close()
pdfOutputFile.close()

# note- delete combined.pdf file
