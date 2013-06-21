from django.db import models

class Software(models.Model):
  name=models.CharField(max_length=500)
  text=models.TextField()
  downloadUrl=models.CharField(max_length=500)
  applicationSubCategory=models.CharField(max_length=500)
  def __unicode__(self):
        return self.name

class Screenshot(models.Model):
  software=models.ForeignKey(Software)
  url_screenshot=models.CharField(max_length=500)
  def __unicode__(self):
        return self.url_screenshot

class Link(models.Model):
  software=models.ForeignKey(Software)
  url_link=models.CharField(max_length=500)
  def __unicode__(self):
        return self.url_link

class Image(models.Model):
  software=models.ForeignKey(Software)
  url_image=models.CharField(max_length=500)
  def __unicode__(self):
        return self.url_image

class Review(models.Model):
  software=models.ForeignKey(Software)
  reviewBody=models.TextField()
  ratingValue=models.DecimalField(max_digits=5,decimal_places=2)
  def __unicode__(self):
        return self.ratingValue


