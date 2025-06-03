from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Tags"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name_plural = "Tasks"
        ordering = ["is_complete", "-date"]

    def __str__(self):
        return self.content
