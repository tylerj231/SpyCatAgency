from fastapi import FastAPI
from src.routers.cats.cat import cats_router

app = FastAPI()
app.include_router(cats_router)


@app.get("/")
async def health_check():
    return {"message": "Healthy"}
