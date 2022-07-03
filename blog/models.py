from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db import models


class Post(models.Model):
    post_title = models.CharField(max_length=300, blank=False, null=False)
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.post_title