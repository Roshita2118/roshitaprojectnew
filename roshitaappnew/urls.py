from django.urls import path
#now import the views.py file into this code

from django.contrib import admin
from django.urls import path
from roshitaappnew import views
from django.contrib import admin
#from myapp.views import MyView
from .views import GeeksCreate

urlpatterns=[
            #path('admin/', admin.site.urls),
            #path('',views.index),
            #path('', views.geeks_view),
            #path('n', views.create_view),
            #path('about/', MyView.as_view()),
            path('', GeeksCreate.as_view()),
            #path('<id>/delete/',views.delete_view,name="delete_view"),
            #path('form/',views.list_view, name="list_view"),
    ]
# importing views from views..py
from .views import detail_view

#urlpatterns = [
    #path('<id>', detail_view),
       #path('<id>/update/',views.update_view,name="update_view"),
#]