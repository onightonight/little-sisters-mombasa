from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from .models import (Photo, Donation, Volunteer, BlogPost, PrayerRequest,
                     ServiceAnnouncement, Testimonial, ContactMessage, Event)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'date_taken', 'views', 'image_preview']
    list_filter = ['category', 'featured', 'is_published', 'date_uploaded']
    search_fields = ['title', 'description', 'photographer']
    readonly_fields = ['date_uploaded', 'views', 'image_preview_large']
    list_editable = ['featured']
    fieldsets = (
        ('Basic Information', {'fields': ('title', 'description', 'alt_text', 'category')}),
        ('Image', {'fields': ('image', 'image_preview_large', 'thumbnail')}),
        ('Details', {'fields': ('photographer', 'date_taken', 'featured', 'is_published', 'uploaded_by')}),
        ('Metadata', {'fields': ('date_uploaded', 'views'), 'classes': ('collapse',)}),
    )
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="40" height="40" style="border-radius:4px;object-fit:cover;" />', obj.image.url)
        return "—"
    image_preview.short_description = 'Preview'
    def image_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="300" style="border-radius:4px;" />', obj.image.url)
        return "No image"
    image_preview_large.short_description = 'Preview'


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['donor_name', 'amount_display', 'method', 'frequency', 'status_badge', 'donated_at']
    list_filter = ['status', 'method', 'frequency', 'currency', 'donated_at']
    search_fields = ['donor_name', 'donor_email', 'transaction_id']
    readonly_fields = ['id', 'donated_at', 'completed_at', 'transaction_id']
    date_hierarchy = 'donated_at'
    fieldsets = (
        ('Donor', {'fields': ('donor_name', 'donor_email', 'donor_phone', 'is_anonymous', 'user')}),
        ('Donation', {'fields': ('amount', 'currency', 'method', 'frequency', 'message')}),
        ('Status', {'fields': ('status', 'transaction_id', 'receipt_url', 'donated_at', 'completed_at')}),
        ('System', {'fields': ('id',), 'classes': ('collapse',)}),
    )
    def amount_display(self, obj):
        return f"{obj.amount} {obj.currency}"
    amount_display.short_description = 'Amount'
    def status_badge(self, obj):
        colors = {'completed': '#16a34a', 'pending': '#d97706', 'failed': '#dc2626', 'refunded': '#6b7280'}
        color = colors.get(obj.status, '#3b82f6')
        return format_html('<span style="background:{};color:white;padding:3px 10px;border-radius:4px;font-size:0.75rem;font-weight:600;">{}</span>', color, obj.status.upper())
    status_badge.short_description = 'Status'


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['name_display', 'email', 'phone', 'skills', 'status_badge', 'hours_contributed', 'joined_date']
    list_filter = ['status', 'skills', 'background_check_completed', 'joined_date']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    readonly_fields = ['id', 'joined_date', 'last_activity']
    date_hierarchy = 'joined_date'
    fieldsets = (
        ('Personal', {'fields': ('first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'address')}),
        ('Emergency Contact', {'fields': ('emergency_contact_name', 'emergency_contact_phone')}),
        ('Volunteer Details', {'fields': ('skills', 'motivation', 'availability', 'preferred_activities', 'experience')}),
        ('Status', {'fields': ('status', 'background_check_completed', 'hours_contributed')}),
        ('Activity', {'fields': ('joined_date', 'last_activity', 'notes'), 'classes': ('collapse',)}),
        ('System', {'fields': ('id',), 'classes': ('collapse',)}),
    )
    def name_display(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    name_display.short_description = 'Name'
    def status_badge(self, obj):
        colors = {'active': '#16a34a', 'inactive': '#dc2626', 'registered': '#3b82f6', 'vetted': '#065f46'}
        color = colors.get(obj.status, '#6b7280')
        return format_html('<span style="background:{};color:white;padding:3px 10px;border-radius:4px;font-size:0.75rem;font-weight:600;">{}</span>', color, obj.status.upper())
    status_badge.short_description = 'Status'


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status_badge', 'published_at', 'views']
    list_filter = ['status', 'published_at', 'created_at']
    search_fields = ['title', 'content', 'slug', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at', 'views']
    date_hierarchy = 'published_at'
    fieldsets = (
        ('Content', {'fields': ('title', 'slug', 'excerpt', 'content', 'featured_image')}),
        ('SEO', {'fields': ('meta_description', 'tags')}),
        ('Publishing', {'fields': ('status', 'author', 'published_at', 'allow_comments')}),
        ('Metadata', {'fields': ('created_at', 'updated_at', 'views'), 'classes': ('collapse',)}),
    )
    def status_badge(self, obj):
        colors = {'published': '#16a34a', 'draft': '#d97706', 'archived': '#6b7280'}
        color = colors.get(obj.status, '#3b82f6')
        return format_html('<span style="background:{};color:white;padding:3px 10px;border-radius:4px;font-size:0.75rem;font-weight:600;">{}</span>', color, obj.status.upper())
    status_badge.short_description = 'Status'


@admin.register(PrayerRequest)
class PrayerRequestAdmin(admin.ModelAdmin):
    list_display = ['name_display', 'request_type', 'status_badge', 'is_anonymous', 'created_at']
    list_filter = ['request_type', 'status', 'is_anonymous', 'created_at']
    search_fields = ['name', 'email', 'intention']
    readonly_fields = ['id', 'created_at', 'approved_at', 'answered_on']
    fieldsets = (
        ('Requestor', {'fields': ('name', 'email', 'is_anonymous')}),
        ('Request', {'fields': ('request_type', 'intention', 'is_for_self', 'who_for')}),
        ('Status', {'fields': ('status', 'answer_note', 'created_at', 'approved_at', 'answered_on')}),
        ('System', {'fields': ('id',), 'classes': ('collapse',)}),
    )
    def name_display(self, obj):
        return "Anonymous" if obj.is_anonymous else obj.name
    name_display.short_description = 'Name'
    def status_badge(self, obj):
        colors = {'approved': '#16a34a', 'pending': '#d97706', 'answered': '#065f46', 'rejected': '#dc2626'}
        color = colors.get(obj.status, '#3b82f6')
        return format_html('<span style="background:{};color:white;padding:3px 10px;border-radius:4px;font-size:0.75rem;font-weight:600;">{}</span>', color, obj.status.upper())
    status_badge.short_description = 'Status'


@admin.register(ServiceAnnouncement)
class ServiceAnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'service_type', 'day_of_week', 'start_time', 'location', 'is_active']
    list_filter = ['service_type', 'day_of_week', 'is_active']
    search_fields = ['title', 'description']
    list_editable = ['is_active']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'is_featured', 'is_published', 'image_preview']
    list_filter = ['is_featured', 'is_published']
    search_fields = ['name', 'role', 'quote']
    list_editable = ['is_featured', 'is_published']
    readonly_fields = ['created_at', 'image_preview_large']
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="36" height="36" style="border-radius:50%;object-fit:cover;" />', obj.image.url)
        return "—"
    image_preview.short_description = 'Photo'
    def image_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" style="border-radius:6px;" />', obj.image.url)
        return "No image"
    image_preview_large.short_description = 'Preview'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'interest', 'is_read', 'is_read_badge', 'created_at']
    list_filter = ['interest', 'is_read', 'created_at']
    search_fields = ['full_name', 'email', 'message']
    readonly_fields = ['id', 'created_at']
    list_editable = ['is_read']
    date_hierarchy = 'created_at'
    fieldsets = (
        ('Contact', {'fields': ('full_name', 'email', 'phone', 'interest')}),
        ('Message', {'fields': ('message',)}),
        ('Management', {'fields': ('is_read', 'replied_at', 'created_at')}),
        ('System', {'fields': ('id',), 'classes': ('collapse',)}),
    )
    def is_read_badge(self, obj):
        if obj.is_read:
            return format_html('<span style="color:#16a34a;font-weight:600;">✓ Read</span>')
        return format_html('<span style="color:#d97706;font-weight:600;">● Unread</span>')
    is_read_badge.short_description = 'Status'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_type', 'date', 'start_time', 'location', 'is_public', 'is_active', 'is_upcoming_badge']
    list_filter = ['event_type', 'is_public', 'is_active', 'date']
    search_fields = ['title', 'description', 'location']
    list_editable = ['is_public', 'is_active']
    date_hierarchy = 'date'
    readonly_fields = ['id', 'created_at']
    fieldsets = (
        ('Event', {'fields': ('title', 'event_type', 'description')}),
        ('Schedule', {'fields': ('date', 'start_time', 'end_time', 'location')}),
        ('Visibility', {'fields': ('is_public', 'is_active', 'created_by')}),
        ('System', {'fields': ('id', 'created_at'), 'classes': ('collapse',)}),
    )
    def is_upcoming_badge(self, obj):
        today = timezone.now().date()
        if obj.date >= today:
            return format_html('<span style="color:#16a34a;font-weight:600;">Upcoming</span>')
        return format_html('<span style="color:#6b7280;">Past</span>')
    is_upcoming_badge.short_description = 'Timing'
