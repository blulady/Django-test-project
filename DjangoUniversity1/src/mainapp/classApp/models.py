
from django.db import models

TITLES = {
    ('Physical Education', 'Physical Education'),
    ('History', 'History'),
    ('Geometry', 'Geometry'),
    ('English', 'English'),
    ('Chemestry', 'Chemestry')
}


class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, choices=TITLES)
    Instructor_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Course_Number = models.IntegerField(blank=True, null=True)
    Duration = models.FloatField(max_length=100)

    objects = models.Manager()

    def __str__(self):  # invoking python's module of string, it's going to return the db object as a string
        return self.Instructor_Name



