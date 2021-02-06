import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/help')
async def help():
    return 'Hello'

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9000)  # noqa
