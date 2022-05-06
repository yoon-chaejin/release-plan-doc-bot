from abc import abstractclassmethod
from main.file import File

from main.release_plan_doc import ReleasePlanDoc


class Scraper:
    
    @abstractclassmethod
    def scrape(cls, source):
        pass

class FileScraper(Scraper):
    __routes = {
        "title" : "tables[2].rows[0].cells[1].text",
        "working_time" : "tables[2].rows[1].cells[1].text",
        "release_time" : "tables[2].rows[1].cells[-2].text",
        "request_corporation" : "tables[2].rows[2].cells[1].text",
        "request_group" : "tables[2].rows[2].cells[7].text",
        "request_person" : "tables[2].rows[2].cells[-2].text",
        "sor_id" : "tables[2].rows[3].cells[-2].text",
        "target_service" : "tables[2].rows[4].cells[1].text",
        "risk_level" : "tables[2].rows[4].cells[-2].text",
        "response_group" : "tables[2].rows[5].cells[1].text",
        "developer" : "tables[2].rows[5].cells[-2].text",
        "task" : "tables[2].rows[10].cells[1].text"
    }

    def scrape(cls, source:File):
        data = dict({})

        for key, value in cls.__routes.items():
            data[key] = source.retrieveFromPosition(value)
        
        return ReleasePlanDoc(**data)