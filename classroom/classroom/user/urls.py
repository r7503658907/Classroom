from django.urls import path
from . import views
urlpatterns = [
    #student
    path('postStudentDetailData/', views.postStudentDetailData.as_view()),
    path('getStudentDetail/', views.getStudentDetail.as_view()),
    path('getStudentDetail/<studentId>/', views.getStudentDetailId.as_view()),

    # parents
    path('postParentsDetail/', views.postParentsDetail.as_view()),
    path('getParentsDetail/', views.getParentsDetail.as_view()),
    path('getParentsDetailId/<studentId_id>/', views.getParentsDetailId.as_view()),

]