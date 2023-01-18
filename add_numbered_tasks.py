from todoist_api_python.api import TodoistAPI

api = TodoistAPI(secrets.TODOIST_API_TOKEN)

try:
    projects = api.get_projects()
    print(projects)
except Exception as error:
    print(error)