# Admin Panel User Guide

This guide explains how to use the admin panel to manage your website content.

## 🔐 Logging In

1. Go to: http://localhost:8000/admin/
2. Enter your username and password
3. Click "Log in"

**Default credentials:**
- Username: `admin`
- Password: `admin123` (change this!)

---

## 📸 Managing Photos

### Access the Photos Section
1. Click on **Photos** in the left menu
2. You'll see a list of all photos

### Adding a New Photo

1. Click the green **+ Add Photo** button
2. Fill in the following fields:

**Title** (Required)
- Name of the photo (e.g., "Volunteers Helping with Meal Time")
- Keep it descriptive and concise

**Description**
- Add more details about the photo
- What's happening, who's in it, any special moments

**Image** (Required)
- Click "Choose File" to upload a photo
- Supported formats: JPG, PNG, GIF, WebP
- Maximum size: 10MB
- Recommended: 1200x800px or larger for best quality

**Category** (Required)
- Select from:
  - 👴 **Elders** - Photos of residents
  - 🤝 **Volunteers** - Photos of volunteers
  - 🎉 **Events** - Special events and celebrations
  - 🏠 **Facilities** - Building and rooms
  - 👥 **Community** - Community activities

**Photographer**
- Name of the person who took the photo
- Optional but helpful for attribution

**Date Taken**
- When was this photo taken?
- Use the calendar picker

**Featured** ⭐
- Check this box to show on the homepage gallery
- Only 6 featured photos display on homepage
- Update this to rotate featured photos

**Is Published**
- Check to make the photo visible on the website
- Uncheck to hide/draft photos

### Editing a Photo

1. Click on a photo in the list to open its details
2. Make your changes
3. Click **Save** or **Save and continue editing**

### Deleting a Photo

1. Open the photo details
2. Scroll to the bottom
3. Click the red **Delete** button
4. Confirm the deletion

### Tips for Good Photos

- 📸 Use high-quality images (clear and well-lit)
- 🎯 Crop to focus on the subject
- 🏷️ Use descriptive titles and descriptions
- 👤 When photographing people, have permission
- 📅 Set the correct date taken
- ⭐ Feature your best photos on the homepage

---

## 📝 Managing Blog Posts

### Access the Blog Section
1. Click on **Blog Posts** in the left menu
2. You'll see a list of all blog posts

### Creating a New Blog Post

1. Click the green **+ Add Blog Post** button
2. Fill in the following fields:

**Title** (Required)
- The main headline of your post
- Make it engaging and informative
- Example: "Spring Cleaning Day at Our Home"

**Slug** (Auto-filled)
- URL-friendly version of the title
- Auto-generated from title, but you can customize
- Only letters, numbers, and hyphens
- Used in the URL: `/blog/your-slug/`

**Author** (Required)
- Select who wrote this post
- Usually yourself (admin)

**Excerpt** (Required)
- Short summary (1-2 sentences)
- Appears in blog listings
- Make it compelling!

**Content** (Required)
- The full article text
- Supports HTML formatting
- Use these common HTML tags:
  ```html
  <h2>Heading 2</h2>
  <h3>Heading 3</h3>
  <p>Paragraph</p>
  <strong>Bold</strong>
  <em>Italic</em>
  <ul><li>Bullet list</li></ul>
  <ol><li>Numbered list</li></ol>
  <blockquote>Quote</blockquote>
  ```

**Featured Image**
- Optional cover photo for the post
- Shows on blog listing and at top of article
- Recommended: 1200x600px or 16:9 aspect ratio

**Status** (Required)
- **Draft** - Work in progress, not visible on website
- **Published** - Live on the website
- **Archived** - Hidden from normal view, but kept in system

**Tags**
- Comma-separated keywords
- Example: "elders, cooking, volunteers, springtime"
- Helps with organization and search

**Allow Comments**
- Check to let readers comment (if enabled)

### Publishing a Blog Post

1. Complete all the post details
2. Set Status to **Published**
3. The post will appear on:
   - Blog page: `/blog/`
   - Individual post: `/blog/your-slug/`
   - Homepage (in recent updates section)

### Scheduling a Post (Future)

Currently, posts are published immediately. Future versions will support:
- Scheduled publishing at a specific date/time
- Automatic social media sharing

### Editing a Blog Post

1. Click on the post title in the list
2. Make your changes
3. Click **Save** or **Save and continue editing**

### Deleting a Blog Post

1. Open the post details
2. Scroll to the bottom
3. Click the red **Delete** button
4. Confirm deletion

### Writing Great Blog Posts

✍️ **Tips for good content:**
1. **Start with a hook** - First 2 sentences should grab attention
2. **Use clear headings** - Break content into sections
3. **Keep paragraphs short** - 2-4 sentences each
4. **Use lists** - Easier to read than dense paragraphs
5. **Include images** - Makes posts more engaging
6. **Proofread** - Check spelling and grammar
7. **Add tags** - Help readers find related posts
8. **Link relevant** - Link to related blog posts in your text
9. **End with reflection** - Wrap up with a meaningful thought
10. **Save as draft first** - Write, save, review, then publish

### Example Blog Post Structure

```
Title: "A Beautiful Day of Service at Our Home"

Excerpt: "Volunteers and residents came together to celebrate 
community, love, and service on this memorable afternoon."

Content:
<h2>A Day of Joy and Community</h2>
<p>Last Saturday was a special day at our home. 
Volunteers arrived early with smiles and ready hearts...</p>

<h3>Morning Preparations</h3>
<p>The kitchen team prepared a delicious meal...</p>

<h3>Afternoon Celebrations</h3>
<p>After lunch, we gathered for songs and stories...</p>

<h3>Grateful Hearts</h3>
<p>As the day ended, we were reminded of why we do this work...</p>

Tags: volunteers, community, service, joy, elderly
```

---

## 👥 Managing Donations (Admin Only)

### View Donations
1. Click on **Donations** in the left menu
2. See all donations by date

### Donation Statuses
- **Pending** - Awaiting processing
- **Completed** - Successfully received
- **Failed** - Payment failed
- **Refunded** - Refund processed

### Donation Methods
- **M-Pesa** - Mobile money payment
- **Bank Transfer** - Direct bank transfer
- **PayPal** - Online payment
- **Crypto** - Cryptocurrency donation
- **Other** - Other payment methods

---

## 👨‍🤝‍👩 Managing Volunteers (Admin Only)

### View Volunteer Registrations
1. Click on **Volunteers** in the left menu
2. Review volunteer applications

### Volunteer Statuses
- **Registered** - New registration
- **Active** - Currently volunteering
- **Inactive** - Not currently serving
- **Vetted** - Background check completed

### Tracking Volunteer Hours
- Record hours contributed
- Track total volunteer hours for reporting

---

## 🙏 Managing Prayer Requests (Admin Only)

### Review Prayer Requests
1. Click on **Prayer Requests** in the left menu
2. See pending requests

### Prayer Request Workflow
1. New request submitted → Status: **Pending**
2. Review the intention
3. Set Status to **Approved** to publish on website
4. When prayer is answered, set Status to **Answered**
5. Add notes about the answer if desired

---

## 📊 Dashboard Statistics

The admin dashboard shows:
- Total photos and recent uploads
- Blog post statistics
- Donation totals and methods
- Volunteer participation
- Prayer request activity
- Website visitor activity (if analytics enabled)

---

## ⚙️ Account Settings

### Change Your Password

1. Click your username in top-right corner
2. Click **Change Password**
3. Enter your current password
4. Enter new password (twice)
5. Click **Change My Password**

**Password Tips:**
- Use at least 8 characters
- Mix uppercase, lowercase, numbers, symbols
- Don't use easily guessed words
- Change regularly for security

### Profile Settings

1. Click your username in top-right corner
2. Click **View Site** to go to homepage
3. Edit your name, email, etc.

---

## 🔍 Search and Filter

### Search Photos
1. In the Photos list, use the search box
2. Search by: title, description, category
3. Results update as you type

### Filter Blog Posts
1. In Blog Posts list, click on Status filter
2. Show only: Draft, Published, or Archived
3. Click filter again to clear

### Sort Lists
- Click column header to sort
- Click again to reverse sort order

---

## 📤 Exporting Data (Future Feature)

Coming soon:
- Export photos list to CSV
- Export blog posts archive
- Export donation reports
- Export volunteer hours

---

## 🆘 Troubleshooting

### "I can't upload images"
- Check file size (max 10MB)
- Check file format (JPG, PNG, etc)
- Check disk space on server
- Check folder permissions

### "My changes aren't showing on the website"
- Make sure you clicked **Save**
- Check that **Is Published** is checked (for photos)
- Check that **Status** is **Published** (for blog posts)
- Clear your browser cache (Ctrl+Shift+Delete)

### "I accidentally deleted something"
- Contact your site administrator
- Database backups may recover deleted items

### "Admin panel is slow"
- Too many photos/posts loaded
- Use search/filter to narrow results
- Try in a different browser
- Contact site administrator

---

## 🔒 Security Best Practices

1. **Change your password immediately** after first login
2. **Log out** when you're done (click logout in top-right)
3. **Don't share** your admin password with others
4. **Never** use simple passwords like "password123"
5. **Be careful** with other users' permissions
6. **Report suspicious** activity to administrator

---

## 📞 Help & Support

### If you need help:
1. Check this guide first
2. Look at similar content you've created before
3. Try using the "Help" links in the admin panel
4. Contact your site administrator
5. Email: admin@littlesisters-mombasa.org

### What's available now:
- ✅ Photo gallery management
- ✅ Blog/news posts
- ✅ Admin dashboard

### Coming soon:
- 🔜 Donation tracking
- 🔜 Volunteer management
- 🔜 Prayer request system
- 🔜 Email notifications
- 🔜 Advanced analytics

---

## 📚 Quick Reference

### Keyboard Shortcuts
- **Save**: Ctrl+S (or Cmd+S on Mac)
- **Delete**: Usually a red button at bottom of form
- **Logout**: Click username → Logout

### Common Tasks
| Task | Steps |
|------|-------|
| Add a photo | Photos → + Add Photo → Fill form → Save |
| Write a blog post | Blog Posts → + Add Blog Post → Fill form → Publish |
| Feature a photo | Photo → Check "Featured" → Save |
| Archive a blog post | Blog Post → Status: Archived → Save |
| View website | Click "View Site" in top-right |
| Change password | Username → Change Password |

---

## 🎓 Learning More

For more advanced features:
- Django Admin Documentation: https://docs.djangoproject.com/en/4.2/ref/contrib/admin/
- Photo editing: Use free tools like Canva, Pixlr, or GIMP
- Writing tips: Read established blogs for inspiration

---

**Happy managing! 🎉**

For questions, contact your site administrator.
