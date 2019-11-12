from .models import Zipcode
import django_filters


class ZipCodeFilter(django_filters.FilterSet):
    JURISDICTION_NAME = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Zipcode
        fields = ['JURISDICTION_NAME', 'COUNT_FEMALE', 'COUNT_MALE',  ]
