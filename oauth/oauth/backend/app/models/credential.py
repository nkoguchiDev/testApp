from mongoengine import Document
from mongoengine.fields import StringField, ReferenceField, BooleanField

from app.models import User


class Credential(Document):
    uuid = StringField(unique=True, required=True)
    _type = StringField(default="credential")
    key = StringField(unique=True, required=True)
    secret = StringField(required=True)
    user = ReferenceField(User)
    is_active = BooleanField(required=True)

    meta = {
        'db_alias': 'mongodb',
        'collection': 'credential',
        'max_documents': 1000,
        'max_size': 2000000
    }
