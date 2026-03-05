import fitz

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    slides = []

    for i, page in enumerate(doc):
        text = page.get_text()
        slides.append({
            "slide_number": i+1,
            "content": text
        })

    return slides