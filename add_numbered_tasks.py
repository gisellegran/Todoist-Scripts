from config import API_KEY
from todoist_api_python.api import TodoistAPI

api = TodoistAPI(API_KEY)

try:
    projects = api.get_projects()
    print(projects)
except Exception as error:
    print(error)