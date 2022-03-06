from django.db import models

# Create your models here.
class Post(models.Model):
    post_author = models.ForeignKey("accounts.AllUsers", on_delete=models.CASCADE)
    upload_time = models.DateTimeField(auto_now_add=True)
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='post_images/')

class Comment(models.Model):
    original_post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    comment_author = models.ForeignKey("accounts.AllUsers", on_delete=models.CASCADE)
    upload_time = models.DateTimeField(auto_now_add=True)
    comment_text = models.TextField()