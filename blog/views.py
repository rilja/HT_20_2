from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'preview',)
    success_url = reverse_lazy('blog:list')


class BlogListView(ListView):
    model = Blog


# class BlogDeleteView(DeleteView):
#     model = Blog


class BlogDetailView(DetailView):
    model = Blog
