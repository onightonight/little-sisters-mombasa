# Little Sisters of the Poor – Mombasa

**Django-powered web system for the Little Sisters of the Poor home in Tudor, Mombasa, Kenya.**

A full-stack website and REST API supporting the mission of the home: welcoming the needy elderly with love, dignity and faith since 1969.

---

## What's Included

| Feature | Details |
|---|---|
| **Homepage** | Full single-page site with all content sections |
| **Photo Gallery** | Category-filtered gallery with lightbox, served from DB |
| **Blog / News** | Published posts with slugs, SEO meta, tags, related posts |
| **Donations** | M-Pesa, Bank, PayPal; one-time & recurring; full bank details |
| **Volunteers / AJJ** | Registration form, opportunity cards, contact submission |
| **Prayer Requests** | Submit, moderate (admin), mark answered |
| **Events** | Upcoming events displayed on homepage & events section |
| **Testimonials** | Featured quotes from volunteers, donors & family members |
| **Service Times** | Mass/Rosary/Visitation schedule managed via admin |
| **Contact Messages** | All form submissions saved to DB, viewable in admin |
| **Vocation** | Discernment journey and the Four Vows |
| **REST API** | Full DRF API for all models |
| **Admin Panel** | Richly configured admin for all data |

---

## Models

| Model | Purpose |
|---|---|
| `Photo` | Gallery images with category, featured flag, alt text |
| `Donation` | All donation records — method, frequency, status |
| `Volunteer` | Volunteer registrations including emergency contacts |
| `BlogPost` | News & updates with SEO fields and auto-slug |
| `PrayerRequest` | Prayer intentions submitted by visitors |
| `ServiceAnnouncement` | Mass and service schedule |
| `Testimonial` | Quotes from volunteers, donors, family |
| `ContactMessage` | **New** — all contact/volunteer form submissions |
| `Event` | **New** — upcoming events shown on homepage |

---

## Quick Start

```bash
# Linux / Mac
bash quickstart.sh

# Windows
quickstart.bat
```

Then visit:
- **Website:** http://localhost:8000/
- **Admin:** http://localhost:8000/admin/ (admin / Admin@1234!)
- **API:** http://localhost:8000/api/

---

## API Endpoints

| Endpoint | Description |
|---|---|
| `GET /api/photos/` | All published photos |
| `GET /api/photos/featured/` | Featured photos (max 6) |
| `GET /api/photos/by_category/` | Counts by category |
| `GET /api/blog/` | Published blog posts |
| `GET /api/blog/{slug}/` | Single blog post by slug |
| `GET /api/blog/recent/` | 5 most recent posts |
| `POST /api/donations/` | Submit a donation record |
| `GET /api/donations/statistics/` | Donation totals (staff only) |
| `POST /api/volunteers/` | Register as volunteer |
| `GET /api/volunteers/statistics/` | Volunteer counts |
| `POST /api/prayers/` | Submit a prayer request |
| `GET /api/prayers/recent_answered/` | Recently answered prayers |
| `GET /api/services/` | Active service announcements |
| `GET /api/testimonials/featured/` | Featured testimonials |
| `POST /api/contact/` | Submit a contact message |
| `GET /api/events/` | Public upcoming events |
| `GET /api/events/upcoming/` | Next 10 upcoming events |

---

## Environment Variables

See `.env.example` for all available settings. Key ones:

```env
SECRET_KEY=...           # Change in production
DEBUG=False              # Set to False for production
DB_ENGINE=...            # postgresql for production
MPESA_CONSUMER_KEY=...   # Daraja API credentials
EMAIL_HOST_USER=...      # SMTP credentials
```

---

## Upgrading from Previous Version

New in this release:
- `ContactMessage` model — saves all form submissions to DB
- `Event` model — upcoming events on homepage
- `Volunteer.emergency_contact_*` fields
- `Donation.frequency` field (one-time / monthly / quarterly / annual)
- `BlogPost.meta_description` field for SEO
- `Photo.alt_text` field for accessibility
- `PrayerRequest.thanksgiving` type added
- `ServiceAnnouncement.novena` type added
- API endpoint: `/api/blog/{slug}/` (lookup by slug)
- API endpoint: `/api/photos/by_category/`
- API endpoint: `/api/contact/unread/` (staff)
- API endpoint: `/api/events/upcoming/`
- WhiteNoise static file serving
- Production security settings when `DEBUG=False`
- API rate throttling (100/hr anon, 1000/hr auth)
- Django-filters properly wired into REST_FRAMEWORK settings
- `BlogPost.save()` auto-sets `published_at` and `slug`

---

## Production Deployment

1. Set `DEBUG=False` in `.env`
2. Set a strong `SECRET_KEY`
3. Switch to PostgreSQL (`DB_ENGINE=django.db.backends.postgresql`)
4. Set `ALLOWED_HOSTS` to your domain
5. Run `python manage.py collectstatic`
6. Use Gunicorn: `gunicorn config.wsgi:application`
7. Configure Nginx to serve static/media files
8. Set up SSL (Let's Encrypt)

---

## Contact

**Little Sisters of the Poor — Mombasa**  
Tom Mboya Avenue, Tudor · P.O. Box 8429-80100 · Mombasa, Kenya  
📞 +254 733 346 352 · ✉️ admin@littlesisters-mombasa.org

*Sainte Jeanne Jugan, pray for us. Feast: 30th August.*
