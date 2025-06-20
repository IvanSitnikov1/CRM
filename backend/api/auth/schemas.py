from datetime import date

from fastapi_users import schemas


class SUserRead(schemas.BaseUser[int]):
    first_name: str
    last_name: str
    photo: str | None
    position: str | None
    company: str | None
    birthday_date: date | None
    location: str | None
    phone_number: str | None
    skype: str | None

class SUserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    photo: str | None = None
    position: str | None = None
    company: str | None = None
    birthday_date: date | None = None
    location: str | None = None
    phone_number: str | None = None
    skype: str | None = None

class SUserUpdate(schemas.BaseUserUpdate):
    first_name: str | None = None
    last_name: str | None = None
    photo: str | None = None
    position: str | None = None
    company: str | None = None
    birthday_date: date | None = None
    location: str | None = None
    phone_number: str | None = None
    skype: str | None = None
