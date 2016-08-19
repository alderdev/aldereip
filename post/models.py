from django.db import models

# Create your models here.


class Post(models.Model):
    subject = models.CharField(max_length=60, null=False, blank=False )
    content = models.TextField(null=False, blank=False)

    create_at = models.DateTimeField(auto_now_add=True, auto_now =False)
    modify = models.DateTimeField(auto_now_add=False, auto_now =True)

    def __str__(self):
        return self.subject

    
