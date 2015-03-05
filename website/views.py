from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic.base import TemplateView
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import FormView
from django import forms

def signup(request):
    try:
        d = request.POST
        andrew_id = d.get("andrew_id")
        name = d.get("name")
        if not andrew_id:
            raise Exception("Please supply andrew id")
        if not name:
            raise Exception("Please supply name")
        subject = "D-List Request"
        message = "Andrew ID: {}\nName: {}\n".format(andrew_id, name)
        from_email = "robertmaratos@gmail.com"
        recipient_list = ["rmaratos@andrew.cmu.edu"]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return HttpResponse(andrew_id + " Successfully Added")
    except Exception as e:
        return HttpResponseBadRequest(e)


def request_submit(request):
    try:
        d = request.POST
        org = d.get("org")
        requester = d.get("requester")
        email = d.get("email")
        date = d.get("date")
        time = d.get("time")
        location = d.get("locations")
        details = d.get("details")
        subject = "Event Request - {}".format(org)
        raw_message = """\
Organization: {}\n
Requester: {}\n
Email: {}\n
Date: {}\n
Time: {}\n
Location: {}\n
Details: {}

Thank you for your event request.  Please verify the above information and
feel free to respond to this email to correct or update anything.
Expect a reply within a couple of days; if you don't hear back from us within
a reasonable period of time, feel free to follow up with another email
(we receive many emails and occasionally one will be misfiled).
"""
        message = raw_message.format(org, requester, email, date, time, location, details)
        from_email = "robertmaratos@gmail.com"
        recipient_list = ["rmaratos@andrew.cmu.edu", email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return HttpResponse(" Successfully Requested")
    except Exception as e:
        print(e)
        return HttpResponseBadRequest(str(e))


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


class FooForm(forms.Form):
    andrew_id = forms.CharField(label='Andrew ID', max_length=10)
    name = forms.CharField(label='Name', max_length=50)


class FooFormView(FormView):
    template_name = "foo.html"
    form_class = FooForm