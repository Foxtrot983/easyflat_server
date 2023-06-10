from rest_framework import serializers

from .models import *

class MarketplaceValue(serializers.RelatedField):
    def to_representation(self, value):
        name = value.name
        return name


class PhotosValue(serializers.RelatedField):
    def to_representation(self, value):
        string = value.image
        return string

            
class HouseViewSetSerializer(serializers.ModelSerializer):
    marketplace = MarketplaceValue(read_only=True)
    #photos = serializers.StringRelatedField(source="photos.first.image")
    photos = PhotosValue(many=True, read_only=True)
    class Meta:
        model = House
        fields = [
            'id', 'amountusd', 'amountbyn', 'rent_rooms',
            'address', 'created_at', 'agency', 'description',
            'marketplace', 'photos'
        ]

        
class HouseDetailSerializer(serializers.ModelSerializer):
    marketplace = MarketplaceValue(read_only=True)
    photos = PhotosValue(many=True, read_only=True)
    
    '''def to_representation(self, value):
        value = House.objects.get()
        return value.marketplace.name'''
    
    class Meta:
        model = House
        fields = [
            'id', 'amountusd', 'amountbyn', 'rent_rooms', 'address',
            'url', 'created_at', 'agency', 'description', 'marketplace', 
            'location_a', 'location_b', 'phoneNumber', 'photos'
        ]