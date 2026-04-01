from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from .models import (Photo, Donation, Volunteer, BlogPost, PrayerRequest,
                     ServiceAnnouncement, Testimonial, ContactMessage, Event)
from .serializers import (PhotoSerializer, DonationSerializer, VolunteerSerializer,
                          BlogPostSerializer, PrayerRequestSerializer,
                          ServiceAnnouncementSerializer, TestimonialSerializer,
                          ContactMessageSerializer, EventSerializer)


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.filter(is_published=True).order_by('-date_uploaded')
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'featured']
    search_fields = ['title', 'description', 'photographer']
    ordering_fields = ['date_uploaded', 'views', 'date_taken']

    @action(detail=True, methods=['post'])
    def increment_views(self, request, pk=None):
        photo = self.get_object()
        photo.views += 1
        photo.save(update_fields=['views'])
        return Response({'views': photo.views})

    @action(detail=False, methods=['get'])
    def featured(self, request):
        queryset = self.queryset.filter(featured=True)[:6]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Return counts grouped by category"""
        from django.db.models import Count
        data = Photo.objects.filter(is_published=True).values('category').annotate(count=Count('id'))
        return Response(list(data))


class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'method', 'frequency']
    ordering_fields = ['donated_at', 'amount']

    def get_queryset(self):
        if self.request.user.is_staff:
            return Donation.objects.all()
        return Donation.objects.filter(status='completed')

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        donations = Donation.objects.filter(status='completed')
        total = sum(d.amount for d in donations)
        count = donations.count()
        monthly = donations.filter(frequency='monthly').count()
        return Response({
            'total_amount': float(total),
            'total_donations': count,
            'average': float(total / count) if count > 0 else 0,
            'monthly_donors': monthly,
        })


class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'skills']
    search_fields = ['first_name', 'last_name', 'email']

    def get_queryset(self):
        if self.request.user.is_staff:
            return Volunteer.objects.all()
        return Volunteer.objects.filter(status__in=['active', 'vetted'])

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        total = Volunteer.objects.count()
        active = Volunteer.objects.filter(status='active').count()
        hours = sum(v.hours_contributed for v in Volunteer.objects.all())
        return Response({
            'total_volunteers': total,
            'active_volunteers': active,
            'total_hours': float(hours),
        })


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.filter(status='published').order_by('-published_at')
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status']
    search_fields = ['title', 'content', 'tags', 'excerpt']
    ordering_fields = ['published_at', 'views']
    lookup_field = 'slug'

    def get_queryset(self):
        if self.request.user.is_staff:
            return BlogPost.objects.all().order_by('-created_at')
        return BlogPost.objects.filter(status='published').order_by('-published_at')

    @action(detail=True, methods=['post'])
    def increment_views(self, request, slug=None):
        post = self.get_object()
        post.views += 1
        post.save(update_fields=['views'])
        return Response({'views': post.views})

    @action(detail=False, methods=['get'])
    def recent(self, request):
        queryset = self.get_queryset()[:5]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PrayerRequestViewSet(viewsets.ModelViewSet):
    queryset = PrayerRequest.objects.filter(status='approved')
    serializer_class = PrayerRequestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_staff:
            return PrayerRequest.objects.all()
        return PrayerRequest.objects.filter(status__in=['approved', 'answered'])

    @action(detail=False, methods=['get'])
    def recent_answered(self, request):
        queryset = PrayerRequest.objects.filter(status='answered').order_by('-answered_on')[:10]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ServiceAnnouncementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceAnnouncement.objects.filter(is_active=True)
    serializer_class = ServiceAnnouncementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['service_type', 'day_of_week']


class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonial.objects.filter(is_published=True).order_by('-created_at')
    serializer_class = TestimonialSerializer

    @action(detail=False, methods=['get'])
    def featured(self, request):
        queryset = self.queryset.filter(is_featured=True)[:4]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ContactMessageViewSet(viewsets.ModelViewSet):
    """Accepts contact form submissions; staff can view all."""
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticatedOrReadOnly()]

    def get_queryset(self):
        if self.request.user.is_staff:
            return ContactMessage.objects.all()
        return ContactMessage.objects.none()

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticatedOrReadOnly])
    def unread(self, request):
        if not request.user.is_staff:
            return Response({'detail': 'Not authorised.'}, status=status.HTTP_403_FORBIDDEN)
        queryset = ContactMessage.objects.filter(is_read=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.filter(is_active=True, is_public=True)
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['event_type']
    search_fields = ['title', 'description']

    def get_queryset(self):
        if self.request.user.is_staff:
            return Event.objects.all()
        return Event.objects.filter(is_active=True, is_public=True)

    @action(detail=False, methods=['get'])
    def upcoming(self, request):
        today = timezone.now().date()
        queryset = Event.objects.filter(is_active=True, is_public=True, date__gte=today).order_by('date')[:10]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
