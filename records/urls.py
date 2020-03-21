from django.urls import path

from .views import RecordCreateView, RecordsListView, RecordDetailView, SuccessMessageTemplateView
from .views import accept_record, reject_record, close_record

urlpatterns = [
    path(
        '',
        RecordCreateView.as_view(),
        name='create-record'
    ),
    path(
        'ticket/create/',
        RecordCreateView.as_view(),
        name='create-record'
    ),
    path(
        'tickets/',
        RecordsListView.as_view(),
        name='list-records'
    ),
    path(
        'ticket/<int:pk>',
        RecordDetailView.as_view(),
        name='detail-record'
    ),
    path(
        'ticket/<int:pk>/accept/',
        accept_record,
        name='accept-record'
    ),
    path(
        'ticket/<int:pk>/reject/',
        reject_record,
        name='reject-record'
    ),
    path(
        'ticket/<int:pk>/close/',
        close_record,
        name='close-record'
    ),
    path(
        'ticket-success-message/',
        SuccessMessageTemplateView.as_view(),
        name='template-success-message'
    ),
]

