
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    groups = ['Admin', 'Student', 'College']
    for group_name in groups:
        Group.objects.get_orcreate(name = group_name)