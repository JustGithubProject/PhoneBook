from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, ListView

from .forms import CreatePersonForm
from .models import Phone, Person


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['persons'] = Person.objects.all()
        return context


class AddPhoneFormView(CreateView):
    template_name = "add_person.html"
    form_class = CreatePersonForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        phone_numbers = self.request.POST.get('phones')
        for phone_number in phone_numbers.split('\n'):
            Phone.objects.create(phone=phone_number, contact=self.object)

        return super().get_success_url()


class DeletePhoneView(DeleteView):
    model = Person
    template_name = "delete_person.html"
    success_url = reverse_lazy('home')


class Search(ListView):
    template_name = "search.html"
    context_object_name = "numbers"

    def get_queryset(self):
        return Phone.objects.filter(contact__name__icontains=self.request.GET.get('q')).select_related("contact")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
