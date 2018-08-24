import os
import PyPDF2


if not os.path.isdir("temp"):
    os.mkdir("temp")

text_path = ""
pdf_path = ""

pdf_path = input("Enter the path of the pdf file:")
text_path = input(
    "Enter output text file path: (optional, default: temp/<pdf_name>.txt)")

base_dir = os.path.realpath("temp")
print(base_dir)

if not text_path:
    text_path = os.path.join(base_dir, os.path.basename(
        os.path.normpath(pdf_path)).replace(".pdf", "") + ".txt")

pdf_obj = open(pdf_path, 'rb')
pdf_read = PyPDF2.PdfFileReader(pdf_obj)
num_pages = pdf_read.numPages

for i in range(num_pages):
    page_obj = pdf_read.getPage(i)
    with open(text_path, 'a+') as f:
        f.write(page_obj.extractText())
    print(page_obj.extractText())

pdf_obj.close()
