from django import forms
from .models import NewPost

class NewPostForm (forms.ModelForm):
    class Meta:
        model=NewPost
        exclude=["date"]
        labels={
            "user_name": "Your Name",
            "user_email":"Your Email",
            "content":"Write Your Head Out Here!",
            "image_name":"Any image? Upload Here!",
            "title":"Post Title"
        }
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
