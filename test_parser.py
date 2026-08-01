from resume_parser import extract_text_from_pdf

pdf_path = r"C:\Users\bhoomika\Downloads\Ritesh_Raj_Resume-1.pdf"

text = extract_text_from_pdf(pdf_path)

print(text)