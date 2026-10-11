from app.models.users import Users

def get_user_service(user_id: int) -> Users:
    return Users(id=user_id, name="John Doe", email="john.doe@example.com")