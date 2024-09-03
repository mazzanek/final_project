from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path("", home_page_view, name="home"),
    path("about", about_page_view, name="about"),
    path("cnf", cnf_page_view, name="cnf"),
    path("contacts", contacts_page_view, name="contacts"),
    path("ctw", ctw_page_view, name="ctw"),
    path("ctwb", ctwb_page_view, name="ctwb"),
    path("dnf", dnf_page_view, name="dnf"),
    path("dyn", dyn_page_view, name="dyn"),
    path("dynb", dynb_page_view, name="dynb"),
    path("fim", fim_page_view, name="fim"),
    path("members-info", memebers_page_view, name="members-info"),
    path("sta", sta_page_view, name="sta"),
    path("gdpr", gdpr_page_view, name="gdpr"),
]