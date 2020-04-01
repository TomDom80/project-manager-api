from django.db import models


class Project(models.Model):
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner_ID = models.ForeignKey('auth.User', related_name='project_owner_ID', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, default='')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class ScopeOfWork(models.Model):  # Track
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner_ID = models.ForeignKey('auth.User', related_name='scopeofwork_owner_ID', on_delete=models.CASCADE)
    project_ID = models.ForeignKey('Project', related_name='scopeofwork_project_ID', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    description = models.TextField(blank=True, default='')
    scope = models.TextField(blank=True, default='')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.id) + '. ' + self.name


class ContactPerson(models.Model):
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner_ID = models.ForeignKey('auth.User', related_name='contactperson_owner_ID', on_delete=models.CASCADE)
    project_ID = models.ForeignKey('Project', related_name='contactperson_project_ID', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=False)
    position = models.CharField(max_length=100, unique=False)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class ContactData(models.Model):
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner_ID = models.ForeignKey('auth.User', related_name='contactdata_owner_ID', on_delete=models.CASCADE)
    contact_person_ID = models.ForeignKey('ContactPerson', related_name='contactdata_project_ID',
                                          on_delete=models.PROTECT)
    value = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100, unique=False)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class ProjectComment(models.Model):
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner_ID = models.ForeignKey('auth.User', related_name='projectcomment_owner_ID', on_delete=models.CASCADE)
    project_ID = models.ForeignKey('Project', related_name='projectcomment_project_ID', on_delete=models.CASCADE)
    content = models.TextField(blank=True, default='')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.content


class ProjectLocation(models.Model):
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner_ID = models.ForeignKey('auth.User', related_name='location_owner_ID', on_delete=models.CASCADE)
    project_ID = models.ForeignKey('Project', related_name='location_project_ID', on_delete=models.CASCADE)
    lat = models.FloatField(blank=True, default=None)
    lng = models.FloatField(blank=True, default=None)
    description = models.TextField(blank=True, default='')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.content
