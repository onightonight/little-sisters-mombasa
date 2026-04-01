from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.utils.text import slugify
import uuid


class Photo(models.Model):
    CATEGORY_CHOICES = [
        ('elders', 'Elders'), ('volunteers', 'Volunteers'), ('events', 'Events'),
        ('facilities', 'Facilities'), ('community', 'Community'), ('other', 'Other'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='gallery/%Y/%m/')
    thumbnail = models.ImageField(upload_to='gallery/thumbnails/%Y/%m/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    photographer = models.CharField(max_length=100, blank=True)
    date_taken = models.DateField(default=timezone.now)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    alt_text = models.CharField(max_length=300, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        ordering = ['-date_uploaded']
        verbose_name_plural = 'Photos'
        indexes = [models.Index(fields=['-date_uploaded']), models.Index(fields=['category']), models.Index(fields=['featured'])]
    def __str__(self):
        return self.title


class Donation(models.Model):
    METHOD_CHOICES = [
        ('mpesa', 'M-Pesa'), ('bank', 'Bank Transfer'), ('crypto', 'Cryptocurrency'),
        ('paypal', 'PayPal'), ('card', 'Credit/Debit Card'), ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed'), ('refunded', 'Refunded'),
    ]
    FREQUENCY_CHOICES = [
        ('once', 'One-Time'), ('monthly', 'Monthly'), ('quarterly', 'Quarterly'), ('annual', 'Annual'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    donor_name = models.CharField(max_length=200)
    donor_email = models.EmailField()
    donor_phone = models.CharField(max_length=20, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(100)])
    currency = models.CharField(max_length=3, default='KES')
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES, default='once')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    message = models.TextField(blank=True)
    is_anonymous = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    receipt_url = models.URLField(blank=True, null=True)
    donated_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        ordering = ['-donated_at']
        indexes = [models.Index(fields=['-donated_at']), models.Index(fields=['status']), models.Index(fields=['method'])]
    def __str__(self):
        return f"{self.donor_name} - {self.amount} {self.currency}"


class Volunteer(models.Model):
    SKILL_CHOICES = [
        ('healthcare', 'Healthcare'), ('cooking', 'Cooking'), ('cleaning', 'Cleaning'),
        ('teaching', 'Teaching'), ('administrative', 'Administrative'), ('counseling', 'Counseling'),
        ('maintenance', 'Maintenance'), ('music', 'Music & Entertainment'), ('it', 'IT & Technology'),
        ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('registered', 'Registered'), ('active', 'Active'), ('inactive', 'Inactive'), ('vetted', 'Background Vetted'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    address = models.TextField()
    skills = models.CharField(max_length=50, choices=SKILL_CHOICES)
    motivation = models.TextField()
    availability = models.CharField(max_length=200)
    preferred_activities = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    emergency_contact_name = models.CharField(max_length=200, blank=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='registered')
    background_check_completed = models.BooleanField(default=False)
    joined_date = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(null=True, blank=True)
    hours_contributed = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    class Meta:
        ordering = ['-joined_date']
        indexes = [models.Index(fields=['status']), models.Index(fields=['-joined_date'])]
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'), ('published', 'Published'), ('archived', 'Archived'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, max_length=320)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    featured_image = models.ImageField(upload_to='blog/%Y/%m/', blank=True, null=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=500)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    tags = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    views = models.IntegerField(default=0)
    allow_comments = models.BooleanField(default=True)
    class Meta:
        ordering = ['-published_at', '-created_at']
        verbose_name_plural = 'Blog Posts'
        indexes = [models.Index(fields=['-published_at']), models.Index(fields=['slug']), models.Index(fields=['status'])]
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.status == 'published' and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)
    def get_tag_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()] if self.tags else []


class PrayerRequest(models.Model):
    TYPE_CHOICES = [
        ('health', 'Health'), ('family', 'Family'), ('work', 'Work/Employment'),
        ('financial', 'Financial'), ('spiritual', 'Spiritual'), ('thanksgiving', 'Thanksgiving'), ('other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('answered', 'Answered'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    request_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    intention = models.TextField()
    is_for_self = models.BooleanField(default=True)
    who_for = models.CharField(max_length=300, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    answered_on = models.DateTimeField(null=True, blank=True)
    answer_note = models.TextField(blank=True)
    class Meta:
        ordering = ['-created_at']
        indexes = [models.Index(fields=['status']), models.Index(fields=['-created_at'])]
    def __str__(self):
        return f"Prayer Request from {self.name}"


class ServiceAnnouncement(models.Model):
    SERVICE_TYPES = [
        ('mass', 'Mass'), ('rosary', 'Rosary'), ('visitation', 'Visitation Hours'),
        ('event', 'Special Event'), ('novena', 'Novena'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    description = models.TextField()
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday','Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),
        ('Thursday','Thursday'),('Friday','Friday'),('Saturday','Saturday'),('Sunday','Sunday'),
    ], blank=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['day_of_week', 'start_time']
    def __str__(self):
        return self.title


class Testimonial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    quote = models.TextField()
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return f"{self.name} - {self.role}"


class ContactMessage(models.Model):
    """Contact form submissions from website visitors."""
    INTEREST_CHOICES = [
        ('volunteering', 'Volunteering / AJJ'), ('corporate', 'Corporate Partnership'),
        ('inkind', 'In-Kind Donations'), ('admissions', 'Admissions / Elder Care'),
        ('vocation', 'Religious Vocation'), ('general', 'General Inquiry'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    interest = models.CharField(max_length=30, choices=INTEREST_CHOICES, default='general')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    replied_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
        indexes = [models.Index(fields=['is_read']), models.Index(fields=['-created_at'])]
    def __str__(self):
        return f"Message from {self.full_name} ({self.get_interest_display()})"


class Event(models.Model):
    """Upcoming events and special occasions at the home."""
    EVENT_TYPES = [
        ('birthday', 'Birthday Celebration'), ('mass', 'Special Mass'),
        ('fundraiser', 'Fundraiser'), ('community', 'Community Day'),
        ('training', 'Volunteer Training'), ('other', 'Other'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=200, default='Little Sisters of the Poor, Tudor')
    is_public = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        ordering = ['date', 'start_time']
        indexes = [models.Index(fields=['date']), models.Index(fields=['is_public', 'is_active'])]
    def __str__(self):
        return f"{self.title} — {self.date}"
    @property
    def is_upcoming(self):
        return self.date >= timezone.now().date()
