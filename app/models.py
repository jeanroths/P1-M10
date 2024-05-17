from pydantic import BaseModel, Field, EmailStr

class OrderSchema(BaseModel):
    name: str = Field(default=None)
    email : EmailStr = Field(default=None)
    description: str = Field(default=None)

