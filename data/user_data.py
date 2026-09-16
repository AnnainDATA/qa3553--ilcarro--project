from faker import Faker
from models.user import User

fake = Faker()

def create_user(name=None, last_name=None, email=None, password=None):
    return User(
        name if name is not None else fake.first_name(),
        last_name if last_name is not None else fake.last_name(),
        email if email is not None else fake.unique.email(),
        password if password is not None else fake.password(
            length=10, special_chars=True, digits=True, upper_case=True, lower_case=True
        )
    )
def existing_user():
    return create_user(
        name="Moshe",
        last_name="Kohen",
        email = "anna12345@gmail.com",
        password = "123456!Anna")

# def invalid_email_user():
#     return create_user(email=INVALID_EMAIL, password=EXISTING_USER_PASSWORD)
#
# def invalid_password_user():
#     return create_user(email=EXISTING_USER_EMAIL, password=INVALID_PWD)


