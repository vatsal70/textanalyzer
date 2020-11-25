from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact
def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    global params
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newline = request.POST.get('newline', 'off')
    extraspace = request.POST.get('extraspace', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed, 'nw': djtext}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalize', 'analyzed_text': analyzed, 'nw': djtext}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newline == 'on':
        analyzed = ''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed, 'nw': djtext}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if extraspace == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Line Remove', 'analyzed_text': analyzed, 'nw': djtext}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if removepunc != "on" and newline != "on" and extraspace != "on" and fullcaps != "on":
        return render(request, "error.html")

    return render(request, 'analyze.html', params)


def error(request):
    return HttpResponse(request, "error.html")


def aboutus(request):
    return render(request, 'AboutUs.html')


def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        que = True
        return render(request, 'contactus.html', {'que': que})
    return render(request, 'contactus.html')
    # return render(request, 'contactus.html')