from django.db import models

class StaffMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    photo = models.ImageField(upload_to='staff_photos/')

    def __str__(self):
        return self.name


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('news', 'Yangiliklar'),
        ('projects', 'Loyihalar'),
        ('events', 'Tadbirlar'),
        ('announcements', 'E’lonlar'),
        ('grants', 'Grantlar'),
        ('articles', 'Maqolalar'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='news')
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

