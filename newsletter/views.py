from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm


def home (request):
    title = 'Welcom, pls authenticate'
    if request.user.is_authenticated():
        title = ' Welcom, %s' %(request.user)

    #add a form
    form = SignUpForm()
    context = {
        'template_title':title,
        'form':form,
    }
    return render(request, 'newsletter/home.html', context)