from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone




# class User(models.Model):
#     email = models.CharField(max_length=50)
#     name = models.CharField(max_length=50)
#     surname = models.CharField(max_length=50)
#     login = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     regdate = models.DateTimeField(default=timezone.now)
#     veryfied = models.BooleanField(default='False')
#     active = models.BooleanField(default='False')
#     activatecode = models.CharField(max_length=50)
#     #comment = models.CharField(max_length=50)


class Post(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    created_date = models.DateTimeField(
            default=timezone.now)


class Like_Unlike(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    login_id = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.BooleanField(default='False')
    created_date = models.DateTimeField(
            default=timezone.now)

    def likeadd(self):
        self.save()
        t = Post.objects.get(pk=self.post_id_id)
        t.like = Like_Unlike.objects.filter(value=True, post_id=self.post_id).count()
        t.dislike = Like_Unlike.objects.filter(value=False, post_id=self.post_id).count()
        t.save()

    # def dislikeadd(self):
    #     self.save()
    #     t = Post.objects.get(pk=self.post_id_id)
    #     t.dislike = Like_Unlike.objects.filter(value=False, post_id=self.post_id).count()
    #     t.save()

