from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post, Comment, Reply, Likes
from .forms import PostForm
from users.models import CustomUser as User
from django.db.models import Count
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy

def home(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    replies = Reply.objects.all()
    likes = Likes.objects.all()
    
    context = {
        'posts': posts,
        'comments': comments,
        'replies': replies,
        'likes': likes,
    }
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
        context['form'] = form
    
    return render(request, 'blog/home.html', context)

class PostCreate(LoginRequiredMixin, CreateView):
    
    def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)
    
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.all()
        replies = Reply.objects.all()
        context['comments'] = comments
        context['replies'] = replies
        return context
    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["content"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('home')

    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["content"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["content"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('home')

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ["content"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)
    
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = "/"
    
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

class ReplyCreateView(LoginRequiredMixin, CreateView):
    model = Reply
    fields = ["content"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.comment = Comment.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('home')

class ReplyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reply
    fields = ["content"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.comment = Comment.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)
    
    def test_func(self):
        reply = self.get_object()
        if self.request.user == reply.author:
            return True
        return False

class ReplyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Reply
    success_url = "/"
    
    def test_func(self):
        reply = self.get_object()
        if self.request.user == reply.author:
            return True
        return False


def logoutView(request):
    logout(request)
    return render(request, "users/logout.html")