from django.views.generic.base import TemplateView
from django.conf import settings
from django.views.generic import FormView
from django import forms
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail
from captcha.fields import CaptchaField

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
            context['DEBUG'] = settings.DEBUG
        return context


class JoinForm(forms.Form):
    """
    Form for new member signup
    """
    andrew_id = forms.CharField(label='Andrew ID', max_length=10)
    name = forms.CharField(label='Name', max_length=50)
    captcha = CaptchaField()

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
        send_mail(subject, body, from_email, [to_email])


class RequestForm(forms.Form):
    """
    Form for event request
    """
    organization = forms.CharField(label='Organization', max_length=50)
    contact = forms.CharField(label='Event Contact', max_length=50)
    email = forms.EmailField(label='Email')
    start_date = forms.DateField(label='Date', help_text="Format: mm/dd/yyyy", required=False)
    start_time = forms.CharField(label='Start Time', required=False)
    location = forms.CharField(label='Location', required=False)
    details = forms.CharField(widget=forms.Textarea, label='Details')
    captcha = CaptchaField()

    def send_mail(self):
        template = get_template('email/event.txt')
        context = Context(self.cleaned_data)
        email = template.render(context)
        subject, body = email.split("\n", 1)
        from_email = settings.FROM_EMAIL
        to_email = self.cleaned_data['email']
        send_mail(subject, body, from_email, [to_email])


class JoinView(FormView):
    """
    View for joining, render join form
    """
    template_name = "join.html"
    form_class = JoinForm
    success_url = "/joined"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_mail()
        return super(JoinView, self).form_valid(form)


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
        form.send_mail()
        return super(RequestView, self).form_valid(form)
