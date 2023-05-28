import os

from main import file_controller as fc
from main import release_plan_controller as rpc


file_controller = fc.FileController()
file_paths = file_controller.get_file_paths()
release_plans = rpc.ReleasePlanController.from_docx_file_paths(file_paths)
daily_report = rpc.ReleasePlanController.create_daily_report(release_plans)
file_controller.save_document_as_docx_file(
    os.getcwd() + "/", "daily_report.docx", daily_report
)
