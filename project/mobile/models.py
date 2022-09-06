from unicodedata import name
from django.db import models

# Create your models here.
class humanInfo(models.Model):
    name = models.CharField(max_length=10)
    phone_number=models.CharField(max_length=13)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True) # 생성시간
    
    class Meta :ordering=['created']
    
    
    
class diary(models.Model):
    diary_id = models.AutoField(primary_key = True)
    diary_date = models.DateTimeField(auto_now_add = True)
    diary_title = models.CharField(max_length = 20,)
    diary_content = models.TextField(max_length = 200)
    diary_todayme = models.CharField(max_length = 20, null = True, blank = True)
    diary_tomorrowme = models.CharField(max_length = 20, null = True, blank = True)
    diary_img = models.ImageField(upload_to = None, height_field = None, width_field = None, max_length = 100, null = True, blank = True)
#    user = models.ForeignKey(user, on_delete = models.CASCADE, null = True)
    def __str__(self):
        return self.diary_title