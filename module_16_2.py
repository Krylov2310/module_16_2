from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# запуск - python -m uvicorn module_16_2:app
info_ed = ('Домашнее задание по теме "Валидация данных".<br>'
           'Цель: научится писать необходимую валидацию для вводимых данных при помощи классов Path и Annotated.<br>'
           'Задача "Аннотация и валидация":<br>'
           'Студент Крылов Эдуард Васильевич<br>'
           'Дата: 21.11.2024г.')


# http://127.0.0.1:8000/
@app.get("/")
async def welcome() -> str:
    return "Главная страница"


# http://127.0.0.1:8000/user/admin
@app.get("/user/admin")
async def id_admin() -> str:
    return "Вы вошли как администратор"


# http://127.0.0.1:8000/user/123
@app.get("/user/{user_id}")
async def id_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")]) -> str:
    return f"Вы вошли как пользователь № {user_id}"


# http://127.0.0.1:8000/user/Edison/46
@app.get("/user/{username}/{age}")
async def users(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
                                              example="Edison")], age: Annotated[int, Path(ge=18, le=120, 
                                                                                           description="Enter age", 
                                                                                           example="25")]) -> str:
    return f"Информация о пользователе. Имя: '{username}', Возраст: '{age}'"


# http://127.0.0.1:8000/info
@app.get("/info", response_class=HTMLResponse)
async def info() -> str:
    return info_ed
