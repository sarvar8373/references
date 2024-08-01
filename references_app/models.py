from django.db import models
import math

class Soato(models.Model):
    id = models.IntegerField(primary_key=True)
    version = models.IntegerField()
    code = models.CharField(max_length=50)
    s_comment = models.TextField(null=True, blank=True)
    s_create = models.DateTimeField()
    s_status = models.CharField(max_length=10)
    name_ru = models.CharField(max_length=255)
    name_uz = models.CharField(max_length=255)
    name_uzl = models.CharField(max_length=255)
    name_center_ru = models.CharField(max_length=255, null=True, blank=True)
    name_center_uz = models.CharField(max_length=255, null=True, blank=True)
    name_center_uzl = models.CharField(max_length=255, null=True, blank=True)
    s_user_id = models.IntegerField()
    parent_code = models.CharField(max_length=50)
    keys = models.CharField(max_length=255)
    def __str__(self):
        return self.name_ru
    
class OPF(models.Model):
    version = models.IntegerField()
    code = models.IntegerField()
    s_comment = models.CharField(max_length=255, blank=True, null=True)
    s_create = models.DateTimeField()
    s_status = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255)
    name_uz = models.CharField(max_length=255)
    name_uzl = models.CharField(max_length=255)
    s_user_id = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True) 
    keys = models.CharField(max_length=255)
    def __str__(self):
        return self.name_ru
    def save(self, *args, **kwargs):
        if math.isnan(self.parent_id):
            self.parent_id = None 
        super().save(*args, **kwargs)

class OKONX(models.Model):
    version = models.IntegerField()
    code = models.IntegerField()
    s_comment = models.CharField(max_length=255, blank=True, null=True)
    s_create = models.DateTimeField()
    s_status = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255)
    name_uz = models.CharField(max_length=255)
    name_uzl = models.CharField(max_length=255)
    s_user_id = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)  
    keys = models.CharField(max_length=255)
    branch_code = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name_ru
    def save(self, *args, **kwargs):
        if math.isnan(self.parent_id):
            self.parent_id = None  

        super().save(*args, **kwargs)
    
class SOOGU(models.Model):
    version = models.IntegerField()
    code_okpo = models.IntegerField()
    s_comment = models.TextField()
    s_create = models.DateTimeField(null=True, blank=True)
    s_status = models.CharField(max_length=10)
    name_ru = models.CharField(max_length=255)
    name_uz = models.CharField(max_length=255)
    name_uzl = models.CharField(max_length=255)
    s_user_id = models.IntegerField()
    code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name_ru
    
    def save(self, *args, **kwargs):
        if math.isnan(self.code):
            self.code = None  

        super().save(*args, **kwargs)

class FS(models.Model):
    version = models.IntegerField()
    code = models.IntegerField()
    s_comment = models.CharField(max_length=255, blank=True, null=True)
    s_create = models.DateTimeField()
    s_status = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255)
    name_uz = models.CharField(max_length=255)
    name_uzl = models.CharField(max_length=255)
    s_user_id = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True) 
    keys = models.CharField(max_length=255)
    def __str__(self):
        return self.name_ru
    def save(self, *args, **kwargs):
        if math.isnan(self.parent_id):
            self.parent_id = None 
        super().save(*args, **kwargs)

class DOCTYPE(models.Model):
    version = models.IntegerField()
    keys = models.CharField(max_length=255)  
    s_comment = models.TextField(null=True, blank=True)
    s_create = models.DateTimeField(null=True, blank=True)
    s_status = models.CharField(max_length=10)
    name_ru = models.CharField(max_length=255)
    name_uz = models.CharField(max_length=255)
    name_uzl = models.CharField(max_length=255)
    name_short_ru = models.CharField(max_length=255, null=True, blank=True)
    name_short_uz = models.CharField(max_length=255, null=True, blank=True)
    name_short_uzl = models.CharField(max_length=255, null=True, blank=True)
    parent_id = models.IntegerField(null=True, blank=True)
    s_user_id = models.IntegerField()

    def __str__(self):
        return self.name_ru
    
    def save(self, *args, **kwargs):
        if math.isnan(self.parent_id):
            self.parent_id = None 
        super().save(*args, **kwargs)

class COUNTRY(models.Model):
    version = models.IntegerField()
    code = models.CharField(max_length=255)  
    s_comment = models.TextField(null=True, blank=True)
    s_create = models.DateTimeField(null=True, blank=True)
    s_status = models.CharField(max_length=10)
    name_ru = models.CharField(max_length=255)
    name_uz = models.CharField(max_length=255)
    name_uzl = models.CharField(max_length=255)
    name_short_ru = models.CharField(max_length=255, null=True, blank=True)
    name_short_uz = models.CharField(max_length=255, null=True, blank=True)
    name_short_uzl = models.CharField(max_length=255, null=True, blank=True)
    s_user_id = models.IntegerField()

    def __str__(self):
        return self.name_ru
    
class NATION(models.Model):
    version = models.IntegerField()
    s_comment = models.TextField(null=True, blank=True)
    s_create = models.DateTimeField(null=True, blank=True)
    s_status = models.CharField(max_length=10)
    name_ru = models.CharField(max_length=255)
    name_uz = models.CharField(max_length=255)
    name_uzl = models.CharField(max_length=255)
    s_user_id = models.IntegerField()

    def __str__(self):
        return self.name_ru