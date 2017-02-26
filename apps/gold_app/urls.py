from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^process$', views.process, name='gold_process'),
	url(r'^reset$', views.reset, name='gold_reset'),
    url(r'^', views.index, name='gold_index'),
]
