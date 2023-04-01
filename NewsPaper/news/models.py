from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField()

class Category(models.Model):
    tag_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tag_name.title()


class Post(models.Model):
    POST = 'post'
    ARTICLE = 'article'
    POST_TYPE_CHOICES = [
        (POST, 'Пост'),
        (ARTICLE, 'Статья'),
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=10, choices=POST_TYPE_CHOICES, default=POST)
    release_datetime = models.DateTimeField(auto_now_add=True)
    post_title = models.CharField(max_length=255)
    post_text = models.TextField()
    post_rating = models.IntegerField(default=0)

    categories = models.ManyToManyField(Category, through="PostCategory")

    def __str__(self):
        return f'{self.post_title.title()}: {self.post_text}'

    def preview(self):
        if len(self.post_text) > 124:
            return self.post_text[:124] + "..."
        else:
            return self.post_text

    def like(self):
        self.post_rating += 1
        self.save(update_fields=['post_rating'])

    def dislike(self):
        self.post_rating -= 1
        self.save(update_fields=['post_rating'])


class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    post_title = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_release = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save(update_fields=['comment_rating'])

    def dislike(self):
        self.comment_rating -= 1
        self.save(update_fields=['comment_rating'])

#
