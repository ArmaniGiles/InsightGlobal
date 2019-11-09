from django import forms
from django.contrib.auth.models import User, Group
from .models import Zipcode

import django_filters


class UserFilter(django_filters.FilterSet):
    JURISDICTION_NAME = django_filters.CharFilter(lookup_expr='icontains')
    # groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Zipcode
        fields = ['JURISDICTION_NAME', 'COUNT_FEMALE', 'COUNT_MALE',  ]
