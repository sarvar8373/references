from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_user = models.BooleanField('Is user', default=False)

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=100)
    category_decription = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,  
        related_name='categories',  
        null=True,  
        blank=True 
    )

    def __str__(self):
        return self.category_name

class TableHeader(models.Model):
    category = models.ForeignKey(Category, related_name='headers', on_delete=models.CASCADE)
    header_name = models.CharField(max_length=100)
    references_category = models.ForeignKey(Category, related_name='header_references', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.header_name

class TableRow(models.Model):
    category = models.ForeignKey(Category, related_name='rows', on_delete=models.CASCADE)
    row_name = models.CharField(max_length=100)
    references_category = models.ForeignKey(Category, related_name='row_references', on_delete=models.CASCADE, null=True, blank=True)
    header = models.ForeignKey(TableHeader, related_name='headers', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.row_name