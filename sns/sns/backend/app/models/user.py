import pymongo

from beanie import Document, Indexed


class User(Document):
    id: Indexed(int)
    full_name: Indexed(str, index_type=pymongo.TEXT)
    email: Indexed(str, index_type=pymongo.TEXT, unique=True)
    hashed_password: str
    is_active: bool = True
    is_superuser: bool = False
