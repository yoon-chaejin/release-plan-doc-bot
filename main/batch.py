from file_controller import FileController
from release_plan import ReleasePlanFromDocxFile
from main import create_daily_report
import os

file_controller = FileController()
file_paths = file_controller.get_file_paths()
release_plans = [ReleasePlanFromDocxFile(i) for i in file_paths]
daily_report = create_daily_report(release_plans)
file_controller.save_document_as_docx_file(os.getcwd()+'/', 'daily_report.docx', daily_report)
