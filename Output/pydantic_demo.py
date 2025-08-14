from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Person(BaseModel):
    name: str = "harshil"
    age : Optional[int] = None
    email: EmailStr
    marks: float = Field(gt = 0, lt=100, default=0.0, description="Marks should be between 0 and 100")
person = {"age" :"21", "email": "abc@gmail.com", "marks": 90.5}

new_person = Person(**person)

print(new_person)

#in pydantic, there is functionality to validate the data if data is not match then it try convert to correct type