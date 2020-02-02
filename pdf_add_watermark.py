import PyPDF2


def add_wtrmark(wtr_file, pdf_file):
    watermark = PyPDF2.PdfFileReader(wtr_file)
    watermark_page = watermark.getPage(0)

    pdf_read = PyPDF2.PdfFileReader(pdf_file)
    pdf_write = PyPDF2.PdfFileWriter()

    for page in range(pdf_read.getNumPages()):
        pdf_page = pdf_read.getPage(page)
        pdf_page.mergePage(watermark_page)
        pdf_write.addPage(pdf_page)

    while True:
        new_path = input("Enter the path for the watermarked pdf created:  ")

        try:
            with open(new_path, mode='wb') as file1:
                pdf_write.write(file1)
                print("\nPDF Created!")
                break
        except:
            print("Enter valid path!!")


while True:

    wtr_path = input("Enter the path of the watermark pdf :  ")
    pdf_path = input("Enter the path of the pdf to be watermarked:  ")
    print(wtr_path)
    print(pdf_path)
    add_wtrmark(wtr_path, pdf_path)
    print("\n~Program Terminated~\n")
    break
