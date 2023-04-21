import PyPDF2

def watermarker_PDF(template_filename, watermark_filename, output_filename) : 
    template = PyPDF2.PdfFileReader(open(template_filename, 'rb'))
    watermark = PyPDF2.PdfFileReader(open(watermark_filename, 'rb'))

    output = PyPDF2.PdfFileWriter()
    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

    with open(output_filename, 'wb') as file:
        output.write(file)

if __name__ == '__main__' :     
    template_filename = 'combine.pdf'
    watermark_filename = 'wtr.pdf'
    output_filename = 'watermark.pdf'

    watermarker_PDF(template_filename, watermark_filename, output_filename)
