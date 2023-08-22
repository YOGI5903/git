from django.urls import path
from . import views
urlpatterns=[
	path("hw/",views.index,name='index'),
	path("np/",views.index1,name='index1'),
	path("para/",views.htmlexample,name='htmlexample'),
    path("submit/",views.adoption_form),
    path('form/',views.form)
]