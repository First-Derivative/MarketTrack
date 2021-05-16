from django.db import models
from UserAccounts.models import UserAccount

# from django.utils import timezone
from datetime import datetime

class AbstractSourceChoice(models.TextChoices):
  AMAZON = ("AZ", "Amazon")
  CURRYS = ("CU", "Currys")
  EBAY = ("EB", "Ebay")
  NEWEGG = ("NE","Newegg")

class Item(models.Model):
  '''
      Class Description
  '''
  name = models.CharField(max_length=80)
  source = models.CharField(max_length=200, default="LINK") 
  abstract_source = models.CharField(max_length=10, choices=AbstractSourceChoice.choices, default=AbstractSourceChoice.CURRYS)
  price = models.FloatField()
  stock_bool = models.BooleanField(default=True, verbose_name="stock_availability")
  stock_no = models.IntegerField(null=True, blank=True, default=-1)
  timestamp = models.DateTimeField(verbose_name="Tracking Timestamp", auto_now=False, auto_now_add=False, default=datetime.now)

  def __str__(self):
      return "{}: {}".format(self.name, self.source)

class Tracked(models.Model):
  '''
      Class Description        
  '''
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

  def __str__(self):
      return "{}: {}".format(self.item.name, self.user.username)

  class Meta:
      verbose_name_plural = "Tracked Items"

class PermanentTrack(models.Model):
  '''
      Class Description
  '''
  item = models.ForeignKey(Item, null=True,on_delete=models.SET_NULL)
  price = models.FloatField()
  # source = models.CharField(max_length=200, default="LINK")
  abstract_source = models.CharField(max_length=10, choices=AbstractSourceChoice.choices, default=AbstractSourceChoice.CURRYS)
  stock_bool = models.BooleanField(default=True)
  stock_no = models.IntegerField(null=True, blank=True, default=-1)
  timestamp = models.DateTimeField(verbose_name="Last Checked Timestamp", auto_now=False, auto_now_add=False, default=datetime.now)
  
  @property 
  def source(self):
    link = self.item.source
    return link

  class Meta:
      verbose_name = 'Permanently Tracked Item'
      verbose_name_plural = 'Permanently Tracked Items'