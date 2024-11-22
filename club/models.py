from django.core.validators import FileExtensionValidator
from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='gallery/',
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'
        db_table = 'club_gallery'
        ordering = ['-created_at']


class Member(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(
        upload_to='members/',
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
    )
    batch = models.IntegerField(default=0)
    education = models.CharField(max_length=100)
    roll = models.IntegerField(default=0)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    problem_solving_experience = models.CharField(max_length=255)
    expectation = models.CharField(max_length=255)
    joined_date = models.DateField(null=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    transaction_id = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
        db_table = 'club_members'
        ordering = ['-created_at']
