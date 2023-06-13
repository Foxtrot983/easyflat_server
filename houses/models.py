from django.db import models
from account.models import CustomUser
from django.utils import timezone

class Marketplace(models.Model):
    name = models.CharField(blank=True, null=True)

    class Meta:
        db_table = 'marketplace'
        
    def __str__(self):
        return f"{self.id}: {self.name}"

class House(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    amountusd = models.SmallIntegerField(db_column='amountUSD', blank=True, null=True)
    amountbyn = models.SmallIntegerField(db_column='amountBYN', blank=True, null=True)
    rent_rooms = models.SmallIntegerField(default=0)
    address = models.CharField(max_length=150, blank=True, null=True)
    url = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    agency = models.BooleanField(default=False)
    description = models.CharField(blank=True, null=True)
    marketplace = models.ForeignKey(Marketplace, models.CASCADE, blank=True, null=True, related_name='marketplace')
    location_a = models.CharField(blank=True, null=True)
    location_b = models.CharField(blank=True, null=True)
    phoneNumber = models.CharField(db_column='phoneNumber', blank=True, null=True)
    

    class Meta:
        db_table = 'house'
        
    def __str__(self) -> str:
            return f"{self.marketplace.name}: {self.address}"    


class HousePhoto(models.Model):
    house = models.ForeignKey(House, models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to="house-photos/", unique=True, blank=True, null=True)

    class Meta:
        db_table = 'house_photo'


