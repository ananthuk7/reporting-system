import django_filters
from .models import Timesheet, MyUser, Batch
from .models import MyUser
from django import forms


class TimeSheetFilter(django_filters.FilterSet):
    user = django_filters.ModelChoiceFilter(queryset=MyUser.objects.all(),
                                            widget=forms.Select(attrs={'class': 'form-select w-25'}))
    batch = django_filters.ModelChoiceFilter(queryset=Batch.objects.all(),
                                             widget=forms.Select(attrs={'class': 'form-select w-25'}))
    date = django_filters.DateFilter(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Timesheet
        fields = ['date', 'batch', 'user']
