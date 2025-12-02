from PyPDF2 import PdfReader, PdfWriter

def extract_pages(input_pdf, output_pdf, pages):
    """
    Extract specific pages from a PDF file.

    :param input_pdf: Path to input PDF file
    :param output_pdf: Path to output PDF file
    :param pages: List of page numbers (1-based indexing)
    """
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page_num in pages:
        # PyPDF2 uses 0-based index internally; user provides 1-based
        writer.add_page(reader.pages[page_num - 1])

    # Write selected pages to output PDF
    with open(output_pdf, "wb") as f:
        writer.write(f)

    print(f"Created: {output_pdf}")


# Example usage:
input_file = "FedEx Scan 2025-11-28_12-38-29 (3).pdf"
output_file = "output_pages_4_to_9.pdf"
pages_to_extract = [4, 5, 6, 7, 8, 9]

extract_pages(input_file, output_file, pages_to_extract)
