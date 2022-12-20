from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import Phone
from .forms import CreatePersonForm


class HomePageView(TemplateView):
    template_name = "home.html"


class AddPhoneFormView(CreateView):
    template_name = "add_person.html"
    form_class = CreatePersonForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        phone_numbers = self.request.POST.get('phones')
        for phone_number in phone_numbers.split('\n'):
            Phone.objects.create(phone=phone_number, contact=self.object)

        return super().get_success_url()
