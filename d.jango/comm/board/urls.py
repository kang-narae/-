from . import views
from django.urls import include, path

app_name='board'
urlpatterns = [
    path('blist/', views.blist,name='blist'),
    path('bwrite/', views.bwrite,name='bwrite'),
    path('bwriteOk/', views.bwriteOk,name='bwriteOk'),
    path('<str:b_no>/bview/', views.bview,name='bview'),
    path('<str:b_no>/bmodify/', views.bmodify,name='bmodify'),
    path('bmodifyOk/', views.bmodifyOk,name='bmodifyOk'),
    path('<str:b_no>/bdelete/', views.bdelete,name='bdelete'),
    path('<str:b_no>/breply/', views.breply,name='breply'),
    path('breplyOk/', views.breplyOk,name='breplyOk'),
    path('publicData/', views.publicData,name='publicData'),
    path('publicData2/', views.publicData2,name='publicData2'),
]