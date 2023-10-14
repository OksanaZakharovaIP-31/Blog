from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from django.views.decorators.http import require_POST
from taggit.models import Tag
from django.views.generic import ListView


# Create your views here.

# Пример класса для отображения всех записей
# class PostListView(ListView):
#     queryset = Post.published.all()  # Запрос
#     context_object_name = 'posts'  # Результаты запроса
#     paginate_by = 5  # Количество объектов на странице
#     template_name = 'blog/post/list.html'  # Страница для отображения


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post,
                             id=post_id,
                             status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'blog/post/comment.html',
                  {'post': post,
                   'form': form,
                   'comment': comment})


def post_list(request, tag_slug=None):
    posts_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts_list = posts_list.filter(tags__in=[tag])
    paginator = Paginator(posts_list, 5)
    page_num = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html',
                  {'posts': posts,
                   'tag': tag})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             status=Post.Status.PUBLISHED)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(request, 'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'form': form})
