def chunk_slides(slides):
    chunks = []
    for slide in slides:
        chunks.append({
            "id": slide["slide_number"],
            "text": slide["content"]
        })
    return chunks