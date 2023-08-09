{\rtf1\ansi\ansicpg1252\cocoartf2753
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from django.db import models\
\
# Create your models here.\
class MenuItem(models.Model):\
   title = models.CharField(max_length=255) \
   price = models.DecimalField(max_digits=6, decimal_places=2) \
   inventory = models.SmallIntegerField()\
\
#    def get_item(self):\
#         return f'\{self.title\} : \{str(self.price)\}'\
\
   def __str__(self):\
        return f'\{self.title\} : \{str(self.price)\}'\
\
class Booking(models.Model):\
    name = models.CharField(max_length=255)\
    no_of_guests = models.SmallIntegerField()\
    reservation_date = models.DateField()\
\
    def __str__(self): \
        return self.first_name}