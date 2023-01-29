from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, RedirectView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import PostCreateForm

class BlogIndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'name': 'mohammad '
        }

        return context


class RedticetViewTest(RedirectView):
    pattern_name = 'blog:index'
    def get_redirect_url(self, *args ,**kwargs):
        article_id = kwargs['pk']
        post = get_object_or_404(Post, id=article_id)
        print(post)
        return super().get_redirect_url(*args,**kwargs)



class PostListView(ListView):

    queryset = Post.objects.all()
    paginate_by = 2
    allow_empty = False # if This Atter is False its mean Django Should Raise A 404 Error For User
    context_object_name = 'posts'
    template_name = 'blog/posts_list.html'


class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post
    context_object_name = 'post'



class CreatePostView(PermissionRequiredMixin,LoginRequiredMixin, CreateView):
    permission_required = 'blog.add_post'
    template_name = 'blog/post_create.html'
    success_url = '/blog/posts/'
    form_class = PostCreateForm


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_create.html'
    success_url = '/blog/posts/'
    form_class = PostCreateForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/blog/posts/'
    template_name_suffix = '_delete'