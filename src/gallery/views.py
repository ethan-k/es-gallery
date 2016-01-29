from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

# Create your views here.

from .models import Gallery

def gallery(request, object_id=None):


    template = "gallery.html"
    context = {

    }
    return render(request, template, context)


def image_like_update(request, object_id=None):
    response_data = {}
    if request.method == 'POST':
        image = get_object_or_404(Gallery, object_id)
        image['likes'] = image['likes'] + 1

        return JsonResponse(image['likes'])
    else:
        return JsonResponse("false")


# 우아한 디버깅을 위한 전체 이미지 출력 페이지
def list_view(request):
    queryset = Gallery.objects.all()
    template = "list_view.html"
    context = {
        "queryset": queryset
    }
    return render(request, template, context)
