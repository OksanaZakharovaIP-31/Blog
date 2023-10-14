from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.simple_tag
def total_post():
    """Count posts"""
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_post.html')
def show_latest_posts(count=5):
    """
    Show latest {count} post
    count: int
    """
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_post(count=5):
    """Show {count} most comment posts"""
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    """Use Markdown"""
    return mark_safe(markdown.markdown(text))