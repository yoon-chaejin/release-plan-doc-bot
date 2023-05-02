from tkinter import filedialog
class FileController:
    def getFilePaths(self):

        filePaths = filedialog.askopenfilenames()

        return list(filePaths)