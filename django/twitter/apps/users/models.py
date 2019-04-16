from django.db import models

# Create your models here.
class UserManager(models.Manager):
    pass

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<User: {self.first_name} {self.last_name}>"
    def __str__(self):
        return f"<User: {self.first_name} {self.last_name}>"