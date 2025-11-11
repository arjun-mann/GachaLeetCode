from fastapi import FastAPI #imports FastAPI
from fastapi.middleware.cors import CORSMiddleware #imports CORS
from pydantic import BaseModel #defines data schemas for requests and responses
import os #OS
from dotenv import load_dotenv #laods key-val pairs from .env

load_dotenv() #example .env
app = FastAPI() #creates FastAPI app instance to handle routes, middleware, requests
origins = [ #creates a list of allowed frontend origins
    os.getenv("Front_URL", "http://localhost:3000")
]

app.add_middleware( #wraps app in CORS
    CORSMiddleware, 
    allow_origins=origins, #what URLS we can talk to
    allow_credentials=True, #cookies
    allow_methods=["*"], #all HTTP methods
    allow_headers=["*"], #all custom headers
)

class Message(BaseModel): #body must contain text str
    text: str
    
@app.get("/") #get for root
def read_root():
    return {"message": "FastAPI backend running"}

@app.get("/echo") #returns resp
def echo_message(msg: Message):
    return {"you sent": msg.text}