
'''Pydantic is a data validation and settings management library for Python.
It allows you to define data models with type annotations, and it automatically validates the data against the specified types.'''
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
new_person = {'name': 'Prakash', 'age': 21} # age should be int not str
person=Person(**new_person)
print(person)