from fastapi import FastAPI
from fastapi_pagination import Page, add_pagination, paginate
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class User(BaseModel):
    name: str
    surname: str


users = [
    User(name="Yurii1", surname="Karabas"),
    User(name="Yurii", surname="Karabas2"),
    User(name="Yurii3", surname="Karabas"),
    User(name="Yurii", surname="Karabas4"),
    User(name="Yurii", surname="Karabas5"),
    User(name="Yurii", surname="Karabas6"),
    User(name="Yurii", surname="Karabas6"),
    User(name="Yurii", surname="Karabas6"),
    User(name="Yurii", surname="Karabas6"),
    User(name="Yurii", surname="Karabas6"),
    User(name="Yurii", surname="Karabas6"),
    User(name="Yurii", surname="Karabas6"),
    User(name="Yurii", surname="Karabas6"),
    User(name="Yurii", surname="Karabas6"),
]


@app.get("/users", response_model=Page[User])
async def get_users():
    return paginate(users)


add_pagination(app)

uvicorn.run(app, port=8080, host="0.0.0.0")
