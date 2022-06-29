from django.shortcuts import render
from django.http import HttpResponse
from user.models import Avatar
# Create your views here.


def index(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    return render(
        request=request,
        context=context_dict,
        template_name= 'index.html')

def about(request):
    return render(request, 'about.html')


def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}
