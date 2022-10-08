from mongoengine import Document
from mongoengine.fields import StringField, BooleanField, EmailField


class User(Document):
    uuid = StringField(unique=True, required=True)
    email = EmailField(unique=True, required=True)
    hashed_password = StringField(required=True)
    is_active = BooleanField(required=True)
    is_superuser = BooleanField(required=True)

    meta = {
        'db_alias': 'mongodb',
        'collection': 'sns',
        'max_documents': 1000,
        'max_size': 2000000
    }
