from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect, JsonResponse
import json


# Create your views here.


def upload_image(request):
    if request.method == 'GET':
        return render(request, 'gallery/upload_image.html')
    elif request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = Image(image=form.cleaned_data["image"],
                              name=form.cleaned_data["name"]
                              )
            new_image.save()
            return HttpResponseRedirect('../image_gallery')


def image_gallery(request):
    images = Image.objects.all()
    # print(images)
    return render(request, 'gallery/image_gallery.html', {'images': images[::-1]})


def delete_image(request):
    if request.method == 'POST':
        # image_id = request.body
        body = json.loads(request.body)
        print(body)
        if body["image_id"] != "":
            Image.objects.filter(id=body["image_id"]).delete()
            data = {
                'image_deleted': 'true',
            }
            return JsonResponse(data)

        return HttpResponseRedirect('../image_gallery')