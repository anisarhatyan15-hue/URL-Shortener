from fastapi import FastAPI

from app.database import Base, engine
from app.routers import url as url_router

Base.metadata.create_all(bind=engine)
app = FastAPI(title="URL Shortener Service")
app.include_router(url_router.router)


@app.get("/")
def root():
    return {"message": "URL Shortener API is running"}

