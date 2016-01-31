from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, Http404
import json

# Create your views here.

from .models import Gallery

def gallery(request, object_id=None):

    queryset = Gallery.objects.all()
    template = "gallery.html"
    context = {
        "queryset": queryset
    }
    return render(request, template, context)


def image_like_update(request):
    response_data = {}
    if request.is_ajax():
        if request.method == 'POST':
            print(request.body)

            object_id = request.POST['object_id']
            image = get_object_or_404(Gallery, id=object_id)
            print(image)
            print(image.likes)
            image.likes = image.likes + 1
            print (image.likes)
            image.save()

            return HttpResponse(image.likes)
        else:
            return HttpResponse("Fail")
    return HttpResponse("Fail")


# 우아한 디버깅을 위한 전체 이미지 출력 페이지
def list_view(request):
    queryset = Gallery.objects.all()
    template = "list_view.html"
    context = {
        "queryset": queryset
    }
    return render(request, template, context)
