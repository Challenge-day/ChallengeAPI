# main.py
import uvicorn

from fastapi import FastAPI

from src.utils.lifespan import lifespan
from src.routes import referrals, users, auth  

app = FastAPI(lifespan=lifespan, swagger_ui_parameters={"operationsSorter": "method"}) # add lifespan=lifespan,

app.include_router(referrals.router, prefix="/api", tags=["referrals"])
app.include_router(users.router, prefix="/api", tags=["users"])
app.include_router(auth.router, prefix="/api", tags=["auth"])

if __name__ == '__main__':
    uvicorn.run(app="main:app", reload=True, host="127.0.0.1", port=8000)
   
