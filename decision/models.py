from django.db import models
from accounts.models import JobPosition, User
import uuid

class Meeting(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title=models.CharField('عنوان الجلسة', max_length=255)
    date=models.DateField('تاريخ الجلسة')
    metting_file = models.FileField(upload_to='uploads/',blank=True,null=True,default=None,max_length=250)
    job_position= models.ForeignKey(verbose_name="مستوى الجلسة",to=JobPosition, on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return f'{self.title}-{self.date}'
    class Meta:
        verbose_name="جلسة" 
        verbose_name_plural="جلسات"
class Decision(models.Model):
    name=models.TextField('عنوان المقرر')
    date=models.DateField('تاريخ المقرر')
    meettings=models.ForeignKey(verbose_name='الجلسات', to=Meeting, on_delete=models.CASCADE)
    responsible= models.ManyToManyField(verbose_name="التكاليف",to=User,blank=True,related_name='res')
    trailing= models.ManyToManyField(verbose_name="متابعة",to=User,blank=True,related_name='trail')
    decision_date=models.DateField('التاريخ المقرر')
    deadline=models.DateField('تاريخ التنفيذ')
    done=models.BooleanField('تم',default=False)
    def __str__(self):
        return f'{self.name}-{self.date}'
    class Meta:
        verbose_name="مقرر"
        verbose_name_plural="مقررات"


    
class Recommendation(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False ,blank=True,null=True)
    title=models.TextField('عنوان التوصيات')
    date=models.DateField('تاريخ التوصيات')

    def __str__(self):
        return f'{self.title}-{self.date}'
    class Meta:
        verbose_name="توصية"
        verbose_name_plural="توصيات"



class Rec(models.Model):
    title=models.CharField('عنوان التوصية', max_length=255)
    recommendation =models.ForeignKey(verbose_name="التوصية",to=Recommendation, on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return f'{self.title}'