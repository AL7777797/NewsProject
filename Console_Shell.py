from django.contrib.auth.models import User
from news.models import Author, Category, Post, Comment

user1 = User.objects.create_user('username1')
user2 = User.objects.create_user('username2')

author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

history = Category.objects.create(name='history')
policy = Category.objects.create(name='policy')
technologies = Category.objects.create(name='technologies')
sport = Category.objects.create(name='sport')


post1 = Post.objects.create(author=author1, post_title='День в истории', post_text='Дуэль Пушкина')
post1.categories.add(history)

post2 = Post.objects.create(author=author2, post_title='Обзор матча', post_text='МЮ обыграл МС')
post2.categories.add(sport)

comment1 = Comment.objects.create(post=post1, user=user1, comment_text='Лол')
comment2 = Comment.objects.create(post=post1, user=user2, comment_text='азаза')
comment3 = Comment.objects.create(post=post2, user=user1, comment_text='*****')

post1.like()
post1.like()
post2.like()
comment1.like()
comment2.like()
comment3.dislike()
