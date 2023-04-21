import PyPDF2

def rotate_PDF(target_pdf, output_filename, target_page, degree) : 
    with open(target_pdf, 'rb') as file :
        reader = PyPDF2.PdfFileReader(file)
        page = reader.getPage(target_page)
        page.rotateCounterClockwise(degree)
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        with open(output_filename, 'wb') as new_file : 
            writer.write(new_file)

if __name__ == '__main__' : 
    target_pdf = 'dummy.pdf'
    output_filename = 'rotated.pdf'
    rotate_PDF(target_pdf, output_filename, 0, 90)