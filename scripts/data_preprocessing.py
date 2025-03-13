# scripts/data_preprocessing.py
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import json

# Existing resume processing methods
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    return "\n".join([page.extract_text() for page in reader.pages])

def split_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n", "  ", ".", "! "]
    )
    return splitter.split_text(text)

def save_chunks(chunks, output_path):
    with open(output_path, "w") as f:
        json.dump({"chunks": chunks}, f, indent=2)

# New Q&A processing method
def process_qa_file(qa_path):
    """Converts Q&A pairs into formatted chunks"""
    with open(qa_path) as f:
        qa_data = json.load(f)
    
    # Format as "Q: ...\nA: ..." chunks
    return [f"Q: {pair['question']}\nA: {pair['answer']}" 
            for pair in qa_data["qa_pairs"]]

# Main script
if __name__ == "__main__":
    # 1. Process resume and LinkedIn
    resume_text = extract_text_from_pdf("data/raw/WintonGee_resume.pdf")
    resume_chunks = split_text(resume_text)

    linkedin_text = extract_text_from_pdf("data/raw/LinkedIn_Profile.pdf")
    linkedin_chunks = split_text(resume_text)
    
    # 2. Process Q&A
    qa_chunks = process_qa_file("data/processed/qa_pairs.json")  # New line
    
    # 3. Combine and save
    all_chunks = resume_chunks + linkedin_chunks + qa_chunks  # Combine sources
    save_chunks(all_chunks, "data/processed/resume_chunks.json")
    print(f"Saved {len(all_chunks)} combined chunks!")