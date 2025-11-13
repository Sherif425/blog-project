from django.db import models
from datetime import timezone
# from django.db.models.functions import Now

# Create your models here.
class Post(models.Model):
    class Status(models.Model):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    
    publish = models.DateTimeField(default=timezone.now)
    
    # another way to define time 
    # publish = models.DateTimeField(db_default=Now())

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
 

    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )
    
    class Meta:
        # sorting posts, - means descending order
        ordering = ['-publish']
        # define a database index for the publish field
        indexes = [
            models.Index(fields=['-publish']),
        ]
    

    
    
    def __str__(self):
        return self.title
    