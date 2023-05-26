from docx import Document


def create_daily_report(release_plans):
    daily_report = Document()

    daily_report.add_table(3, 2)
    daily_report.tables[0].cell(0, 0).text = "작업자"
    daily_report.tables[0].cell(0, 1).text = "작업 내용"

    for idx, release_plan in enumerate(release_plans):
        daily_report.tables[0].cell(idx + 1, 0).text = release_plan.get_developer_name()
        daily_report.tables[0].cell(
            idx + 1, 1
        ).text = release_plan.get_release_plan_description()

    return daily_report
