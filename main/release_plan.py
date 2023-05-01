from docx import Document

class ReleasePlan :
    def __init__(self, title, request_id):
        self.title = title
        self.request_id = request_id

class ReleasePlanFromDocxFile(ReleasePlan) :
    def __init__(self, file_path):
        document = Document(file_path)
        super().__init__(document.tables[2].cell(0,1).text, document.tables[2].cell(3,12).text)