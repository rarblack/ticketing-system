from django.urls import path

from .views import CategoriesListView

urlpatterns = [
    path('', CategoriesListView.as_view(), name='list-categories'),
]
