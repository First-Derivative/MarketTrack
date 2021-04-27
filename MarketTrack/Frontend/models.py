from django.db import models
from UserAccounts.models import UserAccount

# from django.utils import timezone
from datetime import datetime

'''
class AbstractSourceChoice(models.TextChoices):
    AMAZON = ("AZ", "Amazon")
    CURRYS = ("CU", "Currys")
    EBAY = ("EB", "Ebay")
    NEWEGG = ("NE","NewEgg")
    
'''

class Item(models.Model):
    '''
        Class Description
    '''

    name = models.CharField(max_length=80)
    source = models.CharField(max_length=200) #closest unique identifier: URL for item page
    # abstract_source = models.CharField(max_length=10, choices=AbstractSourceChoice.choices, default=AbstractSourceChoice.AMAZON)
    price = models.FloatField()
    stock_bool = models.BooleanField(null=True, blank=True)
    stock_no = models.IntegerField(null=True, blank=True)
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

class Collection(models.Model):
    name = models.CharField(max_length=80)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

    def __str__(self):
        return "{}: {}".format(self.name, self.user.username)

class CollectionItems(models.Model): 

    collection = models.ForeignKey('Collection', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return "{}: {}".format(self.collection.name, self.item.name)

    class Meta:
        verbose_name_plural = "Collection Items"