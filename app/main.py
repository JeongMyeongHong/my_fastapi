from fastapi import FastAPI
from typing import List  
from fastapi.middleware.cors import CORSMiddleware  
import pymysql
from app.services.detector import DetectorService
from app.constants.menus import LOGIN, LOGOUT, CALCULATOR, DETECT

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def home():
    return "hello"

@app.get(DETECT)
def detect(path):
    return DetectorService().detect(path)
