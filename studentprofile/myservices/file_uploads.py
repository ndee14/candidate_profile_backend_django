import PyPDF2
from django.core.files.uploadedfile import UploadedFile

def extract_text_from_pdf(file):
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


def document_upload(request):
    file_fields = ['cv', 'academic_transcript', 'qualification1', 'qualification2', 'professional_photo']

    for file in file_fields:
        document = request.FILES.get(file, None)

        if not document:
            continue

        file_name = document.name
        file_size = document.size
        
        file_info = {
            'filename': file_name,
            'filepath': '',
            'size': file_size,
            'field': document
        }

        if file != 'professional_photo' and file_name.lower().endswith('.pdf'):
            print("Extracting text from PDF:", file_name)
            extracted_text = extract_text_from_pdf(document)
            file_info['extracted_text'] = extracted_text

        # uploaded_files[file] = file_info

# def upload_documents():
#     profile_id = str(uuid.uuid4())
#     profile_folder = os.path.join(app.config['PROFILES_FOLDER'], profile_id)
#     os.makedirs(profile_folder, exist_ok=True)

#     uploaded_files = {}
#     file_fields = ['cv', 'academic_transcript', 'qualification1', 'qualification2', 'professional_photo']

#     for field in file_fields:
#         if field not in request.files:
#             continue
#         file = request.files[field]
#         if file.filename == '':
#             continue
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             field_folder = os.path.join(profile_folder, field)
#             os.makedirs(field_folder, exist_ok=True)
#             filepath = os.path.join(field_folder, filename)
#             file.save(filepath)

#             file_info = {
#                 'filename': filename,
#                 'filepath': filepath,
#                 'size': os.path.getsize(filepath),
#                 'field': field
#             }

#             if field != 'professional_photo' and filename.lower().endswith('.pdf'):
#                 extracted_text = extract_text_from_pdf(filepath)
#                 file_info['extracted_text'] = extracted_text

#             uploaded_files[field] = file_info

#     if not uploaded_files:
#         flash('No valid files were uploaded')
#         return redirect(request.url)

#     files_info_path = os.path.join(profile_folder, 'files_info.json')
#     with open(files_info_path, 'w') as f:
#         files_for_json = {field: {'filename': info['filename'], 'size': info['size'], 'field': info['field']}
#                           for field, info in uploaded_files.items()}
#         json.dump(files_for_json, f)

#     session['profile_id'] = profile_id
#     return redirect(url_for('profile', profile_id=profile_id))

