from rest_framework import serializers
from django.contrib.auth import get_user, get_user_model

from utils import set_byn

from .models import *

from django.conf import settings
class MarketplaceValue(serializers.RelatedField):
    def to_internal_value(self, data):
        marketplace = Marketplace.objects.get(id=data)
        return marketplace.name
    def to_representation(self, value):
        name = value.name
        return name


class PhotosValue(serializers.RelatedField):
    def to_representation(self, value):
        string = value.image
        return string

            
'''class HouseViewSetSerializer(serializers.ModelSerializer):
    marketplace = MarketplaceValue(read_only=True)
    #photos = serializers.StringRelatedField(source="photos.first.image")
    photos = PhotosValue(many=True, read_only=True)
    
    def create(self, validated_data):
        validated_data['marketplace_id'] = 6
        return House.objects.create(**validated_data)
    class Meta:
        model = House
        fields = [
            'id', 'amountusd', 'amountbyn', 'rent_rooms',
            'address', 'created_at', 'agency', 'description',
            'marketplace', 'photos', 'location_a', "location_b"
        ]
'''

def url_check():
    pass

CHECK_LIST = ['kufar', 'onliner', 'realt','neagent', 'domovita', 'activecloud']

class HousePhotoSerializers(serializers.ModelSerializer):
    def to_representation(self, value):
        value = str(HousePhoto.objects.get(id=value.id).image)
                
        if 'kufar' in value or 'onliner' in value or 'realt' in value or 'neagent' in value or 'domovita' in value or 'activecloud' in value:
            return f'{value}'
        else:
            return f'{settings.MEDIA_URL}{value}'

    class Meta:
        model = HousePhoto
        fields = ['image',]
        
        
class HouseSerializer(serializers.ModelSerializer):
    marketplace = MarketplaceValue(queryset=Marketplace.objects.all(), required=False)
    #photos = PhotosValue(many=True)
    photos = HousePhotoSerializers(many=True, read_only=True)
    uploaded_photos = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )
    #user = serializers.RelatedField(many=False, queryset=get_user_model().objects.all())

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_photos")
        validated_data.pop("marketplace")
        #marketplace_id = validated_data.pop("marketplace_id")
        user = self.context['request'].user
        validated_data.setdefault("user", user)
        amountbyn = set_byn(validated_data['amountusd'])
        marketplace = Marketplace.objects.get(name='easyflat')
        house = House.objects.create(amountbyn=amountbyn, marketplace=marketplace, phoneNumber=user.phoneNumber, **validated_data)
        #print(validated_data)

        for image in uploaded_images:
            HousePhoto.objects.create(house=house, image=image)
            
        return house
    
    class Meta:
        model = House
        fields = "__all__"

        


