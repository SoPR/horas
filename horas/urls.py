from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = [
    path("api/v1/", include("apps.sso.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("search/", include("apps.search.urls")),
    path("stats/", include("apps.stats.urls")),
    path("legal/", TemplateView.as_view(template_name="legal.html"), name="legal"),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
    path(
        "contact/", TemplateView.as_view(template_name="contact.html"), name="contact"
    ),
    path("<str:username>/", include("apps.profiles.urls")),
    path("<str:username>/meetings/", include("apps.meetings.urls")),
    path("", include("apps.core.urls")),
)
