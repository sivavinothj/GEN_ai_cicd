from app.models.users import Users
from app.services.users import get_user_service


def test_get_user_service():
    user = get_user_service(1)
    assert isinstance(user, Users)
    assert user.id == 1
    assert user.name == "John Doe"
    assert user.email == "john.doe@example.com"
