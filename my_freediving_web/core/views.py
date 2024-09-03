from django.shortcuts import render


def home_page_view(request):
    return render(request, "pages/home.html")


def about_page_view(request):
    return render(request, "pages/about.html")

def cnf_page_view(request):
    return render(request, "pages/cnf.html")

def contacts_page_view(request):
    return render(request, "pages/contacts.html")

def ctw_page_view(request):
    return render(request, "pages/ctw.html")

def ctwb_page_view(request):
    return render(request, "pages/ctwb.html")

def dnf_page_view(request):
    return render(request, "pages/dnf.html")

def dyn_page_view(request):
    return render(request, "pages/dyn.html")

def dynb_page_view(request):
    return render(request, "pages/dynb.html")

def fim_page_view(request):
    return render(request, "pages/fim.html")

def memebers_page_view(request):
    return render(request, "pages/members-info.html")

def sta_page_view(request):
    return render(request, "pages/sta.html")

def gdpr_page_view(request):
    return render(request, "pages/gdpr.html")