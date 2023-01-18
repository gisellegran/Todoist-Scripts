from config import API_KEY
from todoist_api_python.api import TodoistAPI
from todoist_api_python.api import Project
from todoist_api_python.api import Section

api = TodoistAPI(API_KEY)

#get project object from its name 

def getProject(name):
    projects = api.get_projects()
    for project in projects:
        if project.name.lower() == name.lower():
            return project
        
#get section from its name 
def getSection(name, project:Project = None):
    if project :
        sections = getProjectSections(project)
    else: 
        sections = api.get_sections()      

    for s in sections:
        if s.name.lower() == name.lower():
            return s
        
#get the secitons belonging to a project
def getProjectSections(project:Project):
    sections = api.get_sections()
    return [s for s in sections if s.project_id == project.id]


#add reoccuring task as individual numbered tasks
#arguments: date, time, timedelay, number, exlucsions, task template
def bulk_numbered_tasks(**kwargs):
    if 'dates' not in kwargs:
        dates = get_dates(**kwargs)
    else:
        dates = kwargs['dates']
        
    try:
        
        time = kwargs['time']
        task = kwargs['task']
        task_template = kwargs['task_template']
        
        i = 1
        for date in dates :
                task_template['due_string'] = date
                task_template['content'] = task + " " + str(i)
                task_template['due_string'] = date.strftime("%m-%d-%y")+" "+time.strftime("%H:%M")

                api.add_task(**task_template)
                i+=1
                    
            
    except Exception as error:
        print(error)

#generate list of dates from start date and time delta
def get_dates(**kwargs):
    start_date = kwargs['start_date']
    timedelta = kwargs['timedelta']
    if 'excl_list' in kwargs:
        excl_list = kwargs['excl_list']
    else :
        excl_list = []

    dates = []
    date = start_date
    i=0
    while i < kwargs['n']:
        if date not in excl_list:
            dates.append(date)
            i+=1

        date+=timedelta

    return dates

def delete_labels(exclude):
    all_labels = api.get_labels()
    exclude = [x.lower() for x in exclude]

    for l in all_labels:
        if l.name.lower() not in exclude:
            try:
                is_success = api.delete_label(label_id=l.id)
                print(is_success)
            except Exception as e:
                print(e)
