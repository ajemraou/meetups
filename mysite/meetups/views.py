from django.shortcuts import render, redirect
from .models import Meetup
from .forms import RegistrationForm
# Create your views here.


def index(request):
    """
    Render the index page for the meetups app.
    """
    # meetups_object = {
    #     'meetups': [
    #         {
    #             'title': 'Django Meetup',
    #             'description': 'A meetup for Django enthusiasts.',
    #             'date': '2023-10-01',
    #             'location': 'Online',
    #             'slug': 'django-meetup',
    #         },
    #         {
    #             'title': 'Python Meetup',
    #             'description': 'A meetup for Python developers.',
    #             'date': '2023-10-15',
    #             'location': 'Online',
    #             'slug': 'python-meetup',
    #         },
    #     ]
    # }
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {'meetups': meetups})

def meetup_detail(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant = registration_form.save()
                selected_meetup.Participant.add(participant)
                return redirect('registration_success')

        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup': selected_meetup,
            'form': registration_form
        })

    except Exception as e:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False,
        })

def confirm_registration(request):
    return render(request, 'meetups/registration-success.html')