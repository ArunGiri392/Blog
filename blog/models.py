from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.first_name} ({self.last_name})"

class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
         return (self.caption)

class Post(models.Model):
    title = models.CharField(max_length=50)
    image_name = models.ImageField(upload_to="posts",null=True)
    date = models.DateTimeField(auto_now=True)
    excerpt = models.CharField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,related_name="posts",null=True)
    slug = models.SlugField(unique = True, db_index=True)
    tag = models.ManyToManyField(Tag)
    
    def __str__(self):
        return f"{self.title} ({self.author})"
  

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.user_name} ({self.user_email})"
  