from django.db import models


class Profile(models.Model):
    vk_id = models.IntegerField(null=False)
    first_name = models.CharField(null=False, max_length=100)
    last_name = models.CharField(null=False, max_length=100)
    is_closed = models.BooleanField(null=False)
    can_access_closed = models.BooleanField(null=False)
    sex = models.IntegerField(null=False)
    photo = models.CharField(null=False, max_length=100)

    deactivated = models.CharField(null=True, blank=True, max_length=100)

    # education
    university = models.IntegerField(null=True, blank=True)
    university_name = models.CharField(null=True, blank=True, max_length=100)
    faculty = models.IntegerField(null=True, blank=True)
    faculty_name = models.CharField(null=True, blank=True, max_length=100)
    graduation = models.IntegerField(null=True, blank=True)

    # personal
    political = models.IntegerField(null=True, blank=True)
    # langs: Optional[List[str]]
    religion = models.CharField(null=True, blank=True, max_length=100)
    inspired_by = models.CharField(null=True, blank=True, max_length=100)
    people_main = models.IntegerField(null=True, blank=True)
    life_main = models.IntegerField(null=True, blank=True)
    smoking = models.IntegerField(null=True, blank=True)
    alcohol = models.IntegerField(null=True, blank=True)

    # custom
    url = models.CharField(null=False, max_length=100, unique=True)
