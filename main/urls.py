from django.urls import path
from .views import index_view,meeting_detail_view,meetings_view

urlpatterns = [
    path('', index_view, name='index'),
    path('meetings/', meetings_view, name='meetings'),
    path('meetings/<int:meeting_id>/', meeting_detail_view, name='meeting_detail'),
]
