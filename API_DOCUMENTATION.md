# Django CMS API Documentation

This document describes the REST API endpoints available for the Little Sisters of the Poor CMS.

## Base URL
```
http://localhost:8000/api/
```

## Authentication

Some endpoints require authentication. Include your user token in headers:
```
Authorization: Token YOUR_TOKEN_HERE
```

---

## 📸 Photos Endpoint

### Get All Photos
```
GET /api/photos/
```

**Query Parameters:**
- `category`: Filter by category (elders, volunteers, events, facilities, community)
- `featured`: true/false
- `search`: Search by title or description
- `ordering`: Sort by field (-date_uploaded, views, etc)

**Example:**
```
GET /api/photos/?category=elders&ordering=-date_uploaded
```

**Response:**
```json
{
  "count": 12,
  "next": "http://localhost:8000/api/photos/?page=2",
  "results": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "title": "Elders at Prayer",
      "description": "...",
      "image": "http://localhost:8000/media/gallery/2025/03/photo.jpg",
      "category": "elders",
      "date_taken": "2025-03-25",
      "views": 42
    }
  ]
}
```

### Get Single Photo
```
GET /api/photos/{id}/
```

### Upload Photo (Admin Only)
```
POST /api/photos/
Content-Type: multipart/form-data

{
  "title": "Photo Title",
  "description": "Description",
  "image": <file>,
  "category": "elders",
  "photographer": "Name",
  "date_taken": "2025-03-25",
  "featured": true,
  "is_published": true
}
```

### Increment Photo Views
```
POST /api/photos/{id}/increment_views/
```

### Get Featured Photos
```
GET /api/photos/featured/
```

---

## 📝 Blog Posts Endpoint

### Get All Blog Posts
```
GET /api/blog/
```

**Query Parameters:**
- `search`: Search by title, content, or tags
- `ordering`: -published_at, views
- `status`: draft, published, archived

**Example:**
```
GET /api/blog/?status=published&ordering=-published_at
```

### Get Single Blog Post
```
GET /api/blog/{id}/
```

### Create Blog Post (Admin Only)
```
POST /api/blog/
Content-Type: application/json

{
  "title": "Blog Post Title",
  "slug": "blog-post-title",
  "excerpt": "Short summary",
  "content": "<h2>HTML content</h2>",
  "status": "published",
  "tags": "news, update, community",
  "allow_comments": true
}
```

### Get Recent Blog Posts
```
GET /api/blog/recent/
```

### Increment Blog Views
```
POST /api/blog/{id}/increment_views/
```

---

## 💰 Donations Endpoint

### Get All Donations (Admin Only)
```
GET /api/donations/
```

**Query Parameters:**
- `status`: pending, completed, failed, refunded
- `method`: mpesa, bank, crypto, paypal

### Create Donation
```
POST /api/donations/
Content-Type: application/json

{
  "donor_name": "John Doe",
  "donor_email": "john@example.com",
  "donor_phone": "+254700000000",
  "amount": 5000,
  "currency": "KES",
  "method": "mpesa",
  "message": "God bless your work",
  "is_anonymous": false
}
```

### Donation Statistics (Admin Only)
```
GET /api/donations/statistics/
```

**Response:**
```json
{
  "total_amount": 250000,
  "total_donations": 48,
  "average": 5208.33
}
```

---

## 👥 Volunteers Endpoint

### Get All Volunteers (Public Only Shows Active)
```
GET /api/volunteers/
```

**Query Parameters:**
- `status`: registered, active, inactive, vetted
- `skills`: healthcare, cooking, cleaning, teaching, etc
- `search`: Search by name or email

### Register as Volunteer
```
POST /api/volunteers/
Content-Type: application/json

{
  "first_name": "Mary",
  "last_name": "Jane",
  "email": "mary@example.com",
  "phone": "+254700000000",
  "date_of_birth": "1990-05-15",
  "address": "Mombasa, Kenya",
  "skills": "healthcare",
  "motivation": "I want to serve the elderly",
  "availability": "Weekends and evenings",
  "preferred_activities": "Healthcare, companionship"
}
```

### Volunteer Statistics (Admin Only)
```
GET /api/volunteers/statistics/
```

**Response:**
```json
{
  "total_volunteers": 34,
  "active_volunteers": 28,
  "total_hours": 1240.5
}
```

---

## 🙏 Prayer Requests Endpoint

### Get Approved Prayer Requests
```
GET /api/prayers/
```

### Submit Prayer Request
```
POST /api/prayers/
Content-Type: application/json

{
  "name": "John",
  "email": "john@example.com",
  "request_type": "health",
  "intention": "Please pray for my mother's recovery",
  "is_for_self": false,
  "who_for": "My mother",
  "is_anonymous": true
}
```

### Get Recently Answered Prayers
```
GET /api/prayers/recent_answered/
```

---

## 📢 Service Announcements Endpoint

### Get All Active Services
```
GET /api/services/
```

**Query Parameters:**
- `service_type`: mass, rosary, visitation, event
- `day_of_week`: Monday, Tuesday, etc

### Get Services for a Specific Day
```
GET /api/services/?day_of_week=Sunday
```

---

## 💬 Testimonials Endpoint

### Get Published Testimonials
```
GET /api/testimonials/
```

### Get Featured Testimonials
```
GET /api/testimonials/featured/
```

**Response:**
```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "name": "Maria Santos",
    "role": "Volunteer",
    "quote": "Working here has been life-changing...",
    "is_featured": true,
    "is_published": true
  }
]
```

---

## Error Responses

All endpoints return consistent error responses:

### 400 Bad Request
```json
{
  "field_name": ["This field is required."]
}
```

### 403 Forbidden
```json
{
  "detail": "Authentication credentials were not provided."
}
```

### 404 Not Found
```json
{
  "detail": "Not found."
}
```

### 500 Server Error
```json
{
  "detail": "Internal server error"
}
```

---

## Pagination

List endpoints return paginated results:

```json
{
  "count": 50,
  "next": "http://localhost:8000/api/photos/?page=2",
  "previous": null,
  "results": [...]
}
```

Default page size is 12 items. Change with: `?page=2`

---

## Rate Limiting

Currently no rate limiting is implemented. For production, consider adding rate limiting via django-ratelimit or similar.

---

## CORS

The API supports Cross-Origin Resource Sharing (CORS). Frontend applications can make requests from:
- localhost:3000
- localhost:8000
- 127.0.0.1:3000

---

## Example Requests

### Using Python Requests
```python
import requests

# Get all photos
response = requests.get('http://localhost:8000/api/photos/')
photos = response.json()

# Create a donation
donation_data = {
    'donor_name': 'John Doe',
    'donor_email': 'john@example.com',
    'amount': 5000,
    'currency': 'KES',
    'method': 'mpesa'
}
response = requests.post(
    'http://localhost:8000/api/donations/',
    json=donation_data
)
```

### Using JavaScript/Fetch
```javascript
// Get photos
fetch('/api/photos/?category=elders')
  .then(response => response.json())
  .then(data => console.log(data));

// Submit prayer
fetch('/api/prayers/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    name: 'John',
    email: 'john@example.com',
    request_type: 'health',
    intention: 'Prayer for healing'
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

### Using cURL
```bash
# Get photos
curl "http://localhost:8000/api/photos/"

# Create donation
curl -X POST http://localhost:8000/api/donations/ \
  -H "Content-Type: application/json" \
  -d '{
    "donor_name": "John",
    "donor_email": "john@example.com",
    "amount": 5000,
    "currency": "KES",
    "method": "mpesa"
  }'
```

---

## Support

For API issues or questions, refer to:
- Django REST Framework Documentation: https://www.django-rest-framework.org/
- Django Documentation: https://docs.djangoproject.com/
