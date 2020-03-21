from django.views import generic
from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.forms.models import modelform_factory, ModelForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, get_list_or_404

from categories.models import Category
from .models import Record
from bases.models import Navbar, Footer


class RecordCreateView(generic.CreateView):
    model = Record
    template_name = 'records/create/create-record.html'
    success_url = reverse_lazy('records:template-success-message')

    def get_form_class(self):
        return modelform_factory(
            self.model,
            form=ModelForm,
            exclude=[
                "status",
                "created_by",
                "created_at"
            ]
        )

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = "pend"
        self.object.created_by = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['navbar'] = Navbar.objects.get(
            type="unauthorized"
        )
        context['footer'] = Footer.objects.get(
            type="unauthorized"
        )
        return context


class RecordsListView(mixins.LoginRequiredMixin, generic.ListView):
    model = Record
    context_object_name = 'records'
    template_name = 'records/list/list-records.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.filter(
            department=self.request.user.department
        )

        context['navbar'] = Navbar.objects.filter(
            type="authorized"
        ).first()

        context['footer'] = Footer.objects.filter(
            type="authorized"
        ).first()

        return context


class SuccessMessageTemplateView(generic.TemplateView):
    template_name = 'records/template/template-success-message.html'


class RecordDetailView(mixins.LoginRequiredMixin, generic.DetailView):
    model = Record
    template_name = 'records/detail/detail-record.html'
    temp_object_name = 'record'


def accept_record(request, pk):
    record = Record.objects.get(pk=pk)
    record.status = "accept"
    record.save()
    return redirect('records:list-records')


def reject_record(request, pk):
    record = Record.objects.get(pk=pk)
    record.status = "reject"
    record.save()
    return redirect('records:list-records')


def close_record(request, pk):
    record = Record.objects.get(pk=pk)
    record.status = "close"
    record.save()
    return redirect('records:list-records')

