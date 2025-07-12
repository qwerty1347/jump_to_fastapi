from fastapi import FastAPI

from app.api.router_collector import get_api_routers


app = FastAPI()

for router in get_api_routers():
    app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}