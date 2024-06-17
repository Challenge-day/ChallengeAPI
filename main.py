# main.py
import uvicorn
from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import FastAPI, Depends, HTTPException, status

from src.db.connect import get_db
from src.routes import referrals, users, mining


app = FastAPI(swagger_ui_parameters={"operationsSorter": "method"})
app.include_router(referrals.router, prefix="/api", tags=["referrals"])
app.include_router(users.router, prefix="/api", tags=["users"])
app.include_router(mining.router, prefix="/mining", tags=["mining"])

@app.get("/", name="root")
def read_root():
    """
    The read_root function is a view function that returns the root of the API.
    It's purpose is to provide a simple way for users to test if their connection
    to the API is working properly.

    :return: A dictionary
    """
    return {"message": "FastApi is working!"}

@app.get("/api/healthchecker")
def healthchecker(db: Session = Depends(get_db)):
    """
    The healthchecker function is a simple function that checks if the database
    is configured correctly. It does this by executing a simple SQL query and checking
    if it returns any results. If it doesn't, then we know something is wrong with the 
    database configuration.
    
    :param db: Session: Pass the database connection to the function
    :return: A dictionary with a message key
    """
    try:
        result = db.execute(text("SELECT 1")).fetchone()
        print(result)
        if result is None:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Database is not configured correctly")
        return {"message": "Database successfully connected"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Error connecting to the database")

if __name__ == '__main__':
    uvicorn.run(app="main:app", reload=True, host="127.0.0.1", port=8000)
   
