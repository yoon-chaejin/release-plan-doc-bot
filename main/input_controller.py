# 처리할 배포계획서 파일을 입력받아라
import tkinter
from tkinter import filedialog
from file import File

class InputController:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.withdraw()
    
    def getFiles(self):
        file_routes = filedialog.askopenfilenames(parent = self.root, title = "Choose a file")

        return list(map(File, file_routes))

if __name__ == "__main__":
    inputController = InputController()
    inputController.getFiles()