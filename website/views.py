from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic.base import TemplateView
from django.core.mail import send_mail
from django.conf import settings



def signup(request):
    try:
        d = request.POST
        andrew_id = d.get("andrew_id")
        name = d.get("name")
        subject = "D-List Request"
        message = "Andrew ID: {}\nName: {}\n".format(andrew_id, name)
        from_email = "robertmaratos@gmail.com"
        recipient_list = ["rmaratos@andrew.cmu.edu"]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return HttpResponse(andrew_id + " Successfully Added")
    except Exception as e:
        return HttpResponseBadRequest(e)


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
            context['raw_content'] = f.read()
        return context