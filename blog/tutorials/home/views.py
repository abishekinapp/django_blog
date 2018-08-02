from django.views.generic import TemplateView
from home.forms import HomeForm ,CommentForm
from django.shortcuts import render,redirect,get_object_or_404
from home.models import Post , Comment
from django.utils import timezone


class HomeView(TemplateView):
    template_name='home/home.html'

    def get(self,request):
        form =HomeForm()
        posts = Post.objects.filter(date__lte = timezone.now()).order_by('-date')
        return render(request, 'home/home.html', {'form':form , 'posts': posts })


#def post_list(request):
#    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
#    return render(request, 'blog/post_list.html', {'posts': posts})

    def post(self,request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user=request.user
            post.save()
            text=form.cleaned_data['post']
            form = HomeForm()
            return redirect('/home/')


        args = {'form':form , 'text' :text }
        return render(request,self.template_name,args)


def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    comments = Comment.objects.filter(date__lte = timezone.now()).order_by('-date')
    return render(request, 'home/post_details.html', {'posts': posts ,'comments':comments})

def postlist(request):
    form =HomeForm()
    posts = Post.objects.filter(date__lte = timezone.now()).order_by('-date')
    return render(request, 'home/post_list.html', {'form':form , 'posts': posts })


'''
def Comment(request):
    form = CommentForm()
    comments=Comment.objects.filter(date__lte = timezone.now()).order_by('-date')

'''

def add_comment(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'home/add_comment.html', {'form': form,'posts':posts,})
