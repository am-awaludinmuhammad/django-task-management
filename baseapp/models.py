from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    # add additional fields in here

    class Meta:
        db_table = 'users'
        
    def __str__(self):
        return self.username

class Task(models.Model):
    BACKLOG = 'backlog'
    NEW = 'new'
    DOING = 'doing'
    REVISION = 'revision'
    DONE = 'done'

    states = (
        (BACKLOG, "Backlog"),
        (NEW, "New"),
        (DOING, "Doing"),
        (REVISION, "Revision"),
        (DONE, "Done"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.TextField(choices=states, default=BACKLOG)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = '"public"."tasks"'