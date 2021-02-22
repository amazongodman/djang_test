# from django.shortcuts import render

# Create your views here.



from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def formfunc(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('list')
    else:
        form = PostForm()
    return render(request, 'form.html', {'form': form})

def listfunc(request):
    posts = Post.objects.all()
    return render(request, 'list.html', {'posts': posts})

def detailfunc(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'detail.html', {'post': post})









