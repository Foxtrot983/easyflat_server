from django_filters import rest_framework as filters
from .models import House

RENT_CHOICE = (
    (0, 'комната'),
    (1, 'однушка'),
    (2, "двушка"),
    (3, "трешка"),
    (4, "четырёшка"),
)

MARKETPLACE_CHOICE = (
    (1, 'Onliner.by'),
    (2, 'Kufar.by'),
    (3, "Realt.by"),
    (4, "Neagent.by"),
    (5, "Домовита"),
)


class HouseFilter(filters.FilterSet):
    amountbyn = filters.RangeFilter()
    rent_rooms = filters.ChoiceFilter(choices=RENT_CHOICE)
    address = filters.CharFilter(field_name='address', lookup_expr='icontains')
    agency = filters.BooleanFilter()
    marketplace = filters.ChoiceFilter(choices=MARKETPLACE_CHOICE)
    location_a = filters.NumericRangeFilter(field_name='location_a', lookup_expr='range')
    location_b = filters.NumericRangeFilter(field_name='location_b', lookup_expr='range')
    
    o = filters.OrderingFilter(
        fields=(
            ("created_at", 'Дата создания'),
        ),
        field_labels={
            'created_at': 'Дата создания',
        }

    )
    
    class Meta:
        model = House
        fields = ['o', "amountbyn", "rent_rooms", 'address', 'agency' ,'marketplace' ,'location_a' ,'location_b']