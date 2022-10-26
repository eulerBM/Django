from tkinter import Widget
from django.db import models

class login_1 (models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    data = models.DateField()
