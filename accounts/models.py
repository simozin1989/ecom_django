from enum import auto
from django.db import models

from django.contrib.auth.models import User
from django.db.models.deletion import ProtectedError
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
import datetime
from django_countries.fields import CountryField
from django.utils.text import slugify
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User ,verbose_name='user',on_delete=models.CASCADE)
    slug = models.SlugField(blank=True,null=True)
    address = models.CharField(max_length=100)
    image = models.ImageField(_('image'),upload_to='profile_img',blank=True,null=True)
    join_date = models.DateTimeField(_('join_date'),default=datetime.datetime.now)
    country = CountryField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile,self).save(*args, **kwargs)    

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return  '%s' %(self.user)

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"pk": self.slug})


    def craet_profil(sender, *args, **kwargs):
        if kwargs['created']:
            user_profil = Profile.objects.create(user=kwargs['instance'])


    post_save.connect(craet_profil,sender=User)        

