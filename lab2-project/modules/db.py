import json
file_path = 'db.json'

def read():
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data

##############################################################

def projects():
    data= read()['projects']
    user_id = authenticated()['id']
    return list(filter(lambda e: e['user_id'] == int(user_id), data))


def get_project(id):
    data = read()['projects']
    
    project = list(filter(lambda e: e['id'] == int(id) and e['user_id'] == authenticated()['id'], data))
    if project:
        return True, project[0]
    else:
        return False, None


def add_project(project):
    db = read()
    
    id = 1

    if len(db['projects']) > 0:
        id=db['projects'][-1]['id']+1

    project['id']=id
    project['user_id']=authenticated()['id']
    
    db['projects'].append(project)

    with open(file_path, 'w') as file:
        json.dump(db, file, indent=4)
        


def update_project(id, project):
    db = read()
    data = db['projects']
    
    for i in range(len(data)):
        if data[i]['id'] == int(id):
            data[i] = {**data[i], **project}
            break

    db['projects'] = data

    with open(file_path, 'w') as file:
        json.dump(db, file, indent=4)


def remove_project(id):
    db = read()
    data = db['projects']
    
    data = list(filter(lambda e: e['id'] != int(id), data))

    db['projects'] = data

    with open(file_path, 'w') as file:
        json.dump(db, file, indent=4)


def projects_by_campaign_range(start_date, end_date):
    data = read()['projects']
    
    projects = list(filter(lambda e: e['start_date'] >= start_date and e['end_date'] <= end_date and e['user_id'] == authenticated()['id'], data))
    return projects

##############################################################
 

def login(email, password):
    data = read()
    user = list(filter(lambda e: e['email'] == email and e['password'] == password, data['users']))
    if user:
        return True, user[0]
    else:
        return False, None


def logout():
    data = read()
    data["auth"]={}

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def register(user):
    db = read()
    
    id = 1

    if len(db['users']) > 0:
        id=db['users'][-1]['id']+1

    user['id']=id
    
    db['users'].append(user)

    with open(file_path, 'w') as file:
        json.dump(db, file, indent=4)
    
    return user



##############################################################

def authenticated(user=None):
    data = read()
    if user == None:
        return data['auth']
    data["auth"]=user

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def isAuth():
    authenticated_user = authenticated()
    if authenticated_user:
        return True
    return False


