class Software(object):
  id=0
  name=None
  text=None
  downloadUrl=None
  applicationSubCategory=None
  screenshotList=[]
  linkList=[]
  imageList=[]
  review=None
  def __init__(self,id,name,text,downloadUrl,applicationSubCategory):
    self.id = id
    self.name = name
    self.text = text
    self.downloadUrl = downloadUrl
    self.applicationSubCategory = applicationSubCategory
  def __unicode__(self):
        return self.name

class Screenshot(object):
  url_screenshot=None
  def __init__(self,url_screenshot):
    self.url_screenshot=url_screenshot
  def __unicode__(self):
        return self.url_screenshot

class Link(object):
  url_link=None
  def __init__(self,url_link):
    self.url_link=url_link
  def __unicode__(self):
        return self.url_link

class Image(object):
  url_image=None
  def __init__(self,url_image):
    self.url_image=url_image
  def __unicode__(self):
        return self.url_image

class Review(object):
  reviewBody=None
  ratingValue=None
  def __init__(self,reviewBody,ratingValue):
    self.reviewBody=reviewBody
    self.ratingValue=ratingValue
  def __unicode__(self):
        return self.ratingValue


