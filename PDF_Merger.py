import PyPDF2
import sys

# input the file paths as arguments
input_list = []


def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    while True:
        try:
            new_pdf = input("Enter the path for the merged pdf")
            merger.write(new_pdf)
            print("\nPDF Merged!!\n")
        except:
            print("Enter valid path")
            continue
        break


while True:
    f = input("Enter the path of PDF :  ")
    input_list.append(f)
    cont = input("Do you want to continue? (y/n) :  ")
    if cont == 'n':
        break
print(input_list)
pdf_merger(input_list)
