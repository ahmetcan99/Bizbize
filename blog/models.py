from django.db import models
from django.utils import timezone
from users.models import CustomUser as User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.author}'s {self.id} numbered post"
    def get_absolute_url(self):
        return reverse("postDetail", kwargs={"pk": self.pk})
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.author.first_name} {self.author.last_name} on {self.post.author.first_name} {self.post.author.last_name}'s post"
        
class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reply by {self.author.first_name} {self.author.last_name} on {self.comment.author.first_name} {self.comment.author.last_name}'s comment on {self.comment.author.first_name} {self.comment.author.last_name}'s post"

class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} liked {self.post.author.first_name} {self.post.author.last_name}'s post"

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to='profile_pics', default='default.jpg')

    def __str__(self):
        return self.name + ' ' + self.surname