# main.py
import uvicorn
import asyncio

from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.start_bot import start_bot
from src.routes import referrals, users, auth

@asynccontextmanager
async def lifespan(app: FastAPI):
    await start_bot()
    yield


app = FastAPI(lifespan=lifespan, swagger_ui_parameters={"operationsSorter": "method"})

app.include_router(referrals.router, prefix="/api", tags=["referrals"])
app.include_router(users.router, prefix="/api", tags=["users"])
app.include_router(auth.router, prefix="/api", tags=["auth"])

if __name__ == '__main__':
    uvicorn.run(app="main:app", reload=True, host="127.0.0.1", port=8000)
   
