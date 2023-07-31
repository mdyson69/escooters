from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
    
def about(request):
    """Return the about.html file"""

    return render(request, 'home/about.html')

    
def contact(request):
    """Return the contact.html file"""

    return render(request, 'home/contact.html')