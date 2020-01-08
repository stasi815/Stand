from django.db import models

# Create your models here.
class Auction(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField('Start Date')
    end_date = models.DateTimeField('Auction Close Date')
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    starting_bid = models.FloatField(verbose_name='Starting Bid')
    min_bid_increment = models.FloatField(verbose_name='Minimun Bid Increment')
    value = models.FloatField()
    current_bid = models.FloatField(verbose_name='Current Highest Bid')
    image = models.ImageField()
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    specific_cause = models.CharField(max_length=200)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def __str__(self):
        return self.name