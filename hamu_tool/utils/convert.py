import fitz

def extract_text_from_pdf(pdf_path : str) -> list[str]:
    """Extract text from a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        list[str]: List of text in each page.
    """
    document = fitz.open(pdf_path)
    num_pages = document.page_count

    page_text = []
    for page_num in range(num_pages):
        page = document.load_page(page_num)
        text_raw = page.get_text()
        text = []
        for line in text_raw.split('\n'):
            line = line.strip()
            if not line:
                continue
            if line[-1] == '-':
                line = line[:-1]
            else:
                line += ' '
            text.append(line)
        text = ''.join(text)
        page_text.append(text)

    return page_text
