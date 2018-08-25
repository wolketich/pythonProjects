import os
import PyPDF2


def create_directory(directory):
    """Create a directory if it doesn't exist."""
    if not os.path.isdir(directory):
        os.mkdir(directory)


def get_default_text_path(pdf_path, base_dir):
    """Generate the default text file path."""
    pdf_name = os.path.basename(os.path.normpath(pdf_path))
    text_file_name = pdf_name.replace(".pdf", ".txt")
    return os.path.join(base_dir, text_file_name)


def extract_text_from_pdf(pdf_path, text_path):
    """Extract text from the PDF and write to a file."""
    # Using 'with' ensures files are closed properly after operations are performed.
    with open(pdf_path, 'rb') as pdf_obj, open(text_path, 'w') as text_file:
        pdf_reader = PyPDF2.PdfReader(pdf_obj)

        for page in pdf_reader.pages:
            text = page.extract_text()
            text_file.write(text)

        # No need to close the files explicitly as 'with' takes care of that.


def main():
    # Create a temp directory for storing text files
    base_dir = "default"
    create_directory(base_dir)

    # Get user input for file paths
    pdf_path = input("Enter the path of the pdf file: ")
    text_path = input(
        "Enter output text file path (optional, leave blank for default): ")

    # If the user doesn't specify a text file path, use the default location.
    if not text_path:
        text_path = get_default_text_path(pdf_path, base_dir)

    try:
        extract_text_from_pdf(pdf_path, text_path)
        print(f"Text extracted and saved to {text_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
