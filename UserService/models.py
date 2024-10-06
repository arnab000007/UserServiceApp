from django.db import models
from django.utils import timezone
from  django.contrib.auth.hashers import make_password,check_password
import  uuid
# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hashed_password = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    roles = models.ManyToManyField(Role)

    def set_password(self, password):
        self.hashed_password = make_password(password)

    def match_password(self, password):
        return check_password(password, self.hashed_password)

    def generate_auth_token(self, valid_seconds = 3600):
        token = Token(user=self, token=uuid.uuid4())
        token.set_expire_at(valid_seconds)
        token.save()
        return token

    @property
    def is_authenticated(self):
        return True


class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=True)
    expires_at = models.DateTimeField()
    is_blacklisted = models.BooleanField(default=False)

    def set_expire_at(self, valid_seconds = 3600):
        self.expires_at = timezone.now() + timezone.timedelta(seconds=valid_seconds)

    def is_valid_token(self):
        return self.is_valid and not self.is_blacklisted and self.expires_at > timezone.now()