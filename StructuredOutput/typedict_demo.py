from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    

new_person: Person = {
    "name": "John Doe",
    "age": 30}

new1_person: Person = {
    "name": "John Doe", 
    "age":'30'
}
# No data validation is done at runtime, so this will not raise an error.
