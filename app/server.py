import uvicorn

from fastapi import FastAPI
from routers import settings, names

app = FastAPI()
app.include_router(settings.router)
app.include_router(names.router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9000)  # noqa
