from django.db import models
from django.utils import timezone as tz

import random
import string

from utils.make_access import make_access

def generate_random_string() -> str:
    token = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(20))
    return token


    
    
class AnonTokenManager(models.Manager):
    def create_token(self):
        token = self.create(
            token=generate_random_string(),
            exp_date=make_access(minutes=20)
            )
        return token



class AnonToken(models.Model):
    token = models.CharField(null=False, unique=True)
    exp_date = models.DateTimeField()
    
    objects = AnonTokenManager()