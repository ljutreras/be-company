from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.app.routes.index import routes

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
)

app.mount('/', routes)
