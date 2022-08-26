from fastapi import FastAPI
from typing import List  
from starlette.middleware.cors import CORSMiddleware  
from db import session  
from model import UserTable, User  
import pymysql
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/users")
def read_users():
    print(' ########## 여기는 들어옴 ######## ')
    db = pymysql.connect(
        host='127.0.0.1', 
        port=3306, 
        user='user', 
        passwd='password', 
        db='sample_db', 
        charset='utf8'
    )
    result = []
    try:
        print(' ### try 내부 들어옴')
        with db.cursor() as cursor:
            sql = "SELECT * FROM `user`"
            print(' ### sql : '+ sql)
            cursor.execute(sql)
            
            result = cursor.fetchall()
            print(' ### while 내부 들어옴')
            print(result)         
    finally:
        db.close()

    # users = session.query(UserTable).all()
    return result

@app.get("/users/{user_id}")
def read_user(user_id: int):
    user = session.query(UserTable).\
        filter(UserTable.id == user_id).first()
    return user

@app.post("/user")

async def create_user(name: str, age: int):
    user = UserTable()
    user.name = name
    user.age = age
    session.add(user)
    session.commit()

@app.put("/users")
async def update_users(users: List[User]):
    for new_user in users:
        user = session.query(UserTable).\
            filter(UserTable.id == new_user.id).first()
        user.name = new_user.name
        user.age = new_user.age
        session.commit()
