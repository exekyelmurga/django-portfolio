from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.db.models import DateField, TextField
import datetime


class Post(models.Model):
    title = CharField(max_length=100)
    description = TextField(default = 'Default description')
    image = ImageField(upload_to="blog/images/")
    date = DateField(datetime.date.today)
