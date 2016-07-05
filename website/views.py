import datetime

from django.views.generic.base import TemplateView
from django.conf import settings
from django.views.generic import FormView
from django import forms
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail
from captcha.fields import CaptchaField
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class RequestView(TemplateView):
    template_name = "request.html"


class MarkdownView(TemplateView):
    """
    Generic Markdown View for most static content

    Reads title of page from first line of markdown file
    Reads content from the rest
    """
    template_name = "markdown-view.html"
    markdown = None

    def get_context_data(self, **kwargs):
        context = super(MarkdownView, self).get_context_data(**kwargs)
        markdown_dir = settings.PROJECT_DIR / "templates/markdown/"
        path = str(markdown_dir / self.markdown)
        with open(path) as f:
            context['title'] = f.readline()  # Read first line for title
            context['raw_content'] = f.read()
        return context


class JoinForm(forms.Form):
    """
    Form for new member signup
    """
    andrew_id = forms.CharField(label='Andrew ID', max_length=10)
    name = forms.CharField(label='Name', max_length=50)
    if settings.CAPTCHA:
        captcha = CaptchaField()

    if settings.AUTOFILL:
        andrew_id.initial = "rmaratos"
        name.initial = "Robert Maratos"

    def clean(self):
        cleaned_data = super(JoinForm, self).clean()
        andrew_id = cleaned_data.get("andrew_id")
        # In case newbies don't know andrewid doesn't include @andrew
        if "@" in andrew_id:
            cleaned_data["email"] = andrew_id
        else:
            cleaned_data["email"] = "{}@andrew.cmu.edu".format(andrew_id)
        name = cleaned_data.get("name")
        cleaned_data["first_name"] = name.split(" ")[0]

    def send_mail(self):
        # send email using the self.cleaned_data dictionary
        subject = '[AB Tech] Subject!'
        template = get_template('email/welcome.txt')
        context = Context(self.cleaned_data)
        body = template.render(context)
        from_email = settings.FROM_EMAIL
        to_email = self.cleaned_data['email']
        send_mail(subject, body, from_email, [to_email, from_email])
        return self.cleaned_data


class RequestForm(forms.Form):
    """
    Form for event request
    """
    organization = forms.CharField(label='Organization', max_length=50)
    contact = forms.CharField(label='Event Contact Name', max_length=50)
    email = forms.EmailField(label='Event Contact Email')
    start_date = forms.DateField(label='Date', help_text="Format: mm/dd/yyyy", required=False)
    start_time = forms.CharField(label='Start Time', required=False)
    location = forms.CharField(label='Location', required=False)
    details = forms.CharField(widget=forms.Textarea, label='Details')
    if settings.CAPTCHA:
        captcha = CaptchaField()

    if settings.AUTOFILL:
        organization.initial = "Foo Organization"
        contact.initial = "First Last"
        email.initial = "rmaratos@andrew.cmu.edu"
        start_date.initial = "1/1/2017"
        start_time.initial = "7pm"
        location.initial = "Tech Room"
        details.initial = "\n".join(["blah"]*3)

    def send_mail(self):
        template = get_template('email/event.txt')
        context = Context(self.cleaned_data)
        email = template.render(context)
        subject, body = email.split("\n", 1)
        from_email = settings.FROM_EMAIL
        to_email = self.cleaned_data['email']
        send_mail(subject, body, from_email, [to_email, from_email])
        return self.cleaned_data


class JoinView(FormView):
    """
    View for joining, render join form
    """
    template_name = "join.html"
    form_class = JoinForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        cleaned_data = form.send_mail()
        template = settings.PROJECT_DIR / 'templates/joined.html'
        return render(self.request, template, cleaned_data)


class RequestView(FormView):
    """
    View for request, render request form
    """
    template_name = "request.html"
    form_class = RequestForm
    success_url = "/requested"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        cleaned_data = form.send_mail()
        template = settings.PROJECT_DIR / 'templates/requested.html'
        return render(self.request, template, cleaned_data)
