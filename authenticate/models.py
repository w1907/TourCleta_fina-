from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from catalogo.models import Bicicleta

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	telefono = models.CharField(max_length=20, blank=True)
	bicicletas = models.ManyToManyField(Bicicleta, blank=True)
	is_empleado = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()
