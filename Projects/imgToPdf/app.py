import sys
import os
import img2pdf

def convert_images_to_pdf(file_path, output_path="output.pdf"):
    """
    Convert a single image or all images in a directory to a single PDF.

    :param file_path: Path to the image file or directory containing image files.
    :param output_path: The desired path for the output PDF.
    """
    try:
        # List to hold image file paths
        images = []

        # Check if the path leads to a directory
        if os.path.isdir(file_path):
            # Retrieve all images in the directory
            images = [os.path.join(file_path, fname) for fname in os.listdir(file_path) 
                      if fname.lower().endswith(".jpg") and not os.path.isdir(os.path.join(file_path, fname))]

            # Check if there are any images in the directory
            if not images:
                print("No images found in the directory.")
                return

        # Check if the path leads to a file
        elif os.path.isfile(file_path) and file_path.lower().endswith(".jpg"):
            images.append(file_path)

        else:
            print("Invalid path. Please enter a correct file or directory path.")
            return

        # Convert images to PDF
        with open(output_path, "wb") as f:
            f.write(img2pdf.convert(images))

        print(f"PDF has been successfully saved to {os.path.abspath(output_path)}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <path_to_image_or_directory>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Optional: Implement a way to accept the output path as an argument.
    # output_path = sys.argv[2] if len(sys.argv) > 2 else "output.pdf"
    
    convert_images_to_pdf(file_path)  # Pass output_path if you accept it as an argument.

if __name__ == "__main__":
    main()
