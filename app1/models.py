from django.db import models

cloths=[
       ('001','T-shirt'),
       ('002','Jeans'),
       ('003','frocks'),
       ('004','kurthi'),
        ]

class shop(models.Model):
    cloth_name=models.CharField(max_length=100)
    quantity=models.IntegerField(null=True)
    price=models.BigIntegerField(null=True)
    def __str__(self):
        return self .cloth_name
