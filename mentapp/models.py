from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Tag(models.Model):
    usertype= models.CharField(max_length=20)

    def __str__(self):
        return f"{self.usertype}"


class NewPost(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(validators=[MinLengthValidator(10)])
    image_name = models.ImageField(upload_to="posts", null=True, blank=True)
    date = models.DateField(auto_now=True)
    # slug = models.SlugField(unique=True, db_index=True)
    user_name= models.CharField(max_length=20)
    user_email=models.EmailField()
    usertype= models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title} one {self.date}"

