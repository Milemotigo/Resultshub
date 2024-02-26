from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import StudentRegistrationForm

class StudentRegistrationView(FormView):
    template_name = 'generics/student/register.html'
    form_class = StudentRegistrationForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        '''checks if form is valid'''
        form.save()
        return super().form_valid(form)
