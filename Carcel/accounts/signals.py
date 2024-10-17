from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

#
@receiver(post_save, sender=Profile)
def add_user_to_students_group(sender, instance, created, **kwargs):
    if created:
        try:
            group1=Group.objects.get(name='visitantes')
        except Group.DoesNotExist:
            group1 = Group.objects.create(name='visitantes')
            group2 = Group.objects.create(name='reclusos')
            group3 = Group.objects.create(name='administrativos')
        instance.user.groups.add(group1)