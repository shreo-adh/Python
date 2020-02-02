import PyPDF2

file_path = input("Input file path:  ")
rotate = 0
with open(file_path, mode='rb') as my_file:
    reader = PyPDF2.PdfFileReader(my_file)
    page = reader.getPage(0)
    rotate = int(input("Enter the degree of rotation(Clockwise):  "))
    page.rotateClockwise(rotate)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    new_file_path = input("Enter path of new file:  ")
    with open(new_file_path, mode='wb') as new_file:
        writer.write(new_file)
