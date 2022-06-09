from http.client import HTTP_PORT
from fastapi import APIRouter, HTTPException, Depends
# from ..dependencies import get_token_header
from typing import Optional
from pydantic import BaseModel
from nlp import models

router = APIRouter(
    prefix = '/sentiment',
    tags = ['sentiment'],
    # dependencies=[Depends(get_token_header)],
    responses={404: {'description': 'Not Found'}}
)

news_sentiment = models.SentimentModel()

class NewsSentimentRequestBody(BaseModel):
    titles: list
    
@router.post('/analyze')
async def analyze(request: NewsSentimentRequestBody):
    count = len(request.titles)
    titles = request.titles
    
    results = news_sentiment.predict(titles)

    print(results)
    return {'result': results}



    

    