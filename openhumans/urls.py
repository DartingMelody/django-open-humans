from django.conf.urls import url
from . import views

app_name = 'openhumans'
urlpatterns = [
    url(r'^delete_connection/?$',
        views.DeleteConnection.as_view(), name='delete_connection'),

]