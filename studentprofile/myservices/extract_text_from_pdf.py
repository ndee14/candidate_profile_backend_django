# def extract_text_from_pdf(file):
#     """Extract text from PDF using PyPDF2 only"""
#     try:
        
#         reader = PyPDF2.PdfReader(file)
#         text = ""
#         for i, page in enumerate(reader.pages):
#             page_text = page.extract_text()
#             if page_text:
#                 text += f"--- Page {i + 1} ---\n{page_text}\n\n"

#         if text.strip():
#             return text
#         else:
#             return "This appears to be a scanned PDF. Text extraction requires OCR software."

#     except Exception as e:
#         return f"Error extracting text: {str(e)}"

import PyPDF2
from django.core.files.uploadedfile import UploadedFile

def extract_text_from_pdf(file):
    """
    Extract text from PDF using PyPDF2
    
    Args:
        file: Django UploadedFile object or file path
    
    Returns:
        str: Extracted text or error message
    """
    try:
        # Handle both file paths and UploadedFile objects
        if isinstance(file, UploadedFile):
            file.seek(0)  # Reset file pointer
            reader = PyPDF2.PdfReader(file)
        else:
            reader = PyPDF2.PdfReader(file)
        
        text = ""
        total_pages = len(reader.pages)
        
        for i in range(total_pages):
            page = reader.pages[i]
            page_text = page.extract_text()
            
            if page_text.strip():
                text += f"--- Page {i + 1} ---\n{page_text}\n\n"
            else:
                text += f"--- Page {i + 1} ---\n[No extractable text found]\n\n"
        
        # Check if any meaningful text was extracted
        if text.strip() and not all('[No extractable text found]' in page for page in text.split('--- Page')[1:]):
            return text.strip()
        else:
            return "This appears to be a scanned PDF or image-based PDF. Text extraction requires OCR software."

    except PyPDF2.PdfReadError as e:
        return f"Error reading PDF file: {str(e)}"
    except Exception as e:
        return f"Error extracting text: {str(e)}"