from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserData(models.Model):
    username = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, default='SOME STRING')
    password1 = models.CharField(max_length=250, default='SOME STRING')
    password2 = models.CharField(max_length=250, default='SOME STRING')

    dp = models.ImageField(upload_to="gallery", blank=True, null=True)

    def __str__(self):
        return self.username


class AddMovie(models.Model):
    title = models.CharField(max_length=250, default="SOME STRING")
    release = models.DateTimeField()
    description = models.TextField()
    movie_length = models.IntegerField()
    cover = models.ImageField(upload_to="gallery")
    genre = models.CharField(max_length=250, default="SOME STRING")
    url = models.CharField(max_length=250, default="SOME STRING")
    actor = models.CharField(max_length=250, blank=True, null=True)
    rating = models.CharField(max_length=250, default='SOME STRING')
    comment = models.CharField(max_length=250, default="SOME STRING")

    # def average_rating(self):
    #     ratings = self.ratings.all()
    #     if ratings:
    #         return sum([rating.rating for rating in ratings]) / len(ratings)
    #     return 0
    #
    #
    #
    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(AddMovie, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.TextField()

    def __str__(self):
        return f'Comment by {self.user.username} on {self.movie.title}'


# class Rating(models.Model):
#     movie = models.ForeignKey('AddMovie', on_delete=models.CASCADE, related_name='ratings')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         unique_together = ('movie', 'user')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
