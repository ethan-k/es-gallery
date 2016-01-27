from django.shortcuts import render

# Create your views here.

def gallery(request, object_id=None):


    template = "gallery.html"
    context = {

    }
    return render(request, template, context)


def gallery_update(request, object_id=None):
    pass

