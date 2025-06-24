from django.shortcuts import render
# Create your views here.


def index(request):
    """
    Render the index page for the meetups app.
    """

    meetups = [
        {
            'title': 'Django Meetup',
            'date': '2023-10-01',
            'location': 'New York',
            'description': 'A meetup for Django enthusiasts to share knowledge and network.',
        },
        {
            'title': 'Python Conference',
            'date': '2023-11-15',
            'location': 'San Francisco',
            'description': 'An annual conference for Python developers to discuss the latest trends and technologies.',
        }
    ]
    return render(request, 'meetups/index.html', {'meetups': meetups})

def meetup_detail(request):
    pass