from django.db import models

class supermarketsale(models.Model):
    c_name=models.CharField(max_length=100)
    t_price=models.IntegerField(default=0)
    

    def __str__(self):
        return self.c_name
