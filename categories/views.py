from django.views import generic
from django.contrib.auth import mixins
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Category

from bases.models import Navbar, Footer


class CategoriesListView(mixins.LoginRequiredMixin, generic.ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'categories/list/categories_list.html'

    def get_queryset(self):
        return self.model.objects.filter(
            department=self.request.user.department
        )

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super(CategoriesListView, self).get_context_data(**kwargs)

        context['navbar'] = Navbar.objects.filter(
            department=self.request.user.department
        ).first()

        context['footer'] = Footer.objects.filter(
            department=self.request.user.department
        ).first()

        return context

