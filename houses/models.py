from django.db import models

class Marketplace(models.Model):
    name = models.CharField(blank=True, null=True)

    class Meta:
        db_table = 'marketplace'
        
    def __str__(self):
        return f"{self.id}: {self.name}"

class House(models.Model):
    amountusd = models.SmallIntegerField(db_column='amountUSD', blank=True, null=True)
    amountbyn = models.SmallIntegerField(db_column='amountBYN', blank=True, null=True)
    rent_rooms = models.SmallIntegerField(blank=True, null=True, default=0)
    address = models.CharField(blank=True, null=True, default="Minsk")
    url = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    agency = models.BooleanField(blank=True, null=True)
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
    image = models.CharField(unique=True, blank=True, null=True)
    house = models.ForeignKey(House, models.DO_NOTHING, related_name='photos')

    class Meta:
        db_table = 'house_photo'


