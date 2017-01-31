from django.shortcuts import render

# Create your views here.
from .models import Comment


def index(request):
    lasts_comment_list = Comment.objects.order_by('-created_date')[:5]
    comment_list = Comment.objects.all()
    context = {'lasts_comment_list': lasts_comment_list}
    return render(request, 'post/index.html', context)