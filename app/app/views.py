from .models import Place
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from .forms import PlaceForm, RegisterForm


class PlaceListView(ListView):
    model = Place
    template_name = 'places/place_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Place.objects.all()


class PlaceDetailView(DetailView):
    model = Place
    template_name = 'places/place_list.html'

    def get_queryset(self):
        return Place.objects.all()


class PlaceCreateView(CreateView):
    model = Place
    form_class = PlaceForm
    template_name = 'places/place_form.html'


class PlaceUpdateView(UpdateView):
    model = Place
    form_class = PlaceForm
    template_name = 'places/place_form.html'
    # place = self.get_object()


class PlaceDeleteView(DeleteView):
    model = Place
    template_name = 'places/place_delete.html'


class RegisterView(CreateView):
   form_class = RegisterForm
   template_name = 'registration/register.html'

   def form_valid(self, form):
       response = super().form_valid(form)
       login(self.request, self.object)
       return response