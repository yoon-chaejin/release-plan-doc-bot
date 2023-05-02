from tkinter import filedialog
class FileController:
    def get_file_paths(self):

        file_paths = filedialog.askopenfilenames()

        return list(file_paths)