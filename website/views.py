from django.views.generic.base import TemplateView
from django.conf import settings
from django.views.generic import FormView
from django import forms
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail


class RequestView(TemplateView):
    template_name = "request.html"


class MarkdownView(TemplateView):

    template_name = "markdown-view.html"
    markdown = None

    def get_context_data(self, **kwargs):
        context = super(MarkdownView, self).get_context_data(**kwargs)
        markdown_dir = settings.PROJECT_DIR / "templates/markdown/"
        path = str(markdown_dir / self.markdown)
        with open(path) as f:
            context['title'] = f.readline()
            context['raw_content'] = f.read()
        return context


class JoinForm(forms.Form):
    andrew_id = forms.CharField(label='Andrew ID', max_length=10)
    name = forms.CharField(label='Name', max_length=50)

    def clean(self):
        cleaned_data = super(JoinForm, self).clean()
        andrew_id = cleaned_data.get("andrew_id")
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
        from_email = 'abtech@andrew.cmu.edu'
        to_email = self.cleaned_data['email']
        send_mail(subject, body, from_email, [to_email])


class RequestForm(forms.Form):
    organization = forms.CharField(label='Organization', max_length=50)
    requester = forms.CharField(label='Requester', max_length=50)
    email = forms.EmailField(label='Email')
    date = forms.DateField(label='Date')
    start_time = forms.TimeField(label='Start Time')
    location = forms.CharField(label='Location')
    details = forms.CharField(widget=forms.Textarea, label='Details')

    def send_mail(self):
        template = get_template('email/event.txt')
        context = Context(self.cleaned_data)
        subject = "[AB Tech] Event Request"
        body = template.render(context)
        from_email = 'abtech@andrew.cmu.edu'
        to_email = self.cleaned_data['email']
        send_mail(subject, body, from_email, [to_email])


class JoinView(FormView):
    template_name = "join.html"
    form_class = JoinForm
    success_url = "/joined"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_mail()
        return super(JoinView, self).form_valid(form)


class RequestView(FormView):
    template_name = "request.html"
    form_class = RequestForm
    success_url = "/requested"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_mail()
        return super(RequestView, self).form_valid(form)
