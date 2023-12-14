from django.shortcuts import render,redirect

# Create your views here.
Language="English"
Template="home"

def index(request):
    global Language , Template
    Template="home"
    return render(request,f'{Language}/index.html',{})

def switch(request):
    print("Switch function called success")
    global Language
    if Language=="English":
        Language="Marathi"
    else:
        Language="English"

    return redirect(f'{Template}')

def trustees(request):
    global Template
    Template="trustees"
    print("Showed the trustees.\nThe language is :",Language)
    return render(request,f'{Language}/boardmembers.html',{})

def darshan(request):
    global Template
    Template = 'darshan'
    return render(request,f'{Language}/livedarshan.html')

def history(request):
    global Template
    Template = 'history'
    return render(request,f'{Language}/templehistory.html')

def dailyseva(request):
    global Template
    Template = 'dailyseva'
    return render(request,f'{Language}/dailyseva.html')

def mahaabhishekh(request):
    global Template
    Template = 'mahaabhishekh'
    return render(request,f'{Language}/mahaabhishek.html')

def imagegallery(request):
    global Template
    Template = 'imagegallery'
    return render(request,f'{Language}/imagegallery.html')

def videogallery(request):
    global Template
    Template = 'videogallery'
    return render(request,f'{Language}/videogallery.html')

def othergallery(request):
    global Template
    Template = 'othergallery'
    return render(request,f'{Language}/othergallery.html')

def poojadetails(request):
    global Template
    Template = 'poojadetails'
    return render(request,f'{Language}/pooja.html')

def donation(request):
    global Template
    Template = 'donation'
    return render(request,f'{Language}/donation.html')

def contact(request):
    global Template
    Template = 'contact'
    return render(request,f'{Language}/contact.html')

def Festivals(request):
    global Template
    Template = 'Festivals'
    return render(request,f'{Language}/Festivals.html')

def about(request):
    global Template
    Template = 'about'
    return render(request,f'{Language}/about.html')

def architecture(request):
    global Template
    Template = 'architecture'
    return render(request,f'{Language}/architecture.html')