"""
Load sample data for the Little Sisters of the Poor – Mombasa system.
Run: python manage.py shell < load_sample_data.py
  or: python load_sample_data.py (from project root after activating venv)
"""
import os
import sys
import django
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date, timedelta
from core.models import (BlogPost, ServiceAnnouncement, Testimonial,
                          PrayerRequest, ContactMessage, Event)

print("Loading sample data...")

# Admin user
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@littlesisters-mombasa.org', 'Admin@1234!')
    print("  ✓ Superuser created  (username: admin / password: Admin@1234!)")

# Blog posts
posts = [
    {
        'title': 'Christmas Celebrations at Our Home in Tudor',
        'slug': 'christmas-celebrations-tudor-2024',
        'excerpt': 'A joyful Christmas was celebrated at our home, with carol singing, gift-giving and a special festive meal shared by residents, Sisters and volunteers.',
        'content': '''The Christmas season brought great joy to our home in Tudor, Mombasa. Residents, Little Sisters, staff, and the Association Jeanne Jugan gathered in the chapel for a special Mass of Thanksgiving, followed by carol singing in the garden.

Thanks to the generosity of our benefactors, every resident received a personal gift and enjoyed a special festive meal prepared with love by our kitchen team and volunteers. The celebrations continued with music, dancing, and shared memories — a reminder that family is not only about blood, but about love and service.

We are deeply grateful to all who made this Christmas possible through their donations, time, and prayers. May God reward your kindness.''',
        'status': 'published',
        'tags': 'christmas, celebrations, community, residents',
        'meta_description': 'Christmas celebrations at the Little Sisters of the Poor home in Tudor, Mombasa.',
    },
    {
        'title': 'New Volunteers Join the Association Jeanne Jugan',
        'slug': 'new-ajj-volunteers-2025',
        'excerpt': 'We are delighted to welcome a new cohort of volunteers to the Association Jeanne Jugan, pledging a year of formation and service to our elderly residents.',
        'content': '''The Little Sisters of the Poor in Mombasa are delighted to welcome twelve new members to the Association Jeanne Jugan this May, on the Feast of St. Joseph the Worker.

The Association Jeanne Jugan was established in 1998 to unite lay collaborators — women and men from all walks of life — who wish to share in the mission of the Little Sisters: serving Jesus Christ in the person of the elderly poor. The new cohort includes nurses, teachers, business professionals, and students, all bound by a common desire to serve with love and humility.

Formation sessions will begin this month, focusing on the spirit and charism of Saint Jeanne Jugan, practical skills in elder care, and spiritual accompaniment.

If you would like to join the Association, please contact us at ajj@littlesisters-mombasa.org or call +254 723 087 740.''',
        'status': 'published',
        'tags': 'volunteers, AJJ, community, formation',
        'meta_description': 'New volunteers join the Association Jeanne Jugan at the Little Sisters of the Poor, Mombasa.',
    },
    {
        'title': 'A Message of Gratitude to Our Benefactors',
        'slug': 'gratitude-benefactors-2025',
        'excerpt': 'The Little Sisters and our elderly residents wish to express their heartfelt gratitude to every benefactor whose generosity makes our mission possible.',
        'content': '''Each day, in our Chapel at Tom Mboya Avenue, Tudor, the Little Sisters and our elderly residents pray for the intentions of all our benefactors, friends and family members. This is our most precious gift to you: the daily prayer of the old and the poor, offered to God on your behalf.

Saint Jeanne Jugan reminded the Sisters always: "What would we do without them?" The needs of our home are many — daily meals for 74 residents, medical care, clothing, maintenance, celebrations — and none of it would be possible without your generous support.

Whether you have given once or many times; whether in money, in kind, or in time — you are part of our family. We remember you by name. We pray for you by name. And we trust that God, who is never outdone in generosity, will return your kindness a hundredfold.

Thank you, from the bottom of our hearts.''',
        'status': 'published',
        'tags': 'gratitude, benefactors, prayer, mission',
        'meta_description': 'A message of gratitude from the Little Sisters of the Poor to all their benefactors and supporters.',
    },
]

admin_user = User.objects.get(username='admin')
for p in posts:
    if not BlogPost.objects.filter(slug=p['slug']).exists():
        BlogPost.objects.create(
            author=admin_user,
            published_at=timezone.now() - timedelta(days=posts.index(p)*14),
            **p,
        )
        print(f"  ✓ Blog post: {p['title']}")

# Services
services_data = [
    {'title': 'Morning Mass', 'service_type': 'mass', 'day_of_week': 'Monday', 'start_time': '06:30', 'end_time': '07:15', 'location': 'Chapel, Little Sisters of the Poor', 'description': 'Daily morning Mass open to residents, Sisters, staff and visitors.'},
    {'title': 'Morning Mass', 'service_type': 'mass', 'day_of_week': 'Tuesday', 'start_time': '06:30', 'end_time': '07:15', 'location': 'Chapel, Little Sisters of the Poor', 'description': 'Daily morning Mass open to residents, Sisters, staff and visitors.'},
    {'title': 'Morning Mass', 'service_type': 'mass', 'day_of_week': 'Wednesday', 'start_time': '06:30', 'end_time': '07:15', 'location': 'Chapel, Little Sisters of the Poor', 'description': 'Daily morning Mass open to residents, Sisters, staff and visitors.'},
    {'title': 'Morning Mass', 'service_type': 'mass', 'day_of_week': 'Thursday', 'start_time': '06:30', 'end_time': '07:15', 'location': 'Chapel, Little Sisters of the Poor', 'description': 'Daily morning Mass open to residents, Sisters, staff and visitors.'},
    {'title': 'Morning Mass', 'service_type': 'mass', 'day_of_week': 'Friday', 'start_time': '06:30', 'end_time': '07:15', 'location': 'Chapel, Little Sisters of the Poor', 'description': 'Daily morning Mass open to residents, Sisters, staff and visitors.'},
    {'title': 'Sunday Mass', 'service_type': 'mass', 'day_of_week': 'Sunday', 'start_time': '08:00', 'end_time': '09:00', 'location': 'Chapel, Little Sisters of the Poor', 'description': 'Sunday Mass — all are welcome.'},
    {'title': 'Rosary', 'service_type': 'rosary', 'day_of_week': 'Saturday', 'start_time': '06:00', 'end_time': '06:30', 'location': 'Chapel, Little Sisters of the Poor', 'description': 'Saturday morning Rosary with the community.'},
    {'title': 'Visiting Hours', 'service_type': 'visitation', 'day_of_week': 'Monday', 'start_time': '09:00', 'end_time': '12:00', 'location': 'Little Sisters of the Poor, Tudor', 'description': 'Morning visiting hours for family and friends of residents.'},
    {'title': 'Visiting Hours', 'service_type': 'visitation', 'day_of_week': 'Sunday', 'start_time': '14:00', 'end_time': '17:00', 'location': 'Little Sisters of the Poor, Tudor', 'description': 'Afternoon visiting hours — Sunday.'},
]
for s in services_data:
    if not ServiceAnnouncement.objects.filter(title=s['title'], day_of_week=s.get('day_of_week', '')).exists():
        ServiceAnnouncement.objects.create(**s)
print(f"  ✓ {len(services_data)} service announcements created")

# Testimonials
testimonials_data = [
    {'name': 'James Mutua', 'role': 'Volunteer — AJJ Member', 'quote': 'Serving at the Little Sisters has transformed my understanding of love. The elders receive visitors as angels. I leave every visit more blessed than when I arrived.', 'is_featured': True},
    {'name': 'Grace Wanjiku', 'role': 'Benefactor & Family Friend', 'quote': 'My mother spent her final years here, surrounded by Sisters who loved her as their own. The care, the prayers, the dignity — I am forever grateful.', 'is_featured': True},
    {'name': 'Dr. Samuel Ochieng', 'role': 'Medical Volunteer', 'quote': 'As a doctor, I have worked in many healthcare settings. None compare to the spirit of love that permeates every corner of this home. It is medicine for the soul.', 'is_featured': True},
    {'name': 'Sister Mary Clare, LSP', 'role': 'Little Sister of the Poor', 'quote': 'Saint Jeanne Jugan taught us: "Making the poor happy is all that counts." Every day in Mombasa, I see this truth made real.', 'is_featured': False},
]
for t in testimonials_data:
    if not Testimonial.objects.filter(name=t['name']).exists():
        Testimonial.objects.create(**t)
print(f"  ✓ {len(testimonials_data)} testimonials created")

# Prayer requests (sample approved ones)
prayers = [
    {'name': 'Mary A.', 'email': 'mary@example.com', 'request_type': 'health', 'intention': 'For healing from a long illness', 'status': 'approved', 'is_anonymous': False},
    {'name': 'Anonymous', 'email': 'anon@example.com', 'request_type': 'family', 'intention': 'For reconciliation in my family', 'status': 'approved', 'is_anonymous': True},
    {'name': 'Peter K.', 'email': 'peter@example.com', 'request_type': 'thanksgiving', 'intention': 'Thanksgiving for recovery from surgery', 'status': 'answered', 'is_anonymous': False},
]
for pr in prayers:
    if not PrayerRequest.objects.filter(intention=pr['intention']).exists():
        PrayerRequest.objects.create(**pr)
print(f"  ✓ {len(prayers)} prayer requests created")

# Upcoming events
today = date.today()
events_data = [
    {'title': 'Community Mass & Fellowship', 'event_type': 'mass', 'description': 'Join us for a special community Mass followed by fellowship and refreshments in the garden. All are welcome.', 'date': today + timedelta(days=7), 'start_time': '08:00', 'end_time': '10:00', 'location': 'Chapel & Garden, Little Sisters of the Poor'},
    {'title': 'Birthday Celebrations — June', 'event_type': 'birthday', 'description': 'Monthly birthday celebration for all residents born in June. Cake, music, and joy!', 'date': today + timedelta(days=14), 'start_time': '15:00', 'end_time': '16:30', 'location': 'Dining Hall, Little Sisters of the Poor'},
    {'title': 'Volunteer Orientation Day', 'event_type': 'training', 'description': 'Orientation for new Association Jeanne Jugan members and interested volunteers. Learn about our mission, values, and how you can serve.', 'date': today + timedelta(days=21), 'start_time': '09:00', 'end_time': '12:00', 'location': 'Little Sisters of the Poor, Tudor'},
    {'title': 'Annual Fundraising Gala', 'event_type': 'fundraiser', 'description': 'Our annual fundraising dinner supporting the care of our elderly residents. Dinner, entertainment, and an opportunity to meet the Little Sisters and those they serve.', 'date': today + timedelta(days=45), 'start_time': '18:00', 'end_time': '21:00', 'location': 'Whitesands Beach Hotel, Mombasa'},
]
for ev in events_data:
    if not Event.objects.filter(title=ev['title']).exists():
        Event.objects.create(created_by=admin_user, **ev)
print(f"  ✓ {len(events_data)} events created")

print("\n✅ Sample data loaded successfully!")
print("\n   Admin login: username=admin / password=Admin@1234!")
print("   Run: python manage.py runserver")
print("   Visit: http://localhost:8000")
