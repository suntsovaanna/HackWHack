import uvicorn
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

class NameQuery(BaseModel):
    fullName: str

class BulkNameQuery(BaseModel):
    fullNames: List[str]

@app.post('/name')
async def parsename(data: NameQuery):
    return data.fullName


@app.post('/names')
async def parsenamearray(data: BulkNameQuery):
    return data.fullNames[0]


@app.get('/settings')
async def getSettings():
    return "there is no settings yet"


@app.post('/settings')
async def updateSettings():
    return ""


@app.delete('/settings')
async def resetSettings():
    return

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9000)  # noqa
