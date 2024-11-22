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
    name = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='members/',
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
    )
    designation = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
        db_table = 'club_members'
        ordering = ['-created_at']
