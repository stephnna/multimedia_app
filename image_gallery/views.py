from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm

def image_list(request):
  images = Image.objects.all()
  return render(request, 'image_gallery/image_list.html', {'images': images})

def upload_image(request):
  if request.method == 'POST':
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('image_list')
  else:
      form = ImageForm()
  return render(request, 'image_gallery/upload_image.html', {'form': form})
