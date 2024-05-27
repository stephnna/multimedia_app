from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Image
from .forms import ImageForm, SignUpForm

@login_required
def image_list(request):
    images = Image.objects.all()
    return render(request, 'image_gallery/image_list.html', {'images': images})

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'image_gallery/upload_image.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('image_list')
    else:
        form = SignUpForm()
    return render(request, 'image_gallery/signup.html', {'form': form})
