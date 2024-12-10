
from django.urls import path

from . import views

    



app_name = 'blog'


urlpatterns=[

path('',views.show_post,name='namayeshpost'),
path('detail/<int:id>/',views.detail_post,name='detail'),
# path('detail/<int:pk>',views.detail_post,name='detail'),

path('new_post',views.new_post,name='new_post'),

]