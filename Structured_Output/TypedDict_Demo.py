'''TypeDict is a way to define a dictionary with a specific structure in Python.
It allows you to specify the keys and their corresponding value types, providing better type checking and code clarity.
it doesnot validate data at runtime but helps type hints for better coding.'''


from typing import TypedDict


class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'Prakash', 'age':'21'}

print(new_person)