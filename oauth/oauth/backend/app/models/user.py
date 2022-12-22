from mongoengine import Document
from mongoengine.fields import StringField, BooleanField, EmailField


class User(Document):
    uuid = StringField(unique=True, required=True)
    _type = StringField(default="user")
    email = EmailField(unique=True, required=True)
    hashed_password = StringField(required=True)
    display_name = StringField(required=True)
    is_active = BooleanField(required=True)
    is_superuser = BooleanField(required=True)

    meta = {
        'db_alias': 'mongodb',
        'collection': 'user',
        'max_documents': 1000,
        'max_size': 2000000
    }


class UIUser(Document):
    uuid = StringField(unique=True, required=True)
    _type = StringField(default="ui")
    email = EmailField(unique=True, required=True)
    hashed_password = StringField(required=True)
    display_name = StringField(required=True)
    is_active = BooleanField(required=True)
    is_superuser = BooleanField(required=True)

    meta = {
        'db_alias': 'mongodb',
        'collection': 'user',
        'max_documents': 1000,
        'max_size': 2000000
    }


class APIUser(Document):
    uuid = StringField(unique=True, required=True)
    _type = StringField(default="api")
    email = EmailField(unique=True, required=True)
    display_name = StringField(required=True)
    is_active = BooleanField(required=True)
    is_admin = BooleanField(required=True)

    meta = {
        'db_alias': 'mongodb',
        'collection': 'user',
        'max_documents': 1000,
        'max_size': 2000000
    }
