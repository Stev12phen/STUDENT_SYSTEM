from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns= [
        path('', views.home, name= 'home'),
        path('register_student/', views.register_student, name='register_student'),
        path('success/', views.success, name= 'success'),
        path('login/', views.login_user, name= 'login'),
        path('logout/', views.logout_user, name= 'logout'),
        path('register/', views.register_user, name= 'register'),
        path('add_lecturer/', views.add_lecturer, name= 'add_lecturer'),
        path('view_lecturer/', views.view_lecturers, name= 'view_lecturer'),
        path('student_info/', views.student_info, name= 'student_info'),
        path('student_details/<int:student_id>/', views.Student_details, name= 'student_details'),
        path('delete_student/<int:student_id>/', views.delete_student, name= 'delete_student'),


        

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
