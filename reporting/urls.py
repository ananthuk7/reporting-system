from django.urls import path
from . import views

urlpatterns = [
    path('', views.Signin.as_view(), name='signin'),
    path('home', views.AdminHome.as_view(), name='adminhome'),
    path('adduser', views.AddUser.as_view(), name='adduser'),
    path('addcourse', views.AddCourse.as_view(), name='addcourse'),
    path('addbatch', views.AddBatch.as_view(), name='addbatch'),
    # path('listuser', views.ListAllUser.as_view(), name='listuser'),
    # path('listcourse', views.ListAllCourses.as_view(), name='listcourse'),
    # path('listbatch', views.ListAllBatch.as_view(), name='listbatch'),
    path('edituser/change/<int:id>', views.UserEdit.as_view(), name='edituser'),
    path('editcourse/change/<int:id>', views.CourseEdit.as_view(), name='editcourse'),
    path('editbatch/change/<int:id>', views.BatchEdit.as_view(), name='editbatch'),

    path('signout', views.Signout.as_view(), name='signout'),
    path('user/home', views.UserHome.as_view(), name='userhome'),
    path('user/timesheet', views.AddTimeSheet.as_view(), name='timesheet'),
    path('user/listtimesheet', views.ListTimeSheet.as_view(), name='listtimesheet'),
    path('user/listtimesheets/<int:id>', views.EditTimeSheetView.as_view(), name='editsheet'),
    path('user/change/<int:id>', views.Progress.as_view(), name='changestatus'),

]
