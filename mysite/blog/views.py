from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post

# Create your views here.
def post_list(request):
    #pobiera wszystkie posty do zmiennej
    posts = Post.objects.all()
    return render(request, "blog/post/list.html")