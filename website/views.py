from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "website/index.html", {})

def services(request):
    return render(request, "website/services.html", {})

def equipment(request):
    return render(request, "website/equipment.html", {})

def contact(request):
    return render(request, "website/contact.html", {})

def external(request):
    return render(request, "website/external.html", {})

def join(request):
    return render(request, "website/join.html", {})

def crew(request):
    return render(request, "website/crew.html", {})

def hots(request):
    return render(request, "website/hots.html", {})

def alumni(request):
    return render(request, "website/alumni.html", {})

def events(request):
    return render(request, "website/events.html", {})

def events70(request):
    return render(request, "website/events-1970.html", {})

def events80(request):
    return render(request, "website/events-1980.html", {})

def events90(request):
    return render(request, "website/events-1990.html", {})

def events00(request):
    return render(request, "website/events-2000.html", {})

def timelapse(request):
    return render(request, "website/timelapse.html", {})

def accolades(request):
    return render(request, "website/accolades.html", {})
