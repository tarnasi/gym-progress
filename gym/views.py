from django.shortcuts import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic

from .models import GymTracker

from .forms import CreateGymForm, UpdateGymForm
from program.forms import ProgramForm


class DetailGYMView(generic.edit.FormMixin, generic.DetailView):
    template_name = "dashboard/gym-detail.html"
    model = GymTracker
    form_class = UpdateGymForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form_values = {
            "gym_name": self.object.gym_name,
            "start_at": self.object.start_at,
            "end_at": self.object.end_at,
            "exercise_in_week": self.object.exercise_in_week,
            "exercise_in_day": self.object.exercise_in_day,
        }
        context['form'] = UpdateGymForm(initial=form_values)
        context['program_form'] = ProgramForm()
        return context


class CreateGYMView(SuccessMessageMixin, generic.CreateView):
    model = GymTracker
    form_class = CreateGymForm
    success_url = "/"
    success_message = "New GYM was created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateGYMView, self).form_valid(form)


class UpdateGYMView(SuccessMessageMixin, generic.UpdateView):
    model = GymTracker
    form_class = UpdateGymForm
    success_message = "GYM was updated successfully"

    def get_success_url(self):
        return reverse('GYM:detail', kwargs={'pk': self.object.id})

