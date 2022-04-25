from django.shortcuts import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic

from gym.models import GymTracker
from .models import Program

from .forms import ProgramForm


class CreateProgramView(SuccessMessageMixin, generic.CreateView):
    model = Program
    form_class = ProgramForm
    success_message = "New GYM was created successfully"
    gym_id = None

    def form_valid(self, form):
        self.gym_id = self.kwargs['pk']
        gym = GymTracker.objects.get(pk=self.gym_id)

        form.instance.user = self.request.user
        form.instance.gym = gym
        return super(CreateProgramView, self).form_valid(form)

    def get_success_url(self):
        return reverse("GYM:detail", kwargs={"pk": self.gym_id})
