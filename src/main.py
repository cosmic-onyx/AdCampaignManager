import uvicorn
from fastapi import FastAPI

from api.routers.Event import event_router


app = FastAPI()


@app.get("/")
async def index():
    return {"message": "FastAPI service is working!"}


app.include_router(
    event_router,
)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port='8080',
        reload=True
    )