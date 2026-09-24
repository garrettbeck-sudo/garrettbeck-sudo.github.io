from pathlib import Path
import fitz

pdf_path = Path("attached_assets/0_Garrett_Beck_Haas_MBA_Application_Resume_1790210829873.pdf")
output_dir = Path(".agents/outputs/resume_pages")
output_dir.mkdir(parents=True, exist_ok=True)

document = fitz.open(pdf_path)
print(f"pages={document.page_count}")
print(f"metadata={document.metadata}")

for page_number, page in enumerate(document, start=1):
    print(f"\n--- PAGE {page_number} TEXT ---")
    print(page.get_text("text"))
    pixmap = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
    image_path = output_dir / f"page-{page_number}.png"
    pixmap.save(image_path)
    print(f"rendered={image_path}")

    images = page.get_images(full=True)
    print(f"embedded_images={len(images)}")
    for image_index, image_info in enumerate(images, start=1):
        xref = image_info[0]
        extracted = document.extract_image(xref)
        image_extension = extracted["ext"]
        extracted_path = output_dir / f"page-{page_number}-image-{image_index}.{image_extension}"
        extracted_path.write_bytes(extracted["image"])
        print(f"extracted={extracted_path}")