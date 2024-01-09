from pydantic import BaseModel

# pydantic model to verify requestbody for user
class myUser(BaseModel):
    username: str
    email: str
    password: str