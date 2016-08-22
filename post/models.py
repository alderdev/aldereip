from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Post(models.Model):
    subject = models.CharField(max_length=60, null=False, blank=False )
    content = models.TextField(null=False, blank=False)

    create_at = models.DateTimeField(auto_now_add=True, auto_now =False)
    modify = models.DateTimeField(auto_now_add=False, auto_now =True)

    def __str__(self):
        return self.subject

    def get_absoulte_url(self):

        #return reverse('.views.detail', args=[str(self.id)])
        return "/post/detail/%s/" %( str(self.id) )

'''
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

'''
