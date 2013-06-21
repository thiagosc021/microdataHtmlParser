import html5lib
import urllib
import microdata
import lxml.html as lhtml
from softwareDao import DataAccessor
from software import Software, Screenshot, Link, Image,Review

def parseHtml(url):
  '''
    Metodo que faz o parse dos dados estruturados existentes no html
    usando a classe microdata:https://github.com/edsu/microdata
    e as libs 
          html5lib:https://github.com/html5lib/html5lib-python
          lxml:http://lxml.de/index.html
  '''
  location=urllib.urlopen(url)
  html=lhtml.fromstring(location.read())
  softwareHtmlString= html.get_element_by_id("software")
  items = microdata.get_items(lhtml.tostring(softwareHtmlString))
  if len(items):
    return items[0]
  else:
    return None

def parseHtmlToObject(item):
  software = Software(1,str(item.name), item.text, str(item.downloadUrl), str(item.applicationSubCategory))
  images = []
  for image in item.get_all('image') :
    images.append(Image(str(image)))
  software.imageList = images
  
  screenshots = []
  for screenshot in item.get_all('screenshot') :
    screenshots.append(Screenshot(str(screenshot)))
  software.screenshotList=screenshots
  
  urls = []
  for url in item.get_all('url') :
    urls.append(Link(str(url)))
  software.linkList=urls
  
  software.review = Review(item.review.reviewBody,item.review.ratingValue)
  return software

def saveInDataBase(software,dataBase):

  sDao= DataAccessor(dataBase)
  
  sDao.deleteSoftware(1)
  
  sDao.includeSoftware(software)


if __name__ == "__main__":

  item = parseHtml("http://www.techtudo.com.br/tudo-sobre/s/google-chrome.html")
  software = parseHtmlToObject(item)
  saveInDataBase(software,"/Users/thiago/Documents/globo-exercises/admintechtudo/database")
