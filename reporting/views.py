from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from .models import MyUser, Course, Batch, Timesheet
from . import forms
from .filters import TimeSheetFilter
from django.contrib.auth import authenticate, login, logout
from django_filters.views import FilterView
from .decorators import signin_required, user_login_role
from django.utils.decorators import method_decorator
from datetime import date


@method_decorator(signin_required, name='dispatch')
@method_decorator(user_login_role(allowed_role=['hr']), name='dispatch')
class AdminHome(TemplateView):
    template_name = 'reporting/admin_home.html'
    # def get(self, request, *args, **kwargs):
    #     return render(request, 'reporting/admin_home.html')


@method_decorator(signin_required, name='dispatch')
@method_decorator(user_login_role(allowed_role=['hr']), name='dispatch')
class AddUser(CreateView):
    model = MyUser
    template_name = 'reporting/user_add.html'
    form_class = forms.UserRegistrationForm
    success_url = reverse_lazy("adminhome")

    # context = {}
    #
    # def get(self, request, *args, **kwargs):
    #     form = self.form_name
    #     self.context['form'] = form
    #     return render(request, self.template_name, self.context)
    #
    # def post(self, request, *args, **kwargs):
    #     form = self.form_name(request.POST)
    #     self.context['form'] = form
    #     if form.is_valid():
    #         form.save()
    #         return redirect('adminhome')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = self.model.objects.all()
        return context


@method_decorator(signin_required, name='dispatch')
@method_decorator(user_login_role(allowed_role=['hr']), name='dispatch')
class AddCourse(CreateView):
    # model = Course
    # template_name = 'reporting/add_course.html'
    # form_name = forms.CourseAddForm
    # context = {}
    #
    # def get(self, request, *args, **kwargs):
    #     form = self.form_name
    #     self.context['form'] = form
    #     return render(request, self.template_name, self.context)
    #
    # def post(self, request, *args, **kwargs):
    #     form = self.form_name(request.POST)
    #     self.context['form'] = form
    #     if form.is_valid():
    #         form.save()
    #         return redirect('adminhome')
    model = Course
    template_name = 'reporting/add_course.html'
    form_class = forms.CourseAddForm
    success_url = reverse_lazy('adminhome')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = self.model.objects.all()
        return context


@method_decorator(signin_required, name='dispatch')
@method_decorator(user_login_role(allowed_role=['hr']), name='dispatch')
class AddBatch(CreateView):
    model = Batch
    template_name = 'reporting/add_batch.html'
    form_class = forms.BatchAddForm
    success_url = reverse_lazy('adminhome')

    # context = {}

    # def get(self, request, *args, **kwargs):
    #     form = self.form_name
    #     self.context['form'] = form
    #     return render(request, self.template_name, self.context)
    #
    # def post(self, request, *args, **kwargs):
    #     form = self.form_name(request.POST)
    #     self.context['form'] = form
    #     if form.is_valid():
    #         form.save()
    #         return redirect('adminhome')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['batches'] = self.model.objects.all()
        return context


# Create your views here.


class ListAllUser(ListView):
    model = MyUser
    template_name = 'reporting/list_user.html'


class ListAllCourses(ListView):
    model = Course
    template_name = 'reporting/list_course.html'


class ListAllBatch(ListView):
    model = Batch
    template_name = 'reporting/list_batch.html'


@method_decorator(signin_required, name='dispatch')
@method_decorator(user_login_role(allowed_role=['hr']), name='dispatch')
class UserEdit(UpdateView):
    model = MyUser
    form_class = forms.UserEditForm
    template_name = 'reporting/user_edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('userlist')


@method_decorator(signin_required, name='dispatch')
@method_decorator(user_login_role(allowed_role=['hr']), name='dispatch')
class CourseEdit(UpdateView):
    model = Course
    form_class = forms.CourseAddForm
    template_name = 'reporting/edit_course.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listcourse')


@method_decorator(signin_required, name='dispatch')
@method_decorator(user_login_role(allowed_role=['hr']), name='dispatch')
class BatchEdit(UpdateView):
    model = Batch
    form_class = forms.BatchAddForm
    template_name = 'reporting/edit_batch.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listbatch')


class Signin(TemplateView):
    template_name = 'reporting/user_signup.html'
    form_class = forms.LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if request.user.is_admin:
                    return redirect('adminhome')
                else:
                    return redirect('userhome')


class Signout(TemplateView):

    def get(self, request):
        logout(request)
        return redirect('signin')


@method_decorator(signin_required, name='dispatch')
@method_decorator(user_login_role(allowed_role=['faculty']), name='dispatch')
class UserHome(TemplateView):
    template_name = 'reporting/userhome.html'


@method_decorator(signin_required, name='dispatch')
@method_decorator(user_login_role(allowed_role=['faculty']), name='dispatch')
class AddTimeSheet(CreateView):
    model = Timesheet
    template_name = 'reporting/timesheet.html'
    form_class = forms.TimeSheduleForm
    context = {}

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            timesheet = form.save(commit=False)
            timesheet.user = request.user
            timesheet.save()
            return redirect('userhome')
        else:
            self.context = {'form': form}

            return render(request, self.template_name, self.context)


tdate = date.today()


@method_decorator(signin_required, name='dispatch')
@method_decorator(user_login_role(allowed_role=['faculty']), name='dispatch')
class ListTimeSheet(FilterView):
    model = Timesheet
    template_name = 'reporting/list_timesheet.html'
    context_object_name = 'timesheet'
    filterset_class = TimeSheetFilter

    def get_queryset(self):
        if self.request.user.is_admin:
            queryset = self.model.objects.all()
        else:
            queryset = self.model.objects.filter(user=self.request.user, verified=False, date=tdate)
        return queryset


@method_decorator(signin_required, name='dispatch')
@method_decorator(user_login_role(allowed_role=['faculty']), name='dispatch')
class EditTimeSheetView(UpdateView):
    model = Timesheet
    template_name = 'reporting/edittimesheet.html'
    form_class = forms.TimeSheduleChangeForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listtimesheet')


@method_decorator(signin_required, name='dispatch')
@method_decorator(user_login_role(allowed_role=['hr']), name='dispatch')
class Progress(TemplateView):
    model = Timesheet
    # template_name = 'reporting/changestatus.html'
    # form_class = forms.SheduleChangeForm
    pk_url_kwarg = 'id'

    # success_url = reverse_lazy('listtimesheet')

    def get(self, request, *args, **kwargs):
        timesheet = self.model.objects.get(id=kwargs['id'])
        timesheet.verified = True
        timesheet.save()
        return redirect('listtimesheet')
