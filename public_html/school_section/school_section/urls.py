from django.contrib import admin
from django.urls import path, include
from app_1.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('ilovekatyfrommoscow/', admin.site.urls),
    path('', include('app_1.urls')),
    path('projects/', project, name='project'),
    path('clean/', clean, name='clean'),
    path('speed_read/', speed_read, name='speed_read'),
    path('registration/', RegistrationCreateView.as_view(), name='add'),
    path('text/<str:name_text>/', text),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(template_name='app_1/shedule.html'), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('error/', er, name='error'),
    path('diary/', diary_user, name='diary'),
    path('diary_rewrite/', diary_rewrite, name='diary_rewrite'),
    path('kind_of_studing/', kind_of_studing, name='kind_of_studing'),
    path('accounts/profile/change/', update_profile, name='profile_change'),
    path('timerobots/', TimetableRobots, name='TimetableRobots'),
    path('usefulresources/', UsefullResources, name='UsefullResources'),
    path('awards/', awards, name='awards'),
    path('shop/', shop, name='shop'),

]



