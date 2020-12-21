from django.shortcuts import render, get_object_or_404
from .models import Post #el punto indica que esta en el directorio actual
from django.utils import timezone

# Create your views here.
def post_list(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_list.html', {'posts': posts})