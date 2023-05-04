from tkinter import filedialog
from docx import Document
class FileController:
    def get_file_paths(self):

        file_paths = filedialog.askopenfilenames()

        return list(file_paths)
    
    def save_document_as_docx_file(self, file_path, file_name, document):
        document.save(file_path + file_name)