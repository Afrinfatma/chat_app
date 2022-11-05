from django.db import models



class User(models.Model):
    user_name=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=255)
    email=models.EmailField(max_length=255,unique=True)
   

    def __str__(self):
        return self.user_name



class Messages(models.Model):
    group= models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField(blank=True,null=True)


