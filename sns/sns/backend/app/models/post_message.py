from mongoengine import Document
from mongoengine.fields import StringField, ReferenceField

from app.models import User


class PostMessage(Document):
    uuid = StringField(unique=True, required=True)
    _type = StringField(default="message")
    message = StringField(required=True)
    user = ReferenceField(User)

    meta = {
        'db_alias': 'mongodb',
        'collection': 'message',
        'max_documents': 1000,
        'max_size': 2000000
    }