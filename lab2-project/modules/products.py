import os
import re
from time import sleep
from .db import projects, logout, authenticated, add_project,get_project,update_project,remove_project,projects_by_campaign_range


def projectsForm():
    action = 0

    while True:
        os.system('clear')

        user=authenticated()['first_name']

        print(f"Hello, {user}")
        print("1) list projects")
        print("2) create project")
        print("3) edit project")
        print("4) delete project")
        print("5) search for projects")
        print("6) logout")
        print("7) exit")

        try:
            action = int(input("action: "))
        except:
            action=8

        match action:
            case 1:
                list_projects()
            case 2:
                create_project()
            case 3:
                edit_project()
            case 4:
                delete_project()
            case 5:
                search_projects()
            case 6:
                os.system('clear')
                logout()
                break
            case 7:
                os.system('clear')
                break




def list_projects(_projects = None):
    os.system('clear')

    data = projects() if _projects is None else _projects
    
    if len(data)==0:
        print("No projects found")
        input("press enter to return back")
        return None
    
    keys = data[0].keys()
    
    for a in range(len(data)):
        for b,c in enumerate(keys):
            print(f"{c} ====> {data[a][c]}")
        print('-' * 80)

    input("press enter to return back")
    return None


def create_project():
    os.system('clear')
    print("Create New Project")


    while True:
        title = input(f"Title: ") 
        if re.fullmatch(r'[A-Za-z0-9 ]{1,100}', title):
            break
        print("Invalid title. alphanumeric characters and spaces max 100 char.")

    while True:
        details = input(f"Details: ") 
        if re.fullmatch(r'.{10,}', details):
            break
        print("Invalid details. Minimum 10 characters required.")

    while True:
        target = input(f"Target: ") 
        if re.fullmatch(r'\d+', target):
            break
        print("Invalid target. Use numbers only.")

    while True:
        start_date = input(f"Start Date: ") 
        if re.fullmatch(r'\d{2}-\d{2}-\d{4}', start_date):
            break
        print("Invalid start date. Use DD-MM-YYYY format.")

    while True:
        end_date = input(f"End Date: ") 
        if re.fullmatch(r'\d{2}-\d{2}-\d{4}', end_date):
            break
        print("Invalid end date. Use DD-MM-YYYY format.")


    project = {
        "title": title,
        "details": details,
        "target": target,
        "start_date": start_date,
        "end_date": end_date,
    }

    add_project(project)


def edit_project():
    os.system('clear')

    id = input("Edit Project [id]: ")
    found, project = get_project(id)

    if found == False:
        print("Project not found")
        sleep(2)
        return


    while True:
        title = input(f"Title `{project['title']}`: ") or project["title"]
        if re.fullmatch(r'[A-Za-z0-9 ]{1,100}', title):
            break
        print("Invalid title. alphanumeric characters and spaces max 100 char.")

    while True:
        details = input(f"Details `{project['details']}`: ") or project["details"]
        if re.fullmatch(r'.{10,}', details):
            break
        print("Invalid details. Minimum 10 characters required.")

    while True:
        target = input(f"Target `{project['target']}`: ") or project["target"]
        if re.fullmatch(r'\d+', target):
            break
        print("Invalid target. Use numbers only.")

    while True:
        start_date = input(f"Start Date `{project['start_date']}`: ") or project["start_date"]
        if re.fullmatch(r'\d{2}-\d{2}-\d{4}', start_date):
            break
        print("Invalid start date. Use DD-MM-YYYY format.")

    while True:
        end_date = input(f"End Date `{project['end_date']}`: ") or project["end_date"]
        if re.fullmatch(r'\d{2}-\d{2}-\d{4}', end_date):
            break
        print("Invalid end date. Use DD-MM-YYYY format.")
        
    project = {
        "title": title,
        "details": details,
        "target": target,
        "start_date": start_date,
        "end_date": end_date,
    }
  
    update_project(id, project)


def delete_project():
    os.system('clear')

    id = input("Delete Project [id]: ")
    found,_ = get_project(id)

    if found == False:
        print("Project not found")
        sleep(2)
        return
  
    remove_project(id)


def search_projects():
    os.system('clear')

    while True:
        start_date = input(f"Compain start: ") 
        if re.fullmatch(r'\d{2}-\d{2}-\d{4}', start_date):
            break
        print("Invalid Compain start. Use DD-MM-YYYY format.")

    while True:
        end_date = input(f"Compain end: ") 
        if re.fullmatch(r'\d{2}-\d{2}-\d{4}', end_date):
            break
        print("Invalid Compain end. Use DD-MM-YYYY format.")

    projects = projects_by_campaign_range(start_date, end_date) 

    list_projects(projects)
       