from fastapi import APIRouter
from app.models.users import Users
from app.services.users import get_user_service
router = APIRouter()

@router.get("/users/{user_id}", response_model=Users)
def get_user(user_id: int):
    return get_user_service(user_id)

