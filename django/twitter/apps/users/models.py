from django.db import models
import bcrypt
import re
from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def validate(self, form):
        errors = []

        if len(form['first_name']) < 1:
            errors.append("First name must not be blank")

        if len(form['last_name']) < 1:
            errors.append("Last name must not be blank")

        if not EMAIL_REGEX.match(form['email']):
            errors.append('Email must be valid')

        matching_users = User.objects.filter(email=form['email'])
        if matching_users:
            errors.append("Email already in use")

        submitted_time = datetime.strptime(form['birthday'], '%Y-%m-%d')
        now = datetime.now()
        if submitted_time >= now:
            errors.append("Birthday must be in the past")

        if len(form['password']) < 8:
            errors.append("Password must be 8 characters long")

        return errors

    def easy_create(self, form):
        pw_hash = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())

        user = User.objects.create(
            first_name=form['first_name'],
            last_name=form['last_name'],
            email=form['email'],
            birthday=form['birthday'],
            pw_hash=pw_hash
        )
        return user.id

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=500)
    birthday = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f"<User: {self.first_name} {self.last_name}>"
    def __str__(self):
        return f"<User: {self.first_name} {self.last_name}>"