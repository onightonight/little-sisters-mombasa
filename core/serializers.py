from rest_framework import serializers
from .models import (Photo, Donation, Volunteer, BlogPost, PrayerRequest,
                     ServiceAnnouncement, Testimonial, ContactMessage, Event)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'title', 'description', 'image', 'thumbnail', 'category',
                  'photographer', 'date_taken', 'date_uploaded', 'featured', 'views', 'alt_text']
        read_only_fields = ['id', 'date_uploaded', 'views']


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'donor_name', 'donor_email', 'donor_phone', 'amount', 'currency',
                  'method', 'frequency', 'status', 'message', 'is_anonymous', 'donated_at']
        read_only_fields = ['id', 'status', 'donated_at', 'transaction_id']

    def validate_amount(self, value):
        if value < 100:
            raise serializers.ValidationError("Minimum donation is 100 KES")
        return value


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'date_of_birth',
                  'address', 'skills', 'motivation', 'availability', 'status',
                  'joined_date', 'emergency_contact_name', 'emergency_contact_phone']
        read_only_fields = ['id', 'status', 'joined_date']


class BlogPostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.get_full_name', read_only=True)
    tag_list = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'author', 'author_name', 'featured_image',
                  'excerpt', 'content', 'status', 'tags', 'tag_list', 'created_at',
                  'updated_at', 'published_at', 'views', 'meta_description']
        read_only_fields = ['id', 'created_at', 'updated_at', 'views']

    def get_tag_list(self, obj):
        return obj.get_tag_list()


class PrayerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerRequest
        fields = ['id', 'name', 'email', 'request_type', 'intention', 'is_for_self',
                  'who_for', 'status', 'is_anonymous', 'created_at']
        read_only_fields = ['id', 'status', 'created_at']


class ServiceAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAnnouncement
        fields = ['id', 'title', 'service_type', 'description', 'day_of_week',
                  'start_time', 'end_time', 'location', 'is_active']
        read_only_fields = ['id']


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'role', 'image', 'quote', 'is_featured', 'is_published']
        read_only_fields = ['id']


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'full_name', 'email', 'phone', 'interest', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']


class EventSerializer(serializers.ModelSerializer):
    is_upcoming = serializers.ReadOnlyField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'event_type', 'description', 'date', 'start_time',
                  'end_time', 'location', 'is_public', 'is_upcoming', 'created_at']
        read_only_fields = ['id', 'created_at', 'is_upcoming']
