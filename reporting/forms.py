from django import forms
from django.forms import ModelForm
from .admin import UserCreationForm
from .models import MyUser, Course, Batch, Timesheet
from datetime import date


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = MyUser
        fields = ['email', 'role', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}),
            'role': forms.Select(attrs={'class': 'form-select'}),

        }


class UserEditForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = MyUser
        fields = ['email', 'role']
        exclude = ['password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
        }


class CourseAddForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_name']
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'})
        }


class BatchAddForm(ModelForm):
    class Meta:
        model = Batch
        fields = ['courses', 'batch_name']
        widgets = {
            'courses': forms.Select(attrs={'class': 'form-select'}),
            'batch_name': forms.TextInput(attrs={'class': 'form-control'})
        }


class LoginForm(forms.Form):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


tdate = date.today()


class TimeSheduleForm(ModelForm):
    class Meta:
        model = Timesheet
        fields = ['batch', 'topic']
        widgets = {
            'batch': forms.Select(attrs={'class': 'form-select'}),
            'topic': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        clean_data = super().clean()
        topic = clean_data.get('topic')
        topics = Timesheet.objects.filter(topic=topic, date=tdate)
        topicdate = Timesheet.objects.filter(date=tdate)
        # print(topicdate[0].date)
        if topics:
            if len(topicdate) != 0:
                if topicdate[0].date == tdate:
                    msg = "created today"
                    self.add_error('topic', msg)


class TimeSheduleChangeForm(ModelForm):
    class Meta:
        model = Timesheet
        fields = ['topic', 'topic_status']
        widgets = {
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'topic_status': forms.Select(attrs={'class': 'form-select'}),
        }