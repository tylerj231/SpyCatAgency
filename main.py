from fastapi import FastAPI

from src.routers.routers import base_router

app = FastAPI()
app.include_router(base_router)

@app.get("/")
async def health_check():
    return {"message": "Healthy"}
