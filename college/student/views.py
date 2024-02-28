from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import StudentRegistrationForm

class StudentRegistrationView(FormView):
    template_name = 'generics/student/register2.html'
    form_class = StudentRegistrationForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        '''checks if form is valid'''
        password = form.cleaned_data.get('password')
        confirmpassword = form.cleaned_data.get('confirmpassword')

        if confirm_password != password:
            form.add_error('confirm_password, password do not  match')
            return self.form_invalid(form)

        form.save()
        return super().form_valid(form)
