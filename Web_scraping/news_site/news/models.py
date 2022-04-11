from django.db import models

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


# class userModel(models.Model):
#     trading_code = models.CharField(max_length=100)
    
#     class Meta:
#         db_table = 'userInput'


class Company(models.Model):
    company_trading_code = models.CharField(max_length=50, primary_key=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_info = models.CharField(max_length=10000, blank=True, null=True)
    
    def __str__(self):
        return self.company_name


class News(models.Model):
    #trading_code = models.CharField(max_length=50, blank=True, null=True)
    trading_code = models.ForeignKey(Company, on_delete=models.CASCADE)
    news_title = models.CharField(max_length=255, blank=True, null=True)
    news = models.CharField(max_length=10000, blank=True, null=True)
    news_date = models.DateField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'news_news'
    
    def __str__(self):
        return self.news_title
        
        

    