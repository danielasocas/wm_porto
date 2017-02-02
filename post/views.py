from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Comment
from .forms import CommentForm

def index(request):
    lasts_comment_list = Comment.objects.order_by('-created_date')[:5]
    comment_list = Comment.objects.all()
    context = {'lasts_comment_list': lasts_comment_list}
    return render(request, 'post/index.html', context)
    
def add_comment_to_post(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('index')
    else:
        form = CommentForm()
    return render(request, 'post/add_comment_to_post.html', {'form': form})
    
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('index')