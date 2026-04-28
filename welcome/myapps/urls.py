"""
URL configuration for welcome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from. import views

urlpatterns = [
    path('', views.selection_page, name='selection'),
    path('login/', views.login_view, name='login'),        # login page
    path('chat/', views.chat_view, name='chat'),     # chat page
    path('map/', views.map_view, name='map'),        # map page (no argument needed)
    path('logout/', views.logout_view, name='logout'),

    # NEW STAFF LOGIN
    path('staff-login/', views.staff_login, name='staff_login'),
    path('staff-chat/', views.staff_chat, name='staff_chat'),
    path('group-chat/<str:group_name>/', views.group_chat, name='group_chat'),
    path('delete-message/<str:group_name>/<int:msg_index>/', views.delete_message, name='delete_message'),
    path("share-message/<str:group_name>/<int:msg_index>/",views.share_message,name="share_message"),

    path('login/', views.student_login, name='student_login'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student-chat/', views.student_chat, name='student_chat'),
    path('student-chat/<str:group_name>/', views.student_group_chat, name='student_group_chat'),
    path('delete-student-msg/<int:index>/', views.delete_student_message, name='delete_student_message'),

    path("delete-message/<int:id>/", views.delete_message, name="delete_message"),
    path("student-result/", views.student_result, name="student_result"),
    path("results/", views.student_result, name="results"),
    path("feedback/", views.feedback, name="feedback"),
    path("timetable/", views.timetable, name="timetable"),
    path("timetable/cse_a/", views.cse_a, name="cse_a"),
    path("timetable/cse_b/", views.cse_b, name="cse_b"),
    path("timetable/cse_c/", views.cse_c, name="cse_c"),
    path("assignment_upload/",views.assignment_upload,name="assignment_upload"),
    path("assignment_history/",views.assignment_history,name="assignment_history"),
    path("certificate_upload/",views.certificate_upload,name="certificate_upload"),
    path("certificate_history/",views.certificate_history,name="certificate_history"),
    path("no_due_form/",views.no_due_form,name="no_due_form"),
    path("no_due_table/",views.no_due_table,name="no_due_table"),
    path("student_profile/",views.student_profile,name="student_profile"),
    path("student_profile_table/",views.student_profile_table,name="student_profile_table"),
    path("logout/",views.logout_view,name="logout"),
    path("office/",views.office,name="office"),
    path("office_login/",views.office_login,name="office_login"),
    path("office_chat/",views.office_chat,name="office_chat"),
    path('staff-classes/', views.staff_classes, name='staff_classes'),
    path('staff-dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('staff-certificates/', views.staff_certificates, name='staff_certificates'),
    path('select-class/', views.select_class, name='select_class'),
    path('staff-assignments/<str:section>/', views.staff_assignments, name='staff_assignments'),
    path('staff-feedback/',views.staff_feedback,name="staff_feedback"),
    path('staff-office/',views.staff_office,name="staff_office"),
    path('staff-timetable/',views.staff_timetable,name='staff_timetable'),
    path('staff-no-due/<str:class_name>/',views.staff_no_due,name="staff_no_due"),
    path('staff-no-due-select/', views.staff_no_due_select, name='staff_no_due_select'),
    path('staff-profile-verification/', views.staff_profile_verification, name='staff_profile_verification'),
    path('student-profile-verification/<str:class_name>/', views.student_profile_verification),
    path('staff-profile-select/', views.staff_profile_select, name='staff_profile_select'),
    path('staff-profile/<str:class_name>/', views.staff_profile_verification, name='staff_profile_verification'),
    path('office-students/<str:class_name>/', views.office_students, name='office_students'),
    path('office-student/<str:reg>/', views.office_student_detail, name='office_student_detail'),
    path('office-dashboard/', views.office_dashboard, name='office_dashboard'),
    path('select-class/', views.select_class, name='select_class'),
    path('student-office/', views.student_office, name='student_office'),
    path('office-student/<str:reg>/', views.office_student_detail, name='office_student_detail'),
    path('student-office-status/', views.student_office_status, name='student_office_status'),
    path('syllabus/',views.syllabus_selection,name='syllabus_selection'),
    path('syllabus/<str:subject>/',views.view_syllabus,name='view_syllabus'),
]


