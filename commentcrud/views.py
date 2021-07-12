from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from .forms import myForm
from postcrud.models import Post

def commentcreate(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method=='POST':
        form = myForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('postshow',post_id=post.pk)
        else:
            redirect('list')
    else:
        form=myForm()
        return render(request,'postshow.html',{'form':form,'post':post})
