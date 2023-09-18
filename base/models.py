from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# This is a class based data model that will be
# applied to a SQL database using database migrations
# We are representing our database schema as a python class
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # when we reference a Task object we return the title from the database
        return self.title

    class Meta:
        # We order queries by the complete column/row
        ordering = ['complete']
