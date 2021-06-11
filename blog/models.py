from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_register = models.BooleanField(default=False)
    is_cashier = models.BooleanField(default=False)

    """
    email = forms.EmailField(required=True)
    REQUIRED_FIELDS = ['email']
    """
    class Meta:
        swappable = 'AUTH_USER_MODEL'
#from django.core.urlresolvers import reverse
'''
#Command in the  shell to create Blog ' Post

import random
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from faker import Factory
fake = Factory.create()
s = ' '

user = User.objects.first()
for item in range(1,40):
    author = fake.name()
    title = s.join(fake.words(random.randint(4,16)))
    slug = slugify(title)
    #slugify the title
    status = 'published'
    body = s.join(fake.paragraphs(random.randint(2,10)))
    book = Post.objects.create(title=title, author=user, status=status, body=body, slug=slug )
    print(author)
    book.save()
'''

# Create your models here.

class Leave(models.Model):
    from_date = models.DateField(auto_now_add=True)
    to_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def date_diff(self):
        return (self.to_date - self.from_date).days


class PublishedManager(models.Manager):

    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                .filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
            ('draft', 'Draft'),
            ('published', 'Published'),
            )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    objects = models.Manager()
    published = PublishedManager()


    class Meta:
        ordering = ('-publish', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, 
            self.publish.strftime('%m'),
            self.publish.strftime('%d'),
            self.slug])


