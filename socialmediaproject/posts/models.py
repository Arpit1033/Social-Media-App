from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/%y/%m/%d')
    caption = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length = 200,blank=True) # Useful when we want to associate any url
    # auto_now_add = True : Automatically add current date to the post
    created = models.DateField(auto_now_add=True)
    # For saving list of people who liked a post (Many to Many Relationship)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='posts_liked',blank=True)
    
    def __str__(self):
        return self.title
    
    # Overwriting the inbuilt 'save()' method of 'Post' class
    def save(self,*args,**kwargs):
        # If current object doesn't have a slug, we need to create one for it.
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)