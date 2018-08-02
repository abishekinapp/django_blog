from django.views.generic import TemplateView
from home.forms import HomeForm
from django.shortcuts import render,redirect,get_object_or_404
from home.models import Post
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
    return render(request, 'home/post_details.html', {'posts': posts})


def postlist(request):
    form =HomeForm()
    posts = Post.objects.filter(date__lte = timezone.now()).order_by('-date')
    return render(request, 'home/post_list.html', {'form':form , 'posts': posts })
