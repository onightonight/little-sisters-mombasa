from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Photo, BlogPost, Event, ServiceAnnouncement, Testimonial


def index(request):
    """Homepage — featured photos, recent posts, upcoming events, testimonials."""
    today = timezone.now().date()
    context = {
        'featured_photos': Photo.objects.filter(is_published=True, featured=True)[:6],
        'recent_blog_posts': BlogPost.objects.filter(status='published').order_by('-published_at')[:3],
        'upcoming_events': Event.objects.filter(is_active=True, is_public=True, date__gte=today).order_by('date')[:4],
        'services': ServiceAnnouncement.objects.filter(is_active=True)[:6],
        'testimonials': Testimonial.objects.filter(is_published=True, is_featured=True)[:3],
    }
    return render(request, 'index.html', context)


def gallery_view(request):
    """Full photo gallery with filtering."""
    category = request.GET.get('category', '')
    photos = Photo.objects.filter(is_published=True)
    if category:
        photos = photos.filter(category=category)
    context = {
        'photos': photos,
        'selected_category': category,
        'categories': Photo.CATEGORY_CHOICES,
    }
    return render(request, 'gallery.html', context)


def blog_view(request):
    """Blog listing."""
    tag = request.GET.get('tag', '')
    posts = BlogPost.objects.filter(status='published').order_by('-published_at')
    if tag:
        posts = posts.filter(tags__icontains=tag)
    context = {'blog_posts': posts, 'selected_tag': tag}
    return render(request, 'blog.html', context)


def blog_detail_view(request, slug):
    """Single blog post."""
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    post.views += 1
    post.save(update_fields=['views'])
    tag_list = post.get_tag_list()
    related_posts = BlogPost.objects.filter(
        status='published',
        tags__icontains=tag_list[0] if tag_list else ''
    ).exclude(id=post.id)[:3] if tag_list else BlogPost.objects.filter(
        status='published'
    ).exclude(id=post.id).order_by('-published_at')[:3]
    context = {'post': post, 'related_posts': related_posts, 'tag_list': tag_list}
    return render(request, 'blog-detail.html', context)


def donate_view(request):
    return render(request, 'donate.html')


def volunteer_view(request):
    return render(request, 'volunteer.html')


def prayer_view(request):
    return render(request, 'prayer.html')


def events_view(request):
    today = timezone.now().date()
    upcoming = Event.objects.filter(is_active=True, is_public=True, date__gte=today).order_by('date')
    past = Event.objects.filter(is_active=True, is_public=True, date__lt=today).order_by('-date')[:6]
    context = {'upcoming_events': upcoming, 'past_events': past}
    return render(request, 'events.html', context)


def contact_view(request):
    return render(request, 'contact.html')
