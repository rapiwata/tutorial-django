from django.urls import path
from money_tracker.views import show_tracker
from money_tracker.views import create_transaction
from money_tracker.views import show_xml 


app_name = 'money_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('xml/', show_xml, name='show_xml'),
    path('create', create_transaction, name='create_transaction'),


]

