import sys
import os
import img2pdf

def convert_images_to_pdf(file_path):
    if os.path.isdir(file_path):
        images = [os.path.join(file_path, fname) for fname in os.listdir(file_path) if fname.endswith(".jpg") and not os.path.isdir(os.path.join(file_path, fname))]
        with open("output.pdf", "wb") as f:
            f.write(img2pdf.convert(images))
    elif os.path.isfile(file_path) and file_path.endswith(".jpg"):
        with open("output.pdf", "wb") as f:
            f.write(img2pdf.convert(file_path))
    else:
        print("Please input a valid file or directory path.")

if __name__ == "__main__":
    file_path = sys.argv[1]
    convert_images_to_pdf(file_path)
