"""Django View Classes for abtech.org."""

from website import forms
from django.conf import settings
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic.base import TemplateView


class MarkdownView(TemplateView):
    """
    Generic Markdown View for most static content.

    Reads title of page from first line of markdown file and the page content
    from the rest of the file.
    """

    template_name = "markdown-view.html"
    markdown = None

    def get_context_data(self, **kwargs):
        """Fill content from markdown template."""
        context = super(MarkdownView, self).get_context_data(**kwargs)
        markdown_dir = settings.PROJECT_DIR / "templates/markdown/"
        path = str(markdown_dir / self.markdown)
        with open(path) as content:
            context['title'] = content.readline()  # Read first line for title
            context['raw_content'] = content.read()
        return context


class JoinView(FormView):
    """View for join page containing the JoinForm."""

    template_name = "join.html"
    form_class = forms.JoinForm

    def form_valid(self, form):
        """Called when valid form data has been POSTed."""
        cleaned_data = form.send_mail()
        template = settings.PROJECT_DIR / 'templates/joined.html'
        return render(self.request, template, cleaned_data)


class RequestView(FormView):
    """View for event request page containing the RequestForm."""

    template_name = "request.html"
    form_class = forms.RequestForm

    def form_valid(self, form):
        """Called when valid form data has been POSTed."""
        cleaned_data = form.send_mail()
        template = settings.PROJECT_DIR / 'templates/requested.html'
        return render(self.request, template, cleaned_data)
