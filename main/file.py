from docx import Document

class File():
    def __init__(self, file_route):
        self.filename = file_route.split('/')[-1]
        self.document = Document(file_route)
        self.file_route = file_route