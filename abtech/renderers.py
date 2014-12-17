from django_medusa.renderers import StaticSiteRenderer
from django.core.urlresolvers import reverse
from website import urls


class HomeRenderer(StaticSiteRenderer):
    def get_paths(self):
        paths = []
        for url in urls.urlpatterns:
            name = "website:{}".format(url.name)
            paths.append(reverse(name))
        print("PATHS", paths)
        return paths

renderers = [HomeRenderer, ]