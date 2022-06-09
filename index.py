from fastapi import FastAPI, Query 
from typing import Optional
from pydantic import BaseModel
import sys
import pathlib
from routers import sentiment

cwd = pathlib.Path(__file__).parent
sys.path.append(str(cwd))

app = FastAPI()

app.include_router(sentiment.router)

@app.get('/')
def health_check():
    return {'message': 'healthy'}