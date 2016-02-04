from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
from .forms import SignUpForm, ContactForm

def base (request):
    return render (request, 'newsletter/base.html')

def home(request):
    title = 'Welcom, pls authenticate'
    if request.user.is_authenticated():
        title = ' Welcom, %s' % (request.user)

    form = SignUpForm(request.POST or None)
    context = {
        'template_title': title,
        'form': form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get('full_name')
        if not full_name:
            full_name = 'New full name'
        instance.full_name = full_name
        title = 'Thank you!'
        instance.save()
        context = {
            'template_title': title,
        }

    return render(request, 'newsletter/home.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        # sending email to yourself
        to_email = [form_email]
        contact_message = '''
        User: %s
        wanna say: %s
        via mail: %s
        ''' % (form_full_name,
               form_message,
               form_email)

        # !!!use html_message OR contact_message not both

        # some_html_message = '''
        # <h1>Hellow (htm part)</h1>
        # '''

        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  # html_message=some_html_message,
                  fail_silently=False)
    context = {
        'form': form,
    }
    return render(request, 'newsletter/forms.html', context)
