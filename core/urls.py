from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'photos', views.PhotoViewSet, basename='photo')
router.register(r'donations', views.DonationViewSet, basename='donation')
router.register(r'volunteers', views.VolunteerViewSet, basename='volunteer')
router.register(r'blog', views.BlogPostViewSet, basename='blogpost')
router.register(r'prayers', views.PrayerRequestViewSet, basename='prayerrequest')
router.register(r'services', views.ServiceAnnouncementViewSet, basename='service')
router.register(r'testimonials', views.TestimonialViewSet, basename='testimonial')
router.register(r'contact', views.ContactMessageViewSet, basename='contact')
router.register(r'events', views.EventViewSet, basename='event')

app_name = 'core'

urlpatterns = [
    path('', include(router.urls)),
]
