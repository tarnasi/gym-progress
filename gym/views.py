from django.contrib.messages.views import SuccessMessageMixin

from .models import GymTracker

from .forms import CreateGymForm

from django.views import generic


class CreateGYMView(SuccessMessageMixin, generic.CreateView):
    model = GymTracker
    form_class = CreateGymForm
    success_url = "/"
    success_message = "New GYM was created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateGYMView, self).form_valid(form)


class DetailGYMView(generic.DetailView):
    template_name = "dashboard/gym-detail.html"
    model = GymTracker



