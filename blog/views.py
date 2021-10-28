from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

def home(request):
    # return HttpResponse("<h1>Home Page</h1>")
    context = {
        'posts': post.objects.all(),
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = post
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class UserPostListView(ListView):
    model = post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # ordering = ['-date_posted']
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = post  # blog/post_list.html  <app>/model_<viewtype>.html


def about(request):
    # return HttpResponse("<h1>About Page</h1>")
    return render(request, 'blog/about.html', {'title': 'tarun'})


class PostCreateView(CreateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False