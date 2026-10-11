from fastapi import FastAPI
from fastapi import APIRouter
from app.routes.users import router as users_router
app = FastAPI()
router = APIRouter()
@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}

@app.get("/health")
def health():
    return {"status": "healthy"}

app.include_router(users_router)
