from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView, ListView, CreateView, UpdateView, DeleteView

from cities.forms import HtmlForm, CityForm
from cities.models import City

__all__ = (
    'home', 'HomeDetailView', 'CityCreateView', 'CityUpdateView', 'CityDeleteView',
)


# class HomeView(ListView):
#     model = City
#     template_name = 'cities/home.html'
#     form = HtmlForm()
#
#     def get_context(self):
#         context =

def home(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()

    form = CityForm()
    qs = City.objects.all()
    context = {'object_list': qs, 'form': form}
    return render(request, 'cities/home.html', context=context)


class HomeDetailView(DetailView):
    model = City
    template_name = 'cities/detail.html'


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')


class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')

