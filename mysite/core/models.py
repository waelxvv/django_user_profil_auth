from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Telephone = models.IntegerField(null=True, blank=True)
    Adresse = models.CharField(max_length=30, blank=True)
    DateDeNaissance = models.DateField(null=True, blank=True)
    SalaireSouhaite = models.FloatField(null=True, blank=True)
    Motivation = models.CharField(max_length=150, blank=True)
    DateDeDisponibilite = models.DateField(null=True, blank=True)
    Reponse = models.CharField(max_length=30, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
