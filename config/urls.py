from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.page_views import (
    index, gallery_view, blog_view, blog_detail_view,
    donate_view, volunteer_view, prayer_view, events_view, contact_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # Frontend routes
    path('', index, name='home'),
    path('gallery/', gallery_view, name='gallery'),
    path('blog/', blog_view, name='blog'),
    path('blog/<slug:slug>/', blog_detail_view, name='blog-detail'),
    path('donate/', donate_view, name='donate'),
    path('volunteer/', volunteer_view, name='volunteer'),
    path('prayer/', prayer_view, name='prayer'),
    path('events/', events_view, name='events'),
    path('contact/', contact_view, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Little Sisters of the Poor – Mombasa"
admin.site.site_title = "LSP Admin Portal"
admin.site.index_title = "Welcome to the Admin Portal"
