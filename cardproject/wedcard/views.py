from django.shortcuts import render, get_object_or_404


from django.http import HttpResponse
from .models import wedding_card

def base(request):
    return render(request, 'wedcard/base.html', {})

def about(request):
    return render(request, 'wedcard/about.html', {})

def contact(request):
    return render(request, 'wedcard/about.html', {})

def notice(request):
    return render(request, 'wedcard/about.html', {})

def news(request):
    return render(request, 'wedcard/about.html', {})

def remarks(request):
    return render(request, 'wedcard/about.html', {})

def sample_view(request):
    samples = wedding_card.objects.all()  # Fetch all Sample objects
    return render(request, 'wedcard/samples.html', {'samples': samples})

def detail(request, pk):
    card = get_object_or_404(wedding_card, pk=pk)
    return render(request, 'wedcard/detail.html', {'card': card})
