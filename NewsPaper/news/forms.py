from django import forms
from django.core.exceptions import ValidationError

from .models import Post

class PostForm(forms.ModelForm):
    post_text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'author',
            'post_title',
            'post_text',
            'post_rating'
        ]

    def clean(self):
        cleaned_data = super().clean()
        post_title = cleaned_data.get('post_title')
        post_text = cleaned_data.get('post_text')

        if post_text == post_title:
            raise ValidationError(
                "Описание не должно быть иденитично названию"
            )

        return cleaned_data