import unittest
import sqlite3
from softwareDao import DataAccessor
from software import Software, Screenshot, Link, Image,Review

class TestSoftwareDao(unittest.TestCase):

    def setUp(self):
        conn = sqlite3.connect("/Users/thiago/Documents/globo-exercises/admintechtudo/database")
        cursor = conn.cursor()
        sql = "DELETE FROM software_software"
        cursor.execute(sql)
        sql = "DELETE FROM software_screenshot"
        cursor.execute(sql)
        sql = "DELETE FROM software_link"
        cursor.execute(sql)
        sql = "DELETE FROM software_image"
        cursor.execute(sql)
        sql = "DELETE FROM software_review"
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        self.sDao = DataAccessor("/Users/thiago/Documents/globo-exercises/admintechtudo/database")
        
    def test_includeSoftware(self):
        software = Software(1,"name","text","downloadUrl","applicationSubCategory")
        software.imageList = [Image("teste")]
        software.LinkList = [Link("teste")]
        software.screenshotList = [Screenshot("teste")]
        software.review = Review("teste",1)
        self.sDao.includeSoftware(software)

    def test_readExistSoftware(self):
        conn = sqlite3.connect("/Users/thiago/Documents/globo-exercises/admintechtudo/database")
        conn.text_factory = str
        cursor = conn.cursor()
        software = [1,"teste", "teste", "teste", "teste"]
        cursor.execute("INSERT INTO software_software VALUES (?,?,?,?,?)", software)
        cursor.execute("INSERT INTO software_screenshot VALUES (?,?,?)", [1,1,"teste"])
        cursor.execute("INSERT INTO software_link VALUES (?,?,?)", [1,1,"teste"])
        cursor.execute("INSERT INTO software_image VALUES (?,?,?)", [1,1,"teste"])
        cursor.execute("INSERT INTO software_review VALUES (?,?,?,?)", [1,1,"teste",1])
        conn.commit()
        cursor.close()
        
        software = self.sDao.readSoftware(1)
        self.assertIsNotNone(software)
        self.assertEquals(len(software.screenshotList),1)
        self.assertEquals(len(software.linkList),1)
        self.assertEquals(len(software.imageList),1)
        self.assertIsNotNone(software.review)
        
    def test_deleteSoftware(self):
        conn = sqlite3.connect("/Users/thiago/Documents/globo-exercises/admintechtudo/database")
        conn.text_factory = str
        cursor = conn.cursor()
        software = [1,"teste", "teste", "teste", "teste"]
        cursor.execute("INSERT INTO software_software VALUES (?,?,?,?,?)", software)
        conn.commit()
        cursor.close()
        
        self.sDao.deleteSoftware(1)
        

if __name__ == '__main__':
    unittest.main()
