import pymongo

def welcome():
    print('*****************************************************************')
    print('**      Mongo Rookie Employee v0.1                             **')
    print('*****************************************************************')
    print()
    print('Start input employees...')
    print()

def getDbConn():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    return client.testdb    

def storeUser(collection):
    name = input('Name: ')
    age = input('Age: ')
    phone = input('Phone: ')
    employee = {
        "name": name,
        "age": age,
        "phone": phone
    }
    collection.insert(employee)
    print('Employee insert successful!')
    
def listUsers(users):
    for user in users:
        print('Name: %s' % user['name'])
        print('Age: %s' % user['age'])
        print('Phone: %s' % user['phone'])
        print('---------------------------------------------------------')    

def main():
    welcome()
    db = getDbConn()
    collection = db.users
    
    while (True):
        print()
        isContinue = input('Continue?(y/n)')
        if (isContinue.upper() != 'Y'):
            break
        
        # store new user
        storeUser(collection)
        
        print()
        print('All Employees:')
        print('##########################################################')
        
        # show all users
        users = collection.find()
        listUsers(users)
    
    print('** Program End! Byebye! :-)')
    
if __name__=='__main__':
    main()    



    
    
    
    