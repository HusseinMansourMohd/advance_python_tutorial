import json

person = {"name":"John", "age":30 , "city": "New York" , "hasChilderen":False} 

personJason = json.dumps(person , indent=10 , separators=(': ',': ') , sort_keys=True)

print(personJason)

# convert back to dictionary 

with open('person.json', 'r') as file:  
    person = json.load(file)
    print(person)

########################################

import json

class User:
    def __init__(self, name , age) :
        self.name = name
        self.age = age 

user = User('Max', 27)

def encide_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age':o.age, o__class__.__name__:True}
    else:
        raise TypeError
    
class UserENcoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name,'age':o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)
    
userJSON = UserENcoder().encode(user)
print(userJSON)

def decode_user(dct):
    if user.__name__ in dct:
        return User(name=dct['name'] , age=dct['age'])

# userJSON = json.dumps(user, default=encode_user)
# print(userJSON)

user = json.loads(userJSON , object_hook=decode_user)
print(type(user))
print(user.name)
