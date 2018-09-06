"""Django Forms for abtech.org."""

from captcha.fields import CaptchaField

from django import forms
from django.core.mail import send_mail, EmailMessage, make_msgid
from django.conf import settings
from django.template.loader import get_template

from website import tracker


class JoinForm(forms.Form):
    """Form for email list signup."""

    andrew_id = forms.CharField(label='Andrew ID', max_length=10)
    name = forms.CharField(label='Name', max_length=50)

    if settings.CAPTCHA:
        captcha = CaptchaField()

    if settings.AUTOFILL:
        andrew_id.initial = "rmaratos"
        name.initial = "Robert Maratos"

    def clean(self):
        """Clean form data to pass to mailer."""
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
        """Send email using the cleaned_data dictionary."""
        template = get_template('email/welcome.txt')
        context = self.cleaned_data
        email = template.render(context)
        subject, body = email.split("\n", 1)
        from_email = settings.JOIN_EMAIL
        to_email = self.cleaned_data['email']
        send_mail(subject, body, from_email, [to_email, from_email])
        return self.cleaned_data


class RequestForm(forms.Form):
    """Form for event request."""

    event_name = forms.CharField(label='Event Name', max_length=50)
    organization = forms.CharField(label='Organization', max_length=75)
    contact = forms.CharField(label='Event Contact Name', max_length=50)
    email = forms.EmailField(label='Event Contact Email')
    start_date = forms.DateField(label='Start Date', help_text="Format: mm/dd/yyyy")
    start_time = forms.CharField(label='Start Time', required=False)
    end_date = forms.DateField(label='End Date', help_text="Format: mm/dd/yyyy")
    end_time = forms.CharField(label='End Time', required=False)
    location = forms.CharField(label='Location', required=False)
    details = forms.CharField(widget=forms.Textarea, label='Details')

    if settings.CAPTCHA:
        captcha = CaptchaField()

    if settings.AUTOFILL:
        event_name.initial = "Event Name"
        organization.initial = "Foo Organization"
        contact.initial = "First Last"
        email.initial = "rmaratos@andrew.cmu.edu"
        start_date.initial = "1/1/2017"
        start_time.initial = "7pm"
        end_date.initial = "1/1/2017"
        end_time.initial = "8pm"
        location.initial = "Tech Room"
        details.initial = "\n".join(["blah"]*3)

    def tracker_event(self, context):
        template = get_template('email/tracker_event.txt')
        description = template.render(context)
        event_id = tracker.Tracker().create_event(context, description)
        return event_id

    def send_mail(self):
        """Send event request email generated using form data."""
        template = get_template('email/event.txt')
        context = self.cleaned_data
        email = template.render(context)
        subject, body = email.split("\n", 1)
        from_email = settings.EVENT_EMAIL
        to_email = self.cleaned_data['email']

        message_id = make_msgid()
        email = EmailMessage(subject, body, from_email, [to_email, from_email],
                    headers={'Message-ID': message_id}
        )
        email.send()


        event_url = self.tracker_event(context)
        tracker_email = EmailMessage(subject, event_url, from_email, [from_email],
            headers={'In-Reply-To': message_id})
        tracker_email.send()
        return self.cleaned_data
