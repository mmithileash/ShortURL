from fastapi import FastAPI

from server.routers import short_url_maker, retrieve_long_url

app = FastAPI()

app.include_router(short_url_maker.router)
app.include_router(retrieve_long_url.router)
