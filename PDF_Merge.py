import PyPDF2

def combiner_PDF(pdf_lst, output_filename):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_lst : 
        print(pdf)
        merger.append(pdf)
    merger.write(output_filename)

if __name__ == '__main__' : 
    pdf_lst = ['dummy.pdf', 'wtr.pdf']
    output_filename = 'combine.pdf'
    combiner_PDF(pdf_lst, output_filename)