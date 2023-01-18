import bulk_tasks
import datetime

#build task template

project = bulk_tasks.getProject("School")
section = bulk_tasks.getSection("Deadlines")

task_template = {
    "project_id" : project.id,
    "section_id" : section.id,
    "due_lang": "en",
    "labels": ["CSI2520"],
    "priority": 4,
}


""" bulk_tasks.bulk_numbered_tasks(
    task = 'Quiz Scheme',
    start_date = datetime.date(2023,3,30),
    time = datetime.time(23,30),
    timedelta = datetime.timedelta(days=7),
    n = 3,
    excl_list = [],
    task_template = task_template,
) """


""" bulk_tasks.bulk_numbered_tasks(
    task = 'Devoir',
    dates = [datetime.date(2023,3,13),datetime.date(2023,3,30),datetime.date(2023,4,10)],
    time = datetime.time(23,30),
    task_template = task_template,
) """

keep_labels = ['CSI2520', 'ELG2736', 'Adsorption', 'waiting']
bulk_tasks.delete_labels(keep_labels)
