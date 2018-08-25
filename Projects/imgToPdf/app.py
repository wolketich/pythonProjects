import sys
import img2pdf
import os

# Get the file path from the command line argument
filepath = sys.argv[1]

# Check if the file path is a directory
if os.path.isdir(filepath):
    with open("output.pdf", "wb") as f:
        imgs = []
        # Loop through all files in the directory
        for fname in os.listdir(filepath):
            # Check if the file is a jpg image
            if not fname.endswith(".jpg"):
                continue
            path = os.path.join(filepath, fname)
            # Check if the file is a directory
            if os.path.isdir(path):
                continue
            imgs.append(path)
        # Convert all images to pdf and write to file
        f.write(img2pdf.convert(imgs))

# Check if the file path is a file
elif os.path.isfile(filepath):
    # Check if the file is a jpg image
    if filepath.endswith(".jpg"):
        with open("output.pdf", "wb") as f:
            # Convert the image to pdf and write to file
            f.write(img2pdf.convert(filepath))

# Print an error message if the file path is not a file or directory
else:
    print("please input file or dir")
