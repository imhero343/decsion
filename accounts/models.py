from django.db import models

from django.contrib.auth.models import AbstractBaseUser , BaseUserManager,PermissionsMixin

from treebeard.mp_tree import MP_Node


class JobPosition(MP_Node):
    name = models.CharField(verbose_name='عنوان التكليف',max_length=30)
    node_order_by = ['name']

    def __str__(self):
        return 'Job : {}'.format(self.name)
    class Meta:
        verbose_name="تكليف"
        verbose_name_plural="تكاليف"

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):

        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name="اسم المستخدم",max_length=30,unique=True)
    telegram_user = models.CharField(verbose_name="اسم حساب التليكرام",default="",max_length=255)
    job_position= models.ManyToManyField(verbose_name="التكاليف",to=JobPosition,related_name='uj',through='Userjob',blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, verbose_name='ادمن')
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'


    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    class Meta:
        verbose_name="مستخدم"
        verbose_name_plural="مستخدمين"
class Userjob(models.Model):
    
    job_position= models.ForeignKey(to=JobPosition,verbose_name="تكليف",on_delete=models.CASCADE)
    user= models.ForeignKey(to=User,verbose_name="مستخدم",on_delete=models.CASCADE)
    timestamp= models.DateTimeField(auto_now_add=True,verbose_name='وقت اعطاء التكليف')
    
    def __str__(self):
        return f"{self.job_position}-{self.user}-{self.timestamp}"
    class Meta:
        unique_together = ('job_position', 'user',)
    class Meta:
        verbose_name="تكليف"
        verbose_name_plural="تكاليف"

class Constants(models.Model):
    title = models.CharField('العنوان',max_length=255,unique=True)
    text = models.TextField('النص',max_length=255)
    class Meta:
        verbose_name="ثابت"
        verbose_name_plural="ثوابت"
    def __str__(self):
        return f"{self.title}"