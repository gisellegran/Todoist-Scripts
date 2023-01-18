from config import API_KEY
from todoist_api_python.api import TodoistAPI
import datetime

api = TodoistAPI(API_KEY)

PROJECTS = api.get_projects()

def getProjectID(name):
    for project in PROJECTS:
        if name.lower() == project.name.lower():
            return project.id

try:
    
    id = getProjectID("School")
    print(id)
    date = datetime.date(2023,1,23)
    time = datetime.time(23,30)
    one_week = datetime.timedelta(days=7)
    i=0
    while i < 11 :
        if date != datetime.date(2023, 2, 20) :
            print(date.strftime("%y-%m-%d")+" "+time.strftime("%H:%M"))
            
        
            task = api.add_task(
                content="Laboratoire "+str(i+1),
                project_id=str(id),
                due_string=date.strftime("%m-%d-%y")+" "+time.strftime("%H:%M"),
                due_lang="en",
                labels=["CSI2520"],
                priority=4,
            )
            i+=1
            

        date += one_week
    
except Exception as error:
    print(error)

