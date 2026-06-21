from django.db import models
class studentdata(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    s_id=models.CharField(max_length=100,unique=True)
    date_created=models.DateTimeField(auto_now_add=True)
    cgpa=models.CharField(max_length=100)
    semester=models.CharField(max_length=100)
def __str__(self):
    return studentdata.name