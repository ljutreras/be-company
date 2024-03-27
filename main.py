from fastapi import FastAPI
from src.app.routes.index import routes

app = FastAPI()
app.mount('/', routes)
