from random import randint

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from online_store.settings import EMAIL_HOST_USER
from userextend.forms import UserForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.username = (
                f'{new_user.first_name[0].lower()}'
                f'{new_user.last_name.lower().replace(" ", "")}'
                f'_{randint(100000, 999999)}'
            )
            new_user.save()

            subject = 'New account'
            message = f'Congratulations! Your username is: {new_user.username}'
            send_mail(subject, message, EMAIL_HOST_USER, [new_user.email])

        return redirect('login')
