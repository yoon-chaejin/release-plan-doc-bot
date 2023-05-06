from docx import Document

class ReleasePlan :
    def __init__(self, title, request_id):
        self.title = title
        self.request_id = request_id

class ReleasePlanFromDocxFile(ReleasePlan) :
    def __init__(self, file_path):
        self.document = Document(file_path)
        super().__init__(self.document.tables[2].cell(0,1).text, self.document.tables[2].cell(3,12).text)

    def get_developer_name(self):
        return self.document.tables[2].cell(5, 10).text

    def get_release_plan_description(self):
        return self.document.tables[2].cell(10, 1).text